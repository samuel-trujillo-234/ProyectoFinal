## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask import Flask
import os
from dotenv import load_dotenv
from flask_app.utils.context_processors import inject_user_data

load_dotenv()

app = Flask(__name__)

# Carga la llave secreta del archivo de contexto --> .env
app.secret_key = os.getenv("SECRET_KEY")

# Registrar procesador de contexto desde utils
app.context_processor(inject_user_data)