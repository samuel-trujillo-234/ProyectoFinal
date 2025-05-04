## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from datetime import date
from datetime import datetime
from flask_app.models.usuario_model import Usuario
from flask_app.models.noticia_model import Noticia

today = date.today()

class ReportNoticia:

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.noticia_id = data['noticia_id']

    @classmethod
    def get_all(cls):
        query = """
        SELECT reports_noticias.id AS id,
               reports_noticias.created_at AS created_at, reports_noticias.updated_at AS updated_at,
               reports_noticias.usuario_id AS usuario_id, reports_noticias.noticia_id AS noticia_id,
               usuarios.nome AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM reports_noticias
        LEFT JOIN usuarios ON reports_noticias.usuario_id = usuarios.id
        LEFT JOIN noticias ON reports_noticias.noticia_id = noticias.id;
        """
        results = connectToMySQL().query_db(query)
        reports = []
        for report in results:
            reports.append(cls(report))
        return reports

    @classmethod
    def get_one(cls, id):
        query = """
        SELECT reports_noticias.id AS id,
               reports_noticias.created_at AS created_at, reports_noticias.updated_at AS updated_at,
               reports_noticias.usuario_id AS usuario_id, reports_noticias.noticia_id AS noticia_id,
               usuarios.nome AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM reports_noticias
        LEFT JOIN usuarios ON reports_noticias.usuario_id = usuarios.id
        LEFT JOIN noticias ON reports_noticias.noticia_id = noticias.id
        WHERE reports_noticias.id = %(id)s;
        """
        data = {"id": id}
        result = connectToMySQL().query_db(query, data)
        return cls(result[0]) if result else None

    @classmethod
    def get_count_by_noticia(cls, noticia_id):
        query = "SELECT COUNT(*) as count FROM reports_noticias WHERE noticia_id = %(noticia_id)s;"
        data = {"noticia_id": noticia_id}
        result = connectToMySQL().query_db(query, data)
        return result[0]['count'] if result else 0

    @classmethod
    def get_by_usuario_and_noticia(cls, usuario_id, noticia_id):
        query = """
        SELECT * FROM reports_noticias
        WHERE usuario_id = %(usuario_id)s AND noticia_id = %(noticia_id)s;
        """
        data = {
            "usuario_id": usuario_id,
            "noticia_id": noticia_id
        }
        result = connectToMySQL().query_db(query, data)
        return cls(result[0]) if result else None

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO reports_noticias (created_at, updated_at, usuario_id, noticia_id)
        VALUES (NOW(), NOW(), %(usuario_id)s, %(noticia_id)s);
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM reports_noticias WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_reports_by_noticia(cls, noticia_id):
        query = "DELETE FROM reports_noticias WHERE noticia_id = %(noticia_id)s;"
        data = {"noticia_id": noticia_id}
        return connectToMySQL().query_db(query, data)
