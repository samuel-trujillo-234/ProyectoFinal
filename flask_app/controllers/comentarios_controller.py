## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app import app
from flask import render_template, request, redirect, session, flash, url_for
from flask_app.models.usuario_model import Usuario
from flask_app.models.noticia_model import Noticia
from flask_app.models.comentario_model import Comentario
from datetime import date
from flask_bcrypt import Bcrypt
from flask_app.utils.decoradores import login_required

bcrypt = Bcrypt(app)
today = date.today()


@app.route("/crear_comentario", methods=['POST'])
@login_required
def crear_comentario():
    data = {
        'comentario': request.form['comentario'],
        'usuario_id': session['id'],
        'noticia_id': request.form['noticia_id'],
        }
    
    # Validate the comment before saving
    if not Comentario.validar_comentario(data, None):
        return redirect(f"/noticia/{request.form['noticia_id']}")
        
    Comentario.save(data)
    return redirect(f"/noticia/{request.form['noticia_id']}")


@app.route("/eliminar_comentario/<int:noticia_id>/<int:id>")
@login_required
def deletar_comentario(noticia_id, id):
    Comentario.delete(id)
    return redirect(f"/noticia/{noticia_id}")


@app.route("/editar_comentario/<int:id>")
@login_required
def editar_comentario(id):
    comentario = Comentario.get_one(id)
    return render_template("editar_comentario.html", comentario=comentario)


@app.route("/atualizar_comentario", methods=['POST'])
@login_required
def atualizar_comentario():
    data = {
        'id': request.form['id'],
        'comentario': request.form['comentario']
    }
    
    # Validate the comment before updating
    if not Comentario.validar_comentario(data, request.form['id']):
        return redirect(f"/editar_comentario/{request.form['id']}")
    
    Comentario.update(data)
    return redirect(f"/noticia/{request.form['noticia_id']}")