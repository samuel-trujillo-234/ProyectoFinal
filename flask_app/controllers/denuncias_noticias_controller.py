## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely

from flask_app import app
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from flask_app.models.denuncia_noticia_model import DenunciaNoticia
from datetime import date
from flask_app.utils.decoradores import login_required



@app.route("/denunciar_noticia/<int:noticia_id>", methods=['POST'])
@login_required
def denunciar_noticia(noticia_id):
    usuario_id = session['id']
    data = {
        "usuario_id": usuario_id,
        "noticia_id": noticia_id
    }
    DenunciaNoticia.save(data)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@app.route("/cancelar_denuncia/<int:denuncia_id>", methods=['POST'])
@login_required
def cancelar_denuncia(denuncia_id):
    denuncia = DenunciaNoticia.get_one(denuncia_id)
    
    # Verificar que la denuncia existe y pertenece al usuario actual
    if denuncia and denuncia.usuario_id == session['id']:
        DenunciaNoticia.delete(denuncia_id)
        
        # Si es una petición AJAX, devolver un JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(success=True)
        # Si no es AJAX, redirigir
        return redirect(f"/noticia/{denuncia.noticia_id}")
    
    # Si la denuncia no existe o no pertenece al usuario actual
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=False, message="No autorizado"), 403
    return redirect("/dashboard")


@app.route("/admin/denuncias")
@login_required
def listar_denuncias():
    # Aquí podrías agregar una verificación de que el usuario es administrador
    denuncias = DenunciaNoticia.get_all()
    return render_template("admin/denuncias_noticias.html", denuncias=denuncias)

