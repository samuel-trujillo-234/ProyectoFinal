## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely

from flask import Blueprint
from flask import render_template, request, redirect, session, jsonify
from flask_app.models.favorito_model import Favorito
from flask_app.models.report_noticia_model import ReportNoticia
from datetime import date
from flask_app.utils.decoradores import login_required

report_noticias = Blueprint('report_noticias', __name__)

@report_noticias.route("/reportar_noticia/<int:noticia_id>", methods=['POST'])
@login_required
def reportar_noticia(noticia_id):
    usuario_id = session['id']
    ReportNoticia.save(usuario_id, noticia_id)
    reports_count = ReportNoticia.get_count_by_noticia(noticia_id)
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, count=reports_count)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@report_noticias.route("/cancelar_report/<int:noticia_id>", methods=['POST'])
@login_required
def cancelar_report(noticia_id):
    usuario_id = session['id']
    ReportNoticia.delete(usuario_id, noticia_id)
    reports_count = ReportNoticia.get_count_by_noticia(noticia_id)
    # Si es una petición AJAX, devolver un JSON
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify(success=True, count=reports_count)
    # Si no es AJAX, redirigir
    return redirect(f"/noticia/{noticia_id}")


@report_noticias.route("/admin/reports")
@login_required
def listar_reports():
    # Aquí podrías agregar una verificación de que el usuario es administrador
    reports = ReportNoticia.get_all()
    return render_template("admin/reports_noticias.html", reports=reports)

