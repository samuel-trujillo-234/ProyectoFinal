## Coding Dojo - Python Bootcamp Jan 2025
## Proyecto final
## Wavely

from flask import Blueprint
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from datetime import date
from flask_app.utils.decoradores import login_required

favoritos = Blueprint('favoritos', __name__)

@favoritos.route("/favoritar_noticia/<int:noticia_id>", methods=['POST'])
@login_required
def favoritar_noticia(noticia_id):
    """
    Endpoint to add a news article to user's favorites
    """
    if 'id' not in session:
        return jsonify({'success': False, 'message': 'Usuario no autenticado'}), 401
    
    usuario_id = session['id']
    data = {
        'usuario_id': usuario_id,
        'noticia_id': noticia_id
    }
    
    # Check if the favorite already exists
    existing_favorite = Favorito.get_by_usuario_and_noticia(data)
    if existing_favorite:
        return jsonify({'success': False, 'message': 'Ya está en favoritos'}), 400
    
    # Create the favorite
    Favorito.save(data)
    
    # Get the updated count
    count = Favorito.count_by_noticia({'noticia_id': noticia_id})
    
    return jsonify({'success': True, 'count': count})

@favoritos.route("/cancelar_favorito/<int:noticia_id>", methods=['POST'])
@login_required
def cancelar_favorito(noticia_id):
    """
    Endpoint to remove a news article from user's favorites
    """
    if 'id' not in session:
        return jsonify({'success': False, 'message': 'Usuario no autenticado'}), 401
    
    usuario_id = session['id']
    data = {
        'usuario_id': usuario_id,
        'noticia_id': noticia_id
    }
    
    # Delete the favorite
    Favorito.delete_by_usuario_and_noticia(data)
    
    # Get the updated count
    count = Favorito.count_by_noticia({'noticia_id': noticia_id})
    
    return jsonify({'success': True, 'count': count})