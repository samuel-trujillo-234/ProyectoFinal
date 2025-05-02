## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely


from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario_model import Usuario
from flask_app.utils.decoradores import login_required
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 


@app.route('/iniciar_sessao', methods=['POST'])
def login_usuario():
    usuario = Usuario.get_by_email(request.form['email'])
    if not usuario:
        flash("Correo electrónico y/o contraseña incorrectos.", "error")
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Correo electrónico y/o contraseña incorrectos.", "error")
        return redirect("/")
    flash("Estás logueado en el sistema.", "success")
    session['email'] = usuario.email
    session['id'] = usuario.id
    session['nombre'] = usuario.nombre
    session['apellido'] = usuario.apellido
    session['categoria'] = usuario.categoria
    return redirect("/")

@app.route('/close_session')
def close_session():
    if 'email' in session:
        session.clear()
        flash("Fuiste desconectado del sistema.", "info")
    return redirect ('/')