## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely - Administrador Controller


from flask import Blueprint, render_template, redirect, request, session, flash, jsonify
from flask_app.models.usuario_model import Usuario
from flask_app.utils.decoradores import login_required

administrador = Blueprint('administrador', __name__)

# Function para verificar se es administrador
# Retorna True if admin, False otherwise

def verificar_admin():
    if 'categoria' not in session or session['categoria'] != 'admin':
        flash("Acceso restringido. Debes ser administrador para acceder a esta página.", "error")
        return False
    return True


@administrador.route('/administrar_usuarios')
@login_required
def admin_usuarios():
    if not verificar_admin():
        return redirect('/')
    usuarios = Usuario.get_all()
    return render_template('administracion_usuarios.html', usuarios=usuarios, usuario=session['nombre'], id_usuario=session['id'])


@administrador.route('/update_user_categoria', methods=['POST'])
@login_required
def update_user_categoria():
    if not verificar_admin():
        return redirect('/')
    user_id = request.form.get('user_id')
    categoria = request.form.get('categoria')
    Usuario.update_categoria(user_id, categoria)
    flash("Categoría actualizada correctamente.", "success")    
    return redirect('/administrar_usuarios')


@administrador.route('/delete_user', methods=['POST'])
@login_required
def delete_user():
    if not verificar_admin():
        return redirect('/')
    user_id = request.form.get('user_id')
    Usuario.delete(user_id)
    flash("Usuario eliminado correctamente.", "success")
    return redirect('/administrar_usuarios')