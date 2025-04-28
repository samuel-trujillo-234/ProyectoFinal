## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class VotoComentario:

    def __init__(self, data):
        self.id = data['id']
        self.upvote = data['upvote']
        self.downvote = data['downvote']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.comentario_id = data['comentario_id']
        self.usuario_id = data['usuario_id']

    @classmethod
    def count_upvotes(cls, comentario_id):
        query = "SELECT COUNT(*) AS upvotes FROM comentarios WHERE comentario_id = %(comentario_id)s AND upvote = 1;"
        data = {"comentario_id": comentario_id}
        result = connectToMySQL().query_db(query, data)
        return result[0]['upvotes'] if result else 0

    @classmethod
    def count_downvotes(cls, comentario_id):
        query = "SELECT COUNT(*) AS downvotes FROM comentarios WHERE comentario_id = %(comentario_id)s AND downvote = 1;"
        data = {"comentario_id": comentario_id}
        result = connectToMySQL().query_db(query, data)
        return result[0]['downvotes'] if result else 0

    @classmethod
    def check_vote(cls, comentario_id, usuario_id):
        # Returns True if user has NOT voted yet, False otherwise
        query = "SELECT * FROM comentarios WHERE comentario_id = %(comentario_id)s AND usuario_id = %(usuario_id)s;"
        data = {"comentario_id": comentario_id, "usuario_id": usuario_id}
        result = connectToMySQL().query_db(query, data)
        return len(result) == 0

    @classmethod
    def save_vote(cls, comentario_id, usuario_id, upvote=False, downvote=False):
        query = """
            INSERT INTO comentarios (comentario_id, usuario_id, upvote, downvote, created_at, updated_at)
            VALUES (%(comentario_id)s, %(usuario_id)s, %(upvote)s, %(downvote)s, NOW(), NOW());
        """
        data = {
            "comentario_id": comentario_id,
            "usuario_id": usuario_id,
            "upvote": 1 if upvote else 0,
            "downvote": 1 if downvote else 0
        }
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_vote(cls, comentario_id, usuario_id):
        query = "DELETE FROM comentarios WHERE comentario_id = %(comentario_id)s AND usuario_id = %(usuario_id)s;"
        data = {"comentario_id": comentario_id, "usuario_id": usuario_id}
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_votes_comentario(cls, comentario_id):
        query = "DELETE FROM comentarios WHERE comentario_id = %(comentario_id)s;"
        data = {"comentario_id": comentario_id}
        return connectToMySQL().query_db(query, data)
