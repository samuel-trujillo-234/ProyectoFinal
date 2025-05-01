## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Usuario:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.categoria = data['categoria']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Nuevos campos para configuraciones
        self.notificaciones_email = data.get('notificaciones_email', 0)
        self.notificaciones_nuevas = data.get('notificaciones_nuevas', 0)
        self.notificaciones_comentarios = data.get('notificaciones_comentarios', 0)
        self.perfil_publico = data.get('perfil_publico', 0)
        self.mostrar_email = data.get('mostrar_email', 0)
        self.tema = data.get('tema', 'claro')
        self.tamano_fuente = data.get('tamano_fuente', 'normal')
        self.cuenta_activa = data.get('cuenta_activa', 1)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL().query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append(cls(usuario))
        return usuarios


    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = { "id": id }
        usuario = connectToMySQL().query_db(query, data)
        return cls(usuario[0])


    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = { 'email': email }
        resultados = connectToMySQL().query_db(query, data)
        if len(resultados) == 0:
            return None
        usuario_recuperado = cls(resultados[0])
        return usuario_recuperado


    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO usuarios (
                nombre, apellido, email, password, categoria, 
                notificaciones_email, notificaciones_nuevas, notificaciones_comentarios,
                perfil_publico, mostrar_email, tema, tamano_fuente, cuenta_activa,
                created_at, updated_at
            ) VALUES (
                %(nombre)s, %(apellido)s, %(email)s, %(password)s, %(categoria)s,
                0, 0, 0, 0, 0, 'claro', 'normal', 1,
                NOW(), NOW()
            )
        """
        return connectToMySQL().query_db(query, data)


    @classmethod
    def update(cls, data):
        query = """
            UPDATE usuarios 
            SET nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                password = %(password)s,
                categoria = %(categoria)s,
                updated_at = NOW()
            WHERE id = %(id)s
        """
        return connectToMySQL().query_db(query, data)


    @classmethod
    def update_config(cls, data):
        query = """
            UPDATE usuarios 
            SET notificaciones_email = %(notificaciones_email)s,
                notificaciones_nuevas = %(notificaciones_nuevas)s,
                notificaciones_comentarios = %(notificaciones_comentarios)s,
                perfil_publico = %(perfil_publico)s,
                mostrar_email = %(mostrar_email)s,
                tema = %(tema)s,
                tamano_fuente = %(tamano_fuente)s,
                updated_at = NOW()
            WHERE id = %(id)s
        """
        return connectToMySQL().query_db(query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        data = { "id": id }
        return connectToMySQL().query_db(query, data)


    @classmethod
    def desactivar(cls, id):
        query = "UPDATE usuarios SET cuenta_activa = 0 WHERE id = %(id)s;"
        data = { "id": id }
        return connectToMySQL().query_db(query, data)


    @classmethod
    def update_categoria(cls, user_id, categoria):
        """
        Actualiza solo la categoría de un usuario.
        Retorna True si la actualización fue exitosa, False en caso contrario.
        """
        query = "UPDATE usuarios SET categoria = %(categoria)s, updated_at = NOW() WHERE id = %(id)s"
        data = {
            "id": user_id,
            "categoria": categoria
        }
        return connectToMySQL().query_db(query, data)


    @classmethod
    def check_email(cls, email):
        query = "SELECT COUNT(*) as count FROM usuarios WHERE email = %(email)s;"
        data = { 'email': email }
        result = connectToMySQL().query_db(query, data)
        return result[0]['count'] > 0


    @staticmethod
    def validar_usuario(usuario):
        valido = True
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$')
        if len(usuario['nombre']) <= 2 or len(usuario['apellido']) <= 2:
            flash("Nombre y apellido deben tener más de dos caracteres.", "error")
            valido = False
        if 'password' in usuario and usuario.get('confirmacion_password'):
            if usuario['password'] != usuario['confirmacion_password']:
                flash("Las contraseñas no coinciden.", "error")
                valido = False
            if not password_regex.match(usuario['password']):
                flash("La contraseña debe tener al menos 8 caracteres, incluir mayúsculas, minúsculas, números y caracteres especiales.", "error")
                valido = False
        if not email_regex.match(usuario['email']):
            flash("Dirección de correo electrónico inválida.", "error")
            valido = False
        return valido