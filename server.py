## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely


from flask import Flask, render_template
from flask_app import app

from flask_app.controllers import usuarios_controller
from flask_app.controllers import autentication_controller
from flask_app.controllers import administrador_controller
from flask_app.controllers import noticias_controller
from flask_app.controllers import comentarios_controller

if __name__ == '__main__':
    app.run(debug=True)