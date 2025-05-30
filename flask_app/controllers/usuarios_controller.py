## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask import Blueprint
from flask import render_template, request, redirect, session, flash
from flask_app.models.usuario_model import Usuario
from flask_app.models.noticia_model import Noticia
from flask_app.utils.decoradores import login_required
from datetime import date
from flask_app.extensions import bcrypt
import os

usuarios = Blueprint('usuarios', __name__)

today = date.today()

@usuarios.route('/')
def home():
    noticia = Noticia.get_latest()
    return render_template('home.html', noticia=noticia)


@usuarios.route('/registrar_usuario', methods=['POST'])
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


@usuarios.route('/actualizar_perfil', methods=['POST'])
@login_required
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


@usuarios.route('/cambiar_password', methods=['POST'])
@login_required
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


@usuarios.route('/actualizar_notificaciones', methods=['POST'])
@login_required
def actualizar_notificaciones():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para guardar las preferencias de notificaciones
    flash("Preferencias de notificaciones actualizadas", "success")
    return redirect('/settings')


@usuarios.route('/actualizar_privacidad', methods=['POST'])
@login_required
def actualizar_privacidad():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para guardar las configuraciones de privacidad
    flash("Configuración de privacidad actualizada", "success")
    return redirect('/settings')


@usuarios.route('/actualizar_tema', methods=['POST'])
@login_required
def actualizar_tema():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para guardar las preferencias de tema
    flash("Preferencias de tema actualizadas", "success")
    return redirect('/settings')


@usuarios.route('/desactivar_cuenta', methods=['POST'])
@login_required
def desactivar_cuenta():
    if 'id' not in session:
        return redirect('/')
    # Aquí se implementaría la lógica para desactivar la cuenta
    flash("Cuenta desactivada exitosamente", "success")
    session.clear()
    return redirect('/')


@usuarios.route('/eliminar_cuenta', methods=['POST'])
@login_required
def eliminar_cuenta():
    if 'id' not in session:
        return redirect('/')
    if Usuario.delete(session['id']):
        flash("Cuenta eliminada exitosamente", "info")
        session.clear()
    else:
        flash("Error al eliminar la cuenta", "error")
    return redirect('/')


@usuarios.route('/settings')
@login_required
def settings():
    return render_template('settings.html')