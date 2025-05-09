## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask_app.config.celery_worker import celery
from flask_app.utils.openai_helper import call_openai_with_tool
from flask_app.models.noticia_model import Noticia

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

    # 🚀 Call OpenAI through the centralized helper
    result = call_openai_with_tool(prompt, fact_vs_opinion_schema, "assess_fact_opinion")

    if "error" in result:
        print(f"[Celery Task] Error processing submission {noticia_id}: {result['error']}")
        return

    assessment = result["result"]

    data = {
        "id": noticia_id,
        "tipo": assessment["score"],
        "analisis": assessment["explanation"]
    }
    
    Noticia.update_tipo(data)
