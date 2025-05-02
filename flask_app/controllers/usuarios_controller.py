## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely


from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.usuario_model import Usuario
from flask_app.utils.decoradores import login_required
from datetime import date
from flask_bcrypt import Bcrypt
import os

bcrypt = Bcrypt(app)
today = date.today()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    lista_admin = os.getenv("ADMINS")
    if request.form['email'] in lista_admin:
        tipo_usuario = 'admin'
    else:
        tipo_usuario = 'user'
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirmacion_password': request.form['confirmacion_password'],
        'categoria': tipo_usuario
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
    if 'nombre' not in session or 'categoria' not in session:
        return redirect('/')
    return render_template("/home.html", usuario=session['nombre'], role=session['categoria'])


@app.route('/actualizar_perfil', methods=['POST'])
def actualizar_perfil():
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': session['id'],
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': session['password'] if 'password' in session else None,
        'categoria': session['categoria']
    }
    if Usuario.update(data):
        session['nombre'] = request.form['nombre']
        session['apellido'] = request.form['apellido']
        session['email'] = request.form['email']
        flash("Perfil actualizado exitosamente", "success")
    else:
        flash("Error al actualizar el perfil", "error")
    return redirect('/settings')


@app.route('/cambiar_password', methods=['POST'])
def cambiar_password():
    if 'id' not in session:
        return redirect('/')
    usuario = Usuario.get_one(session['id'])
    if not bcrypt.check_password_hash(usuario.password, request.form['password_actual']):
        flash("La contraseña actual es incorrecta", "error")
        return redirect('/settings')
    if request.form['password_nueva'] != request.form['confirmacion_password']:
        flash("Las contraseñas nuevas no coinciden", "error")
        return redirect('/settings')
    password_hash = bcrypt.generate_password_hash(request.form['password_nueva'])
    data = {
        'id': session['id'],
        'nombre': usuario.nombre,
        'apellido': usuario.apellido,
        'email': usuario.email,
        'password': password_hash,
        'categoria': usuario.categoria
    }
    if Usuario.update(data):
        flash("Contraseña actualizada exitosamente", "success")
    else:
        flash("Error al actualizar la contraseña", "error")
    return redirect('/settings')


@app.route('/actualizar_notificaciones', methods=['POST'])
def actualizar_notificaciones():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para guardar las preferencias de notificaciones
    flash("Preferencias de notificaciones actualizadas", "success")
    return redirect('/settings')


@app.route('/actualizar_privacidad', methods=['POST'])
def actualizar_privacidad():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para guardar las configuraciones de privacidad
    flash("Configuración de privacidad actualizada", "success")
    return redirect('/settings')


@app.route('/actualizar_tema', methods=['POST'])
def actualizar_tema():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para guardar las preferencias de tema
    flash("Preferencias de tema actualizadas", "success")
    return redirect('/settings')


@app.route('/desactivar_cuenta', methods=['POST'])
def desactivar_cuenta():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para desactivar la cuenta
    flash("Cuenta desactivada exitosamente", "success")
    session.clear()
    return redirect('/')


@app.route('/eliminar_cuenta', methods=['POST'])
def eliminar_cuenta():
    if 'id' not in session:
        return redirect('/')
    if Usuario.delete(session['id']):
        flash("Cuenta eliminada exitosamente", "info")
        session.clear()
    else:
        flash("Error al eliminar la cuenta", "error")
    return redirect('/')

