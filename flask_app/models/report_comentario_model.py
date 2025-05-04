## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from datetime import date


class ReportComentario:

    def __init__(self, data):
        self.usuario_id = data['usuario_id']
        self.comentario_id = data['comentario_id']


    @classmethod
    def save(cls, usuario_id, comentario_id):
        if cls.check_if_reported(usuario_id, comentario_id):
            return True
        query = """
            INSERT INTO reports_comentarios (usuario_id, comentario_id)
            VALUES (%(usuario_id)s, %(comentario_id)s);
        """
        data = {
            "usuario_id": usuario_id,
            "comentario_id": comentario_id
        }
        return connectToMySQL().query_db(query, data)


    @classmethod
    def delete(cls, usuario_id, comentario_id):
        query = "DELETE FROM reports_comentarios WHERE usuario_id = %(usuario_id)s AND comentario_id = %(comentario_id)s;"
        data = {
            "usuario_id": usuario_id,
            "comentario_id": comentario_id
        }
        return connectToMySQL().query_db(query, data)


    @classmethod
    def delete_all_for_comentario(cls, comentario_id):
        query = "DELETE FROM reports_comentarios WHERE comentario_id = %(comentario_id)s;"
        data = {"comentario_id": comentario_id}
        return connectToMySQL().query_db(query, data)
    

    @classmethod
    def get_count_by_comentario(cls, comentario_id):
        query = "SELECT COUNT(*) as count FROM reports_comentarios WHERE comentario_id = %(comentario_id)s;"
        data = {"comentario_id": comentario_id}
        result = connectToMySQL().query_db(query, data)
        if result:
            return result[0]['count']
        return 0
    
    @classmethod
    def check_if_reported(cls, usuario_id, comentario_id):
        query = "SELECT * FROM reports_comentarios WHERE usuario_id = %(usuario_id)s AND comentario_id = %(comentario_id)s;"
        data = {
            "usuario_id": usuario_id,
            "comentario_id": comentario_id
        }
        result = connectToMySQL().query_db(query, data)
        if result:
            return True
        return False

