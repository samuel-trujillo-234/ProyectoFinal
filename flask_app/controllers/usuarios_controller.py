## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely


from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.usuario_model import Usuario
from datetime import date
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
today = date.today()



@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirmacion_password': request.form['confirmacion_password'],
        'categoria': "user"
        }
    if Usuario.validar_usuario(data) == True:
        data.pop('confirmacion_password', None)
        password_hash = bcrypt.generate_password_hash(request.form['password'])
        data['password'] = password_hash
        Usuario.save(data)
        flash("Usuario registrado con éxito..", "success")
    return redirect("/")


@app.route('/logar_usuario')
def logar_usuario():
    return render_template("/home.html", usuario=session['nombre'])

