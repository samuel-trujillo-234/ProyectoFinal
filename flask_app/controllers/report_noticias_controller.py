## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask_app import app
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from flask_app.models.report_noticia_model import ReportNoticia
from datetime import date
from flask_app.utils.decoradores import login_required



@app.route("/reportar_noticia/<int:noticia_id>", methods=['POST'])
@login_required
def reportar_noticia(noticia_id):
    usuario_id = session['id']
    data = {
        "usuario_id": usuario_id,
        "noticia_id": noticia_id
    }
    ReportNoticia.save(data)
    
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@app.route("/cancelar_report/<int:report_id>", methods=['POST'])
@login_required
def cancelar_report(report_id):
    report = ReportNoticia.get_one(report_id)
    # Verificar que el report existe y pertenece al usuario actual
    if report and report.usuario_id == session['id']:
        ReportNoticia.delete(report_id)
        # Si es una petición AJAX, devolver un JSON
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify(success=True)
        # Si no es AJAX, redirigir
        return redirect(f"/noticia/{report.noticia_id}")
    # Si el report no existe o no pertenece al usuario actual
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=False, message="No autorizado"), 403
    return redirect("/dashboard")


@app.route("/admin/reports")
@login_required
def listar_reports():
    # Aquí podrías agregar una verificación de que el usuario es administrador
    reports = ReportNoticia.get_all()
    return render_template("admin/reports_noticias.html", reports=reports)

