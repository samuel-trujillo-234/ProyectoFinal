## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from datetime import date
from datetime import datetime
from flask_app.models.usuario_model import Usuario

today = date.today()

class Comentario:

    def __init__(self, data):
        self.id = data['id']
        self.comentario = data['comentario']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.noticia_id = data['noticia_id']
        self.nombre_usuario = data['nombre_usuario']


    @classmethod
    def get_all(cls):
        query = """
        SELECT comentarios.id AS id, comentarios.comentario AS comentario,
               comentarios.created_at AS created_at, comentarios.updated_at AS updated_at,
               comentarios.usuario_id AS usuario_id, comentarios.noticia_id AS noticia_id,
               usuarios.nombre AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM comentarios
        LEFT JOIN usuarios ON comentarios.usuario_id = usuarios.id
        LEFT JOIN noticias ON comentarios.noticia_id = noticias.id;
        """
        results = connectToMySQL().query_db(query)
        comentarios = []
        for comentario in results:
            comentarios.append(cls(comentario))
        return comentarios


    @classmethod
    def get_one(cls, id):
        query = """
        SELECT comentarios.id AS id, comentarios.comentario AS comentario,
               comentarios.created_at AS created_at, comentarios.updated_at AS updated_at,
               comentarios.usuario_id AS usuario_id, comentarios.noticia_id AS noticia_id,
               usuarios.nombre AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM comentarios
        LEFT JOIN usuarios ON comentarios.usuario_id = usuarios.id
        LEFT JOIN noticias ON comentarios.noticia_id = noticias.id
        WHERE comentarios.id = %(id)s;
        """
        data = {"id": id}
        result = connectToMySQL().query_db(query, data)
        return cls(result[0]) if result else None


    @classmethod
    def select_noticia(cls, id):
        query = """
        SELECT comentarios.id AS id, comentarios.comentario AS comentario,
               comentarios.created_at AS created_at, comentarios.updated_at AS updated_at,
               comentarios.usuario_id AS usuario_id, comentarios.noticia_id AS noticia_id,
               usuarios.nombre AS nombre_usuario,
               noticias.titulo AS titulo_noticia
        FROM comentarios
        LEFT JOIN usuarios ON comentarios.usuario_id = usuarios.id
        LEFT JOIN noticias ON comentarios.noticia_id = noticias.id
        WHERE noticias.id = %(id)s
        ORDER BY comentarios.created_at DESC;
        """
        data = {"id": id}
        results = connectToMySQL().query_db(query, data)
        comentarios = []
        if results:  # Check if results is not None or False
            for comentario in results:
                comentarios.append(cls(comentario))
        return comentarios


    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO comentarios (comentario, created_at, updated_at, usuario_id, noticia_id)
        VALUES (%(comentario)s, NOW(), NOW(), %(usuario_id)s, %(noticia_id)s);
        """
        return connectToMySQL().query_db(query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM comentarios WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL().query_db(query, data)


    @classmethod
    def update(cls, data):
        query = """
        UPDATE comentarios
        SET comentario = %(comentario)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL().query_db(query, data)


    @staticmethod
    def validar_comentario(comentario, comentario_id):
        valido = True
        session['comentario'] = comentario['comentario']
        if len(comentario['comentario']) <= 3:
            flash("El contenido del comentario debe tener más de dos caracteres.", "error")
            valido = False
        if len(comentario['comentario']) > 100:
            flash("El tamaño máximo del comentario es de 100 caracteres. Ajuste el texto e intente nuevamente.", "error")
            valido = False
        return valido