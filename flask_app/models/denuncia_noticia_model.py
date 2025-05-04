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

class DenunciaNoticia:

    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.noticia_id = data['noticia_id']

    @classmethod
    def get_all(cls):
        query = """
        SELECT denuncias_noticias.id AS id,
               denuncias_noticias.created_at AS created_at, denuncias_noticias.updated_at AS updated_at,
               denuncias_noticias.usuario_id AS usuario_id, denuncias_noticias.noticia_id AS noticia_id,
               usuarios.nome AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM denuncias_noticias
        LEFT JOIN usuarios ON denuncias_noticias.usuario_id = usuarios.id
        LEFT JOIN noticias ON denuncias_noticias.noticia_id = noticias.id;
        """
        results = connectToMySQL().query_db(query)
        denuncias = []
        for denuncia in results:
            denuncias.append(cls(denuncia))
        return denuncias

    @classmethod
    def get_one(cls, id):
        query = """
        SELECT denuncias_noticias.id AS id,
               denuncias_noticias.created_at AS created_at, denuncias_noticias.updated_at AS updated_at,
               denuncias_noticias.usuario_id AS usuario_id, denuncias_noticias.noticia_id AS noticia_id,
               usuarios.nome AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM denuncias_noticias
        LEFT JOIN usuarios ON denuncias_noticias.usuario_id = usuarios.id
        LEFT JOIN noticias ON denuncias_noticias.noticia_id = noticias.id
        WHERE denuncias_noticias.id = %(id)s;
        """
        data = {"id": id}
        result = connectToMySQL().query_db(query, data)
        return cls(result[0]) if result else None

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO denuncias_noticias (created_at, updated_at, usuario_id, noticia_id)
        VALUES (NOW(), NOW(), %(usuario_id)s, %(noticia_id)s);
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete(cls, id):
        query = "DELETE FROM denuncias_noticias WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL().query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE denuncias_noticias
        SET updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def delete_denuncias_by_noticia(cls, noticia_id):
        query = "DELETE FROM denuncias_noticias WHERE noticia_id = %(noticia_id)s;"
        data = {"noticia_id": noticia_id}
        return connectToMySQL().query_db(query, data)
