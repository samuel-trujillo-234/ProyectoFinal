## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask import Blueprint
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from flask_app.models.report_comentario_model import ReportComentario
from datetime import date
from flask_app.utils.decoradores import login_required

report_comentarios = Blueprint('report_comentarios', __name__)

@report_comentarios.route("/reportar_comentario/<int:comentario_id>", methods=['POST'])
@login_required
def reportar_comentario(comentario_id):
    usuario_id = session['id']
    ReportComentario.save(usuario_id, comentario_id)
    reports_count = ReportComentario.get_count_by_comentario(comentario_id)
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, count=reports_count)
    # Si no es AJAX, redirigir
    return redirect(request.referrer or "/")


@report_comentarios.route("/cancelar_report_comentario/<int:comentario_id>", methods=['POST'])
@login_required
def cancelar_report_comentario(comentario_id):
    usuario_id = session['id']
    ReportComentario.delete(usuario_id, comentario_id)
    reports_count = ReportComentario.get_count_by_comentario(comentario_id)
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, count=reports_count)
    # Si no es AJAX, redirigir
    return redirect(request.referrer or "/")


@report_comentarios.route("/admin/reports_comentarios")
@login_required
def listar_reports_comentarios():
    # Aquí podrías agregar una verificación de que el usuario es administrador
    reports = ReportComentario.get_all()
    return render_template("admin/reports_comentarios.html", reports=reports)

