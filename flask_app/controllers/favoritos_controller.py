## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app import app
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from datetime import date
from flask_app.utils.decoradores import login_required


@app.route("/crear_favorito/<int:noticia_id>", methods=['POST'])
@login_required
def crear_favorito(noticia_id):
    usuario_id = session['id']
    Favorito.save(usuario_id, noticia_id)
    # Get the updated count
    favoritos_count = Favorito.get_count_by_noticia(noticia_id)
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, count=favoritos_count)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@app.route("/eliminar_favorito/<int:noticia_id>", methods=['POST'])
@login_required
def eliminar_favorito(noticia_id):
    usuario_id = session['id']
    Favorito.delete(usuario_id, noticia_id)
    # Get the updated count
    favoritos_count = Favorito.get_count_by_noticia(noticia_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, count=favoritos_count)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")

