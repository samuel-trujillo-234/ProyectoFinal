## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask_app import app
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from flask_app.models.like_noticia_model import VotoNoticia
from flask_app.models.like_comentario_model import VotoComentario
from datetime import date
from flask_app.utils.decoradores import login_required


# Rutas de Votos para Noticias
@app.route("/upvote/<int:noticia_id>", methods=['POST'])
@login_required
def upvote_noticia(noticia_id):
    usuario_id = session['id']
    
    # Verificar si el usuario ya ha votado en esta noticia
    if not VotoNoticia.check_vote(noticia_id, usuario_id):
        # Si ya votaron, eliminar el voto anterior
        VotoNoticia.delete_vote(noticia_id, usuario_id)
    
    # Guardar el nuevo voto positivo
    VotoNoticia.save_vote(noticia_id, usuario_id, upvote=True)
    
    # Obtener los conteos actualizados
    upvotes = VotoNoticia.count_upvotes(noticia_id)
    downvotes = VotoNoticia.count_downvotes(noticia_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@app.route("/downvote/<int:noticia_id>", methods=['POST'])
@login_required
def downvote_noticia(noticia_id):
    usuario_id = session['id']
    
    # Verificar si el usuario ya ha votado en esta noticia
    if not VotoNoticia.check_vote(noticia_id, usuario_id):
        # Si ya votaron, eliminar el voto anterior
        VotoNoticia.delete_vote(noticia_id, usuario_id)
    
    # Guardar el nuevo voto negativo
    VotoNoticia.save_vote(noticia_id, usuario_id, downvote=True)
    
    # Obtener los conteos actualizados
    upvotes = VotoNoticia.count_upvotes(noticia_id)
    downvotes = VotoNoticia.count_downvotes(noticia_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@app.route("/delete_vote/<int:noticia_id>", methods=['POST'])
@login_required
def delete_vote(noticia_id):
    usuario_id = session['id']
    
    # Eliminar el voto
    VotoNoticia.delete_vote(noticia_id, usuario_id)
    
    # Obtener los conteos actualizados
    upvotes = VotoNoticia.count_upvotes(noticia_id)
    downvotes = VotoNoticia.count_downvotes(noticia_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


# Rutas de Votos para Comentarios
@app.route("/upvote_comentario/<int:comentario_id>", methods=['POST'])
@login_required
def upvote_comentario(comentario_id):
    usuario_id = session['id']
    
    # Verificar si el usuario ya ha votado en este comentario
    if not VotoComentario.check_vote(comentario_id, usuario_id):
        # Si ya votaron, eliminar el voto anterior
        VotoComentario.delete_vote(comentario_id, usuario_id)
    
    # Guardar el nuevo voto positivo
    VotoComentario.save_vote(comentario_id, usuario_id, upvote=True)
    
    # Obtener los conteos actualizados
    upvotes = VotoComentario.count_upvotes(comentario_id)
    downvotes = VotoComentario.count_downvotes(comentario_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    
    # Obtener el noticia_id para redireccionar (asumiendo que lo tenemos en la solicitud)
    noticia_id = request.form.get('noticia_id', 0)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@app.route("/downvote_comentario/<int:comentario_id>", methods=['POST'])
@login_required
def downvote_comentario(comentario_id):
    usuario_id = session['id']
    
    # Verificar si el usuario ya ha votado en este comentario
    if not VotoComentario.check_vote(comentario_id, usuario_id):
        # Si ya votaron, eliminar el voto anterior
        VotoComentario.delete_vote(comentario_id, usuario_id)
    
    # Guardar el nuevo voto negativo
    VotoComentario.save_vote(comentario_id, usuario_id, downvote=True)
    
    # Obtener los conteos actualizados
    upvotes = VotoComentario.count_upvotes(comentario_id)
    downvotes = VotoComentario.count_downvotes(comentario_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    
    # Obtener el noticia_id para redireccionar (asumiendo que lo tenemos en la solicitud)
    noticia_id = request.form.get('noticia_id', 0)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@app.route("/delete_vote_comentario/<int:comentario_id>", methods=['POST'])
@login_required
def delete_vote_comentario(comentario_id):
    usuario_id = session['id']
    
    # Eliminar el voto
    VotoComentario.delete_vote(comentario_id, usuario_id)
    
    # Obtener los conteos actualizados
    upvotes = VotoComentario.count_upvotes(comentario_id)
    downvotes = VotoComentario.count_downvotes(comentario_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    
    # Obtener el noticia_id para redireccionar (asumiendo que lo tenemos en la solicitud)
    noticia_id = request.form.get('noticia_id', 0)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")

