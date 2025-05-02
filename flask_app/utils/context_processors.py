## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

"""
Utilidades de procesadores de contexto para la aplicación Flask.
Hace que los datos de sesión estén disponibles para todas las plantillas.
"""

from flask import session

def inject_user_data():
    """
    Procesador de contexto para inyectar datos de sesión de usuario en todas las plantillas.
    Hace que las variables 'usuario' y 'role' estén disponibles en todas las plantillas.
    
    Returns:
        dict: Diccionario que contiene datos de sesión del usuario
    """
    user_data = {
        "usuario": session.get('nombre', None),
        "role": session.get('categoria', None)
    }
    return user_data