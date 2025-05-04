## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from datetime import date
from datetime import datetime
from flask_app.models.usuario_model import Usuario
from flask_app.models.comentario_model import Comentario

today = date.today()

class Noticia:

    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.noticia = data['noticia']
        self.foto_video = data['foto_video']
        self.tags = data['tags']
        self.revisada = data['revisada']
        self.keywords = data['keywords']
        self.hechos = data['hechos']
        self.sesgo = data['sesgo']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.nombre_usuario = data['nombre_usuario']
        self.comentarios_count = data.get('comentarios_count', 0)  # Default to 0 if not provided

    @classmethod
    def get_all(cls):
        query = """
        SELECT noticias.id AS id, noticias.titulo AS titulo, noticias.noticia AS noticia, noticias.foto_video AS foto_video,
               noticias.tags AS tags, noticias.revisada AS revisada, noticias.keywords AS keywords, noticias.hechos AS hechos,
               noticias.sesgo AS sesgo, noticias.created_at AS created_at, noticias.updated_at AS updated_at,
               noticias.usuario_id AS usuario_id, usuarios.nombre AS nombre_usuario,
               COUNT(comentarios.id) AS comentarios_count
        FROM noticias
        LEFT JOIN usuarios ON noticias.usuario_id = usuarios.id
        LEFT JOIN comentarios ON noticias.id = comentarios.noticia_id
        GROUP BY noticias.id;
        """
        results = connectToMySQL().query_db(query)
        noticias = []
        for noticia in results:
            noticias.append(cls(noticia))
        return noticias

    @classmethod
    def get_one(cls, id):
        query = """
        SELECT noticias.id AS id, noticias.titulo AS titulo, noticias.noticia AS noticia, noticias.foto_video AS foto_video,
               noticias.tags AS tags, noticias.revisada AS revisada, noticias.keywords AS keywords, noticias.hechos AS hechos,
               noticias.sesgo AS sesgo, noticias.created_at AS created_at, noticias.updated_at AS updated_at,
               noticias.usuario_id AS usuario_id, usuarios.nombre AS nombre_usuario,
               COUNT(comentarios.id) AS comentarios_count
        FROM noticias
        LEFT JOIN usuarios ON noticias.usuario_id = usuarios.id
        LEFT JOIN comentarios ON noticias.id = comentarios.noticia_id
        WHERE noticias.id = %(id)s
        GROUP BY noticias.id;
        """
        data = {"id": id}
        result = connectToMySQL().query_db(query, data)
        return cls(result[0]) if result else None


    @classmethod
    def get_favoritas(cls):
        query = """
        SELECT noticias.id AS id, noticias.titulo AS titulo, noticias.noticia AS noticia, noticias.foto_video AS foto_video,
               noticias.tags AS tags, noticias.revisada AS revisada, noticias.keywords AS keywords, noticias.hechos AS hechos,
               noticias.sesgo AS sesgo, noticias.created_at AS created_at, noticias.updated_at AS updated_at,
               noticias.usuario_id AS usuario_id, usuarios.nombre AS nombre_usuario,
               COUNT(comentarios.id) AS comentarios_count
        FROM favoritos
        JOIN noticias ON favoritos.noticia_id = noticias.id
        LEFT JOIN usuarios ON noticias.usuario_id = usuarios.id
        LEFT JOIN comentarios ON noticias.id = comentarios.noticia_id
        WHERE favoritos.usuario_id = %(usuario_id)s
        GROUP BY noticias.id;
        """
        data = {"usuario_id": session['id']}
        results = connectToMySQL().query_db(query, data)
        noticias = []
        for noticia in results:
            noticias.append(cls(noticia))
        return noticias

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO noticias (titulo, noticia, foto_video, tags, revisada, keywords, hechos, sesgo, created_at, updated_at, usuario_id)
        VALUES (%(titulo)s, %(noticia)s, %(foto_video)s, %(tags)s, %(revisada)s, %(keywords)s, %(hechos)s, %(sesgo)s, %(created_at)s, %(updated_at)s, %(usuario_id)s);
        """
        # Add current timestamp for created_at and updated_at
        data_with_dates = data.copy()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_with_dates['created_at'] = current_time
        data_with_dates['updated_at'] = current_time
        
        return connectToMySQL().query_db(query, data_with_dates)

    @classmethod
    def delete(cls, id):
        Comentario.delete_por_noticia(id)
        query = "DELETE FROM noticias WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL().query_db(query, data)

    @classmethod
    def update(cls, data):
        query = """
        UPDATE noticias
        SET titulo = %(titulo)s, noticia = %(noticia)s, foto_video = %(foto_video)s, tags = %(tags)s, revisada = %(revisada)s,
            keywords = %(keywords)s, hechos = %(hechos)s, sesgo = %(sesgo)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL().query_db(query, data)

    @classmethod
    def check_titulo_noticia(cls, titulo, noticia_id):
        titulo_disponible = True
        titulo_limpio = titulo.replace(" ", "").lower()
        query = "SELECT * FROM noticias WHERE LOWER(REPLACE(titulo, ' ', '')) = %(titulo_limpio)s AND id != %(id)s;"
        data = {
            'titulo_limpio': titulo_limpio,
            'id': noticia_id
        }
        results = connectToMySQL().query_db(query, data)
        if len(results) > 0:
            titulo_disponible = False
        return titulo_disponible

    @staticmethod
    def validar_noticia(noticia, noticia_id):
        valido = True
        session['noticia'] = noticia['noticia']
        # Supondo que la fecha de la noticia está en noticia['created_at'] y es opcional
        # Si hay campo de fecha de publicación, ajustar aquí
        if len(noticia['titulo']) <= 3:
            flash("El título de la noticia debe tener más de dos caracteres.", "error")
            valido = False
        if len(noticia['noticia']) <= 3:
            flash("El contenido de la noticia debe tener más de dos caracteres.", "error")
            valido = False
        if len(noticia['noticia']) > 5000:
            flash("El tamaño máximo del contenido es de 5000 caracteres. Ajuste el texto e intente nuevamente.", "error")
            valido = False
        if Noticia.check_titulo_noticia(noticia['titulo'], noticia_id) == False:
            flash("Ya existe una noticia registrada con este título.", "error")
            valido = False
        # Validaciones adicionales según necesidad
        return valido