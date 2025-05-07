## Coding Dojo - Python Bootcamp Jan 2025
## Roberto Alvarez, 2025

from flask_app.config.celery_worker import celery
from flask_app.utils.openai_helper import call_openai_with_tool
from flask_app.models.noticia_model import Noticia

@celery.task
def avaliar_texto_task(noticia_id, texto, usuario_id):
    """
    Celery background task to evaluate if a news text is factual or opinion-based.
    Updates the 'noticia' entry with the score and explanation.
    """

    # 🧠 Tool/function schema to classify text
    fact_vs_opinion_schema = [
        {
            "type": "function",
            "function": {
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
        }
    ]

    # 🧾 Prompt
    prompt = f"""
You are an assistant that classifies texts as either factual reports or opinion pieces.

Evaluate the text below and assign a score:
- Use +1 if the text is clearly and fully a factual, data-based news article.
- Use -1 if the text is fully an opinion or commentary.
- Use values in between -1 and 1 accordingly.

Also return a short explanation of your reasoning.

Text:
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

    # 🗃️ Build and update the Noticia object
    noticia_obj = Noticia({
        "id": noticia_id,
        "news": texto,
        "type": assessment["score"],
        "explanation": assessment["explanation"],
        "created_at": None,
        "updated_at": None,
        "usuario_id": usuario_id
    })

    Noticia.update(noticia_obj)
