## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask_app.config.celery_worker import celery
from flask_app.utils.openai_helper import call_openai_with_tool
from flask_app.models.noticia_model import Noticia

@celery.task
def analisis_sesgo_task(noticia_id, texto, usuario_id):
    narrative_bias_schema = [
        {
            "name": "score_bias", # Changed from type/function format to old API format
            "description": "Evaluates the narrative bias of the author across multiple ideological axes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "economic": {
                        "type": "object",
                        "properties": {
                            "score": { "type": "number" },
                            "label": { "type": "string" },
                            "confidence": { "type": "number" },
                            "features": {
                                "type": "array",
                                "items": { "type": "string" }
                            }
                        },
                        "required": ["score", "label", "confidence", "features"]
                    },
                    "cultural": {
                        "type": "object",
                        "properties": {
                            "score": { "type": "number" },
                            "label": { "type": "string" },
                            "confidence": { "type": "number" },
                            "features": {
                                "type": "array",
                                "items": { "type": "string" }
                            }
                        },
                        "required": ["score", "label", "confidence", "features"]
                    },
                    "institutional": {
                        "type": "object",
                        "properties": {
                            "score": { "type": "number" },
                            "label": { "type": "string" },
                            "confidence": { "type": "number" },
                            "features": {
                                "type": "array",
                                "items": { "type": "string" }
                            }
                        },
                        "required": ["score", "label", "confidence", "features"]
                    },
                    "summary": {
                        "type": "string"
                    }
                },
                "required": ["economic", "cultural", "institutional", "summary"]
            }
        }
    ]

    prompt = f"""
    Eres un analista de sesgo mediático encargado de evaluar el **sesgo narrativo ideológico** de un texto. No estás evaluando el sesgo de los eventos o personas descritas, sino el sesgo del **autor o narrador** basado en cómo se presenta el contenido.

    Tu objetivo es determinar **cómo el autor enmarca**, critica, respalda o reacciona a los eventos, citas y políticas mencionadas.

    Enfócate en los siguientes aspectos:

    1. **Tono y Lenguaje**
        - Detecta tono emocional, sarcástico, irónico o despectivo.
        - Busca adjetivos o adverbios que indiquen aprobación o desaprobación.

    2. **Enmarcado y Comentarios**
        - Nota cuando el autor elogia, critica o cuestiona personas o políticas.
        - Distingue entre contenido citado y cómo el autor introduce o interpreta la cita.

    3. **Selectividad y Omisión**
        - Evalúa si el autor presenta una perspectiva unilateral.
        - Identifica alineación ideológica basada en lo que se enfatiza u omite.

    4. **Atribución de Intenciones**
        - Señala frases que asignen motivos o juicios morales a actores políticos.

    Devuelve una evaluación de sesgo en **tres ejes ideológicos**, basada en la postura narrativa del autor:

    - **Económico** (izquierda ↔ derecha)
    - **Cultural** (progresista ↔ conservador)
    - **Institucional** (anti-élite ↔ pro-establecimiento)

    Para cada eje, devuelve:
    - `score`: un número decimal entre -1 (fuertemente izquierda/progresista/anti-élite) y 1 (fuertemente derecha/conservador/pro-establecimiento)
    - `label`: una etiqueta cualitativa (ej., "izquierda", "centro-derecha")
    - `confidence`: entre 0 y 1
    - `features`: una lista de frases o expresiones clave que indican sesgo

    También devuelve un `summary` que explique la **posición narrativa** general del autor, aclarando explícitamente si el autor **apoya o critica** las ideas y acciones descritas.

    Debes **distinguir entre el sesgo del narrador y el sesgo de las personas que cita o describe**.

    IMPORTANTE: Tu respuesta DEBE ser en español. Proporciona la explicación completamente en español.

    Texto:
    \"\"\"
    {texto}
    \"\"\"
    """

    retorno = False
    max_intentos = 3
    intentos = 0
    
    # Inicializar result con un valor predeterminado
    default_result = {
        "economic": {
            "score": 0,
            "label": "No determinado",
            "confidence": 0,
            "features": ["No se pudo analizar el sesgo económico"]
        },
        "cultural": {
            "score": 0,
            "label": "No determinado",
            "confidence": 0,
            "features": ["No se pudo analizar el sesgo cultural"]
        },
        "institutional": {
            "score": 0,
            "label": "No determinado",
            "confidence": 0,
            "features": ["No se pudo analizar el sesgo institucional"]
        },
        "summary": "No se pudo realizar el análisis de sesgo para este texto."
    }
    
    result = {"result": default_result}
    
    while retorno == False and intentos < max_intentos:
        intentos += 1
        # 🚀 Call OpenAI through the centralized helper
        result = call_openai_with_tool(prompt, narrative_bias_schema, "score_bias")
        
        if result and "error" not in result and "result" in result:
            retorno = True
        elif "error" in result:
            print(f"[Celery Task] Error en intento {intentos}/{max_intentos} para submission {noticia_id}: {result['error']}")
            # Asignar valores predeterminados cuando hay error
            result["result"] = default_result.copy()
            if intentos >= max_intentos:
                print(f"[Celery Task] Se alcanzó el máximo de intentos ({max_intentos}) para submission {noticia_id}")
                return
        else:
            print(f"[Celery Task] Respuesta inesperada en intento {intentos}/{max_intentos} para submission {noticia_id}")
            # Asignar valores predeterminados cuando hay respuesta inesperada
            result["result"] = default_result.copy()
    
    # Si llegamos aquí sin retorno válido después de todos los intentos
    if not retorno:
        print(f"[Celery Task] No se pudo obtener un resultado válido para submission {noticia_id} después de {max_intentos} intentos")
        return

    data = {
        "id": noticia_id,
        "sesgo": result["result"],  # Use result["result"] to get the parsed arguments
    }
    
    Noticia.update_sesgo(data)
