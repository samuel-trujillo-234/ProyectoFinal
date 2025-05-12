## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask import flash
from flask_app.config.celery_worker import celery
from flask_app.utils.openai_helper import call_openai_with_tool
from flask_app.models.noticia_model import Noticia
import sys
import logging

# Configure logging for this module
logger = logging.getLogger(__name__)

@celery.task
def analisis_noticia_task(noticia_id, texto, usuario_id):
    """
    Tarea en segundo plano de Celery para evaluar si un texto de noticia es factual u opinión.
    Actualiza la entrada 'noticia' con la puntuación y explicación.
    """

    # Esquema de función para OpenAI API v0.28.1 (formato antiguo)
    fact_vs_opinion_schema = [
        {
            "name": "assess_fact_opinion",
            "description": "Evaluate whether the text is a factual news report or an opinion piece.",
            "parameters": {
                "type": "object",
                "properties": {
                    "score": {
                        "type": "integer",
                        "description": "-1 for opinion piece, +1 for factual article"
                    },
                    "explanation": {
                        "type": "string",
                        "description": "Brief explanation of why the text was classified this way"
                    }
                },
                "required": ["score", "explanation"]
            }
        }
    ]

    # 🧾 Prompt
    prompt = f"""
Eres un asistente que clasifica textos como reportes objetivos o artículos de opinión.

Evalúa el texto a continuación y asigna una puntuación:
- Usa +1 si el texto es claramente y completamente un artículo de noticias objetivo, basado en datos.
- Usa -1 si el texto es completamente una opinión o comentario.
- Usa valores entre -1 y 1 según corresponda.

También proporciona una breve explicación de tu razonamiento.

IMPORTANTE: Tu respuesta DEBE ser en español. Proporciona la explicación completamente en español.

Texto:
\"\"\"
{texto}
\"\"\"
"""

    retorno = False
    max_intentos = 3
    intentos = 0
    case = 0
    
    # Inicializar result con un valor predeterminado
    default_result = {
        "score": 0, 
        "explanation": "No se pudo analizar el texto"
    }
    
    result = {"result": default_result}

    # Force stdout flush to ensure prints are displayed immediately
    sys.stdout.flush()

    while retorno == False and intentos < max_intentos:
        intentos += 1
        result = call_openai_with_tool(prompt, fact_vs_opinion_schema, "assess_fact_opinion")
        if result and "error" not in result and "result" in result:
            retorno = True
            case = 1
        elif "error" in result:
            logger.error(f"[Celery Task] Error en intento {intentos}/{max_intentos} para submission {noticia_id}: {result['error']}")
            result["result"] = default_result.copy()
            result["result"]["explanation"] = f"Error en análisis: {result.get('error', 'Error desconocido')}"
            case = 2
        else:            
            logger.error(f"[Celery Task] Respuesta inesperada en intento {intentos}/{max_intentos} para submission {noticia_id}")
            result["result"] = default_result.copy()
            result["result"]["explanation"] = "Respuesta inesperada del servicio de análisis"
            case = 3
        if intentos >= max_intentos and not retorno:
            case = 4
            return
    
    if not retorno:
        case = 5
        return

    assessment = result["result"]

    data = {
        "id": noticia_id,
        "tipo": assessment["score"],
        "analisis": assessment["explanation"],
        "revisada": case
    }
    
    Noticia.update_tipo(data)
