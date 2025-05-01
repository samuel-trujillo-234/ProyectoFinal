## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely - Login Required


from flask import render_template, flash, redirect, session
from functools import wraps  

def login_required(funcion):
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        if 'email' not in session:
            flash("No has iniciado sesión", "error")
            return redirect("/")
        return funcion(*args, **kwargs)
    return wrapper


def tiene_permiso(role):
    def wrapper_permiso_main(funcion):
        @wraps(funcion)
        def wrapper_permiso(*args, **kwargs):
            
            if session['usuario']['role'] != role:
                flash("No eres administrador.", "error")
                return redirect("/")
            
            return funcion(*args, **kwargs)
        return wrapper_permiso
    return wrapper_permiso_main