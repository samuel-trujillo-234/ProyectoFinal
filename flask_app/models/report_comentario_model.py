## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from datetime import date
from datetime import datetime
from flask_app.models.usuario_model import Usuario
from flask_app.models.noticia_model import Noticia

today = date.today()

class ReportComentario:

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.noticia_id = data['noticia_id']

    @classmethod
    def get_all(cls):
        query = """
        SELECT reports_comentarios.id AS id, reports_comentarios.explicacions AS explicacions,
               reports_comentarios.created_at AS created_at, reports_comentarios.updated_at AS updated_at,
               reports_comentarios.usuario_id AS usuario_id, reports_comentarios.noticia_id AS noticia_id,
               usuarios.nome AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM reports_comentarios
        LEFT JOIN usuarios ON reports_comentarios.usuario_id = usuarios.id
        LEFT JOIN noticias ON reports_comentarios.noticia_id = noticias.id;
        """
        results = connectToMySQL().query_db(query)
        reports = []
        for report in results:
            reports.append(cls(report))
        return reports

    @classmethod
    def get_one(cls, id):
        query = """
        SELECT reports_comentarios.id AS id, reports_comentarios.explicacions AS explicacions,
               reports_comentarios.created_at AS created_at, reports_comentarios.updated_at AS updated_at,
               reports_comentarios.usuario_id AS usuario_id, reports_comentarios.noticia_id AS noticia_id,
               usuarios.nome AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM reports_comentarios
        LEFT JOIN usuarios ON reports_comentarios.usuario_id = usuarios.id
        LEFT JOIN noticias ON reports_comentarios.noticia_id = noticias.id
        WHERE reports_comentarios.id = %(id)s;
        """
        data = {"id": id}
        result = connectToMySQL().query_db(query, data)
        return cls(result[0]) if result else None

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO reports_comentarios (explicacions, created_at, updated_at, usuario_id, noticia_id)
        VALUES (%(explicacions)s, NOW(), NOW(), %(usuario_id)s, %(noticia_id)s);
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM reports_comentarios WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL().query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE reports_comentarios
        SET explicacions = %(explicacions)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL().query_db(query, data)

    @staticmethod
    def validar_explicacions(report, report_id):
        valido = True
        session['explicacion'] = report['explicacion']
        if len(report['explicacion']) <= 3:
            flash("La explicación debe tener más de dos caracteres.", "error")
            valido = False
        if len(report['explicacion']) > 300:
            flash("El tamaño máximo de la explicación es de 300 caracteres. Ajuste el texto e intente nuevamente.", "error")
            valido = False
        return valido
    
    @classmethod
    def delete_denuncias_by_comentario(cls, comentario_id):
        query = "DELETE FROM reports_comentarios WHERE comentario_id = %(comentario_id)s;"
        data = {"comentario_id": comentario_id}
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_denuncias_by_noticia(cls, noticia_id):
        query = "DELETE FROM reports_comentarios WHERE noticia_id = %(noticia_id)s;"
        data = {"noticia_id": noticia_id}
        return connectToMySQL().query_db(query, data)
