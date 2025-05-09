## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask import Flask
import os
from dotenv import load_dotenv

from flask_app.utils.context_processors import inject_user_data
from flask_app.controllers import register_controllers
from flask_app.extensions import bcrypt, init_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

load_dotenv()

def create_app():
    app = Flask(__name__)

    # 🔐 App configuration
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ⚙️ Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)

    # 🧩 Import and register Blueprints
    from flask_app.controllers import (
        administrador_controller,
        autentication_controller,
        comentarios_controller,
        favoritos_controller,
        likes_comentarios_controller,
        likes_noticias_controller,
        noticias_controller,
        report_comentarios_controller,
        report_noticias_controller,
        usuarios_controller
    )

    app.register_blueprint(administrador_controller.administrador)
    app.register_blueprint(autentication_controller.autentication)
    app.register_blueprint(comentarios_controller.comentarios)
    app.register_blueprint(favoritos_controller.favoritos)
    app.register_blueprint(likes_comentarios_controller.likes_comentarios)
    app.register_blueprint(likes_noticias_controller.likes_noticias)
    app.register_blueprint(noticias_controller.noticias)
    app.register_blueprint(report_comentarios_controller.report_comentarios)
    app.register_blueprint(report_noticias_controller.report_noticias)
    app.register_blueprint(usuarios_controller.usuarios)

    app.secret_key = os.getenv("SECRET_KEY")
    app.context_processor(inject_user_data)

    # 🛠️ Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app

# 🌐 Entry point for WSGI server or Celery
app = create_app()
