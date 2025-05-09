## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely
 
from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

def make_celery(app_name=__name__):
    celery = Celery(
        app_name,
        broker=os.getenv("CELERY_BROKER_URL"),
        backend=os.getenv("CELERY_BACKEND_URL", "redis://localhost:6379/0"),
        include=[
            "flask_app.tasks.analisis_noticia",
            "flask_app.tasks.analisis_sesgo"
        ]
    )
    celery.autodiscover_tasks(['flask_app.tasks'])
    return celery

celery = make_celery()
