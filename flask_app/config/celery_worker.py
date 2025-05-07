from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

def make_celery(app_name=__name__):
    return Celery(
        app_name,
        broker=os.getenv("CELERY_BROKER_URL"),
        backend=os.getenv("CELERY_BACKEND_URL", "redis://localhost:6379/0"),
        include=[
            "flask_app.tasks.analisis_noticia",
            #"flask_app.tasks.extracao_task",
            #"flask_app.tasks.noticias_task",
            #"flask_app.tasks.sesgo_fatos_narrados_task",
            #"flask_app.tasks.sesgo_narrativa_task"
        ]
    )

celery = make_celery()
