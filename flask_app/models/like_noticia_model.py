## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class VotoNoticia:

    def __init__(self, data):
        self.id = data['id']
        self.upvote = data['upvote']
        self.downvote = data['downvote']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.noticia_id = data['noticia_id']
        self.usuario_id = data['usuario_id']

    @classmethod
    def count_upvotes(cls, noticia_id):
        query = "SELECT COUNT(*) AS upvotes FROM votos_noticia WHERE noticia_id = %(noticia_id)s AND upvote = 1;"
        data = {"noticia_id": noticia_id}
        result = connectToMySQL().query_db(query, data)
        return result[0]['upvotes'] if result else 0

    @classmethod
    def count_downvotes(cls, noticia_id):
        query = "SELECT COUNT(*) AS downvotes FROM votos_noticia WHERE noticia_id = %(noticia_id)s AND downvote = 1;"
        data = {"noticia_id": noticia_id}
        result = connectToMySQL().query_db(query, data)
        return result[0]['downvotes'] if result else 0

    @classmethod
    def check_vote(cls, noticia_id, usuario_id):
        # Returns True if user has NOT voted yet, False otherwise
        query = "SELECT * FROM votos_noticia WHERE noticia_id = %(noticia_id)s AND usuario_id = %(usuario_id)s;"
        data = {"noticia_id": noticia_id, "usuario_id": usuario_id}
        result = connectToMySQL().query_db(query, data)
        return len(result) == 0

    @classmethod
    def save_vote(cls, noticia_id, usuario_id, upvote=False, downvote=False):
        query = """
            INSERT INTO votos_noticia (noticia_id, usuario_id, upvote, downvote, created_at, updated_at)
            VALUES (%(noticia_id)s, %(usuario_id)s, %(upvote)s, %(downvote)s, NOW(), NOW());
        """
        data = {
            "noticia_id": noticia_id,
            "usuario_id": usuario_id,
            "upvote": 1 if upvote else 0,
            "downvote": 1 if downvote else 0
        }
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_vote(cls, noticia_id, usuario_id):
        query = "DELETE FROM votos_noticia WHERE noticia_id = %(noticia_id)s AND usuario_id = %(usuario_id)s;"
        data = {"noticia_id": noticia_id, "usuario_id": usuario_id}
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_votes_noticia(cls, noticia_id):
        query = "DELETE FROM votos_noticia WHERE noticia_id = %(noticia_id)s;"
        data = {"noticia_id": noticia_id}
        return connectToMySQL().query_db(query, data)
