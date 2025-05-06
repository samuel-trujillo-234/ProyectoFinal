## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from datetime import date

today = date.today()

class ReportNoticia:

    def __init__(self, data):
        self.usuario_id = data['usuario_id']
        self.noticia_id = data['noticia_id']


    @classmethod
    def save(cls, usuario_id, noticia_id):
        if cls.check_if_reported(usuario_id, noticia_id):
            return True
        query = """
            INSERT INTO reports_noticias (usuario_id, noticia_id)
            VALUES (%(usuario_id)s, %(noticia_id)s);
        """
        data = {
            "usuario_id": usuario_id,
            "noticia_id": noticia_id
        }
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete(cls, usuario_id, noticia_id):
        query = "DELETE FROM reports_noticias WHERE usuario_id = %(usuario_id)s AND noticia_id = %(noticia_id)s;"
        data = {
            "usuario_id": usuario_id,
            "noticia_id": noticia_id
        }
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_por_noticia(cls, noticia_id):
        query = "DELETE FROM reports_noticias WHERE noticia_id = %(noticia_id)s;"
        data = {"noticia_id": noticia_id}
        return connectToMySQL().query_db(query, data)
    
    @classmethod
    def get_count_by_noticia(cls, noticia_id):
        query = "SELECT COUNT(*) as count FROM reports_noticias WHERE noticia_id = %(noticia_id)s;"
        data = {"noticia_id": noticia_id}
        result = connectToMySQL().query_db(query, data)
        if result:
            return result[0]['count']
        return 0
    
    @classmethod
    def check_if_reported(cls, usuario_id, noticia_id):
        query = "SELECT * FROM reports_noticias WHERE usuario_id = %(usuario_id)s AND noticia_id = %(noticia_id)s;"
        data = {
            "usuario_id": usuario_id,
            "noticia_id": noticia_id
        }
        result = connectToMySQL().query_db(query, data)
        if result:
            return True
        return False
    
    