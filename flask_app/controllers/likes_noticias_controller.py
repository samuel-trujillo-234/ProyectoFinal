## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely


from flask import Blueprint
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from flask_app.models.like_noticia_model import VotoNoticia
from datetime import date
from flask_app.utils.decoradores import login_required


likes_noticias = Blueprint('likes_noticias', __name__)

@likes_noticias.route("/upvote/<int:noticia_id>", methods=['POST'])
@login_required
def upvote_noticia(noticia_id):
    usuario_id = session['id']
    
    # Check if the user has already voted on this news
    if not VotoNoticia.check_vote(noticia_id, usuario_id):
        # If they already voted, delete the previous vote
        VotoNoticia.delete_vote(noticia_id, usuario_id)
    
    # Save the new upvote
    VotoNoticia.save_vote(noticia_id, usuario_id, upvote=True)
    
    # Get the updated counts
    upvotes = VotoNoticia.count_upvotes(noticia_id)
    downvotes = VotoNoticia.count_downvotes(noticia_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@likes_noticias.route("/downvote/<int:noticia_id>", methods=['POST'])
@login_required
def downvote_noticia(noticia_id):
    usuario_id = session['id']
    
    # Check if the user has already voted on this news
    if not VotoNoticia.check_vote(noticia_id, usuario_id):
        # If they already voted, delete the previous vote
        VotoNoticia.delete_vote(noticia_id, usuario_id)
    
    # Save the new downvote
    VotoNoticia.save_vote(noticia_id, usuario_id, downvote=True)
    
    # Get the updated counts
    upvotes = VotoNoticia.count_upvotes(noticia_id)
    downvotes = VotoNoticia.count_downvotes(noticia_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@likes_noticias.route("/delete_vote/<int:noticia_id>", methods=['POST'])
@login_required
def delete_vote(noticia_id):
    usuario_id = session['id']
    
    # Delete the vote
    VotoNoticia.delete_vote(noticia_id, usuario_id)
    
    # Get the updated counts
    upvotes = VotoNoticia.count_upvotes(noticia_id)
    downvotes = VotoNoticia.count_downvotes(noticia_id)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, upvotes=upvotes, downvotes=downvotes)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")

