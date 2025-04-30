## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Usuario:

    def __init__(self , data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.categoria = data['categoria']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        results = connectToMySQL().query_db(query)
        usuarios = []
        for usuario in results:
            usuarios.append( cls(usuario) )
        return usuarios


    @classmethod
    def get_one(cls, id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        data = { "id": id }
        usuario = connectToMySQL().query_db(query, data)
        return cls(usuario[0])


    @classmethod
    def get_by_email(cls, email):
        query = "SELECT id, nombre, apellido, email, password, categoria, created_at, updated_at FROM usuarios WHERE email = %(email)s;"
        data = {
            'email': email
        }
        resultados = connectToMySQL().query_db(query, data)
        if len(resultados) == 0:
            return None
        usuario_recuperado = cls(resultados[0])
        return usuario_recuperado


    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, categoria, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(categoria)s, NOW(), NOW())"
        return connectToMySQL().query_db(query, data)


    @classmethod
    def delete(cls, id):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        data = { "id": id }
        return connectToMySQL().query_db(query, data)


    @classmethod
    def update(cls, usuario):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido = %(apellido)s, email = %(email)s, categoria = %(categoria)s, updated_at = NOW() WHERE id = %(id)s"
        data = {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "email": usuario.email,
            "categoria": usuario.categoria,
            }
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
        email_disponivel = True
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {
            'email': email
        }
        results = connectToMySQL().query_db(query, data)
        quantos = len(results)
        if quantos > 0:
            email_disponivel = False
        return email_disponivel


    @staticmethod
    def validar_usuario(usuario):
        valido = True
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
        password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s]).{8,}$')
        if len(usuario['nombre']) <= 2 or len(usuario['apellido']) <= 2:
            flash("Nombre y apellido deben tener mas de dos caracteres.", "error")
            print("Nombre y apellido deben tener mas de dos caracteres.", "error")
            valido = False
        if usuario['password'] != usuario['confirmacion_password']:
            flash("Las contraseñas informadas no coinciden.", "error")
            valido = False
        if not email_regex.match(usuario['email']):
            flash("Dirección de correo electrónico inválida.", "error")
            valido = False
        if not password_regex.match(usuario['password']):
            flash("La contraseña debe tener como mínimo 8 caracteres y contener al menos una letra mayúscula, una minúscula, un número y un carácter especial..", "error")
            valido = False
        if Usuario.check_email(usuario['email']) == False:
            flash("Dirección de correo electrónico ya en uso. Probá con otra.", "error")
            valido = False
        return valido