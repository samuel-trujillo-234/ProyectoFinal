## Coding Dojo - Python Bootcamp Ene 2025
## Proyecto final
## Wavely


from flask_app import app
from flask import render_template, request, redirect, session, flash
from functools import wraps
from flask_app.models.noticia_model import Noticia
from flask_app.models.usuario_model import Usuario
from flask_app.models.comentario_model import Comentario
from flask_app.models.favorito_model import Favorito
from flask_app.models.report_noticia_model import ReportNoticia
from datetime import date
from flask_app.utils.decoradores import login_required
import os
import uuid
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

today = date.today()

# Configurar carpeta de subidas desde variables de entorno
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                            os.getenv('UPLOAD_FOLDER'))

# Convertir cadena separada por comas a conjunto
ALLOWED_EXTENSIONS = set(os.getenv('ALLOWED_EXTENSIONS').split(','))

# Crear directorio de subidas si no existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False


@app.route('/noticias')
@login_required
def mostrar_noticias():
    session['noticia']=""
    nombre = session['nombre']
    if nombre is None:
        return redirect('/') 
    noticias=Noticia.get_all()
    return render_template("/noticias.html", nombre=session['nombre'], apellido=session['apellido'], id=session['id'], noticias=noticias, today=today)


@app.route("/adicionar_noticia")
@login_required
def adicionar_noticia():
    usuarios=Usuario.get_all()
    return render_template("/adicionar_noticia.html", nombre=session['nombre'], apellido=session['apellido'], id=session['id'], usuarios=usuarios, noticia="")


@app.route("/crear_noticia", methods=['POST'])
@login_required
def criar_noticia():
    hechos = ""
    sesgo = ""
    file_path = ""
    if 'archivo_multimedia' in request.files:
        file = request.files['archivo_multimedia']
        if file and file.filename != '' and allowed_file(file.filename):
            # Generar un nombre de archivo único para evitar sobrescribir
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            file_save_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            # Guardar el archivo
            file.save(file_save_path)
            # Establecer la ruta del archivo para almacenarla en la base de datos (ruta relativa para URL)
            file_path = f"/static/uploads/{unique_filename}"
    data = {
        'titulo': request.form['titulo'],
        'noticia': request.form['noticia'],
        'foto_video': request.form['foto_video'] if not file_path else file_path,
        'tags': request.form['tags'],
        'revisada': request.form.get('revisada', 0),
        'keywords': request.form['keywords'],
        'hechos': hechos,
        'sesgo': sesgo,
        'usuario_id': session['id']
    }
    if Noticia.validar_noticia(data, 0) != True:
        return redirect ("/adicionar_noticia")
    Noticia.save(data)   
    flash(f'Nueva noticia añadida con éxito: "{data["titulo"]}".', "success")
    session['noticia']=""
    return redirect("/noticias")


@app.route("/editar_noticia/<int:id>")
@login_required
def editar_noticia(id):
    noticia=Noticia.get_one(id)
    noticia_conteudo=noticia.noticia
    if noticia.usuario_id == session['id']:
        return render_template("/editar_noticia.html", nombre=session['nombre'], apellido=session['apellido'], id=session['id'], noticia=noticia)
    else:
        flash(f'Solo el usuario que creó la noticia puede editarla', "error")
    return redirect("/noticias")


@app.route("/update_noticia", methods=['POST'])
@login_required
def atualizar_noticia():
    hechos = ""
    sesgo = ""
    file_path = ""
    # Manejar la subida de archivo si existe
    if 'archivo_multimedia' in request.files:
        file = request.files['archivo_multimedia']
        if file and file.filename != '' and allowed_file(file.filename):
            # Generar un nombre de archivo único para evitar sobrescribir
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            file_save_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            # Guardar el archivo
            file.save(file_save_path)
            # Establecer la ruta del archivo para almacenarla en la base de datos (ruta relativa para URL)
            file_path = f"/static/uploads/{unique_filename}"
    data = {
        'id': request.form['id'],
        'titulo': request.form['titulo'],
        'noticia': request.form['noticia'],
        'foto_video': request.form['foto_video'] if not file_path else file_path,
        'tags': request.form['tags'],
        'revisada': request.form.get('revisada', 0),
        'keywords': request.form['keywords'],
        'hechos': hechos,
        'sesgo': sesgo,
        'usuario_id': session['id']
    }
    if Noticia.validar_noticia(data, request.form['id']) != True:
        return redirect (f"/editar_noticia/{data['id']}")
    Noticia.update(data)
    flash(f"Noticia actualizada con éxito.", "success")
    session['noticia']=""
    return redirect("/noticias")


@app.route("/eliminar_noticia/<int:id>")
@login_required
def eliminar_noticia(id):
    Noticia.delete(id)
    flash(f"La noticia y todos los comentarios asociados a ella han sido eliminados.", "warning")
    return redirect ('/noticias')


@app.route("/noticia/<int:id>")
@login_required
def mostrar_noticia(id):
    usuarios=Usuario.get_all()
    noticia=Noticia.get_one(id)
    comentarios=Comentario.select_noticia(id)
    favoritos_count = Favorito.get_count_by_noticia(id)
    usuario_ha_favorito = Favorito.check_if_favorited(session['id'], id)
    reports_count = ReportNoticia.get_count_by_noticia(id) 
    usuario_ha_reportado = ReportNoticia.check_if_reported(session['id'], id)
    return render_template("/mostrar_noticia.html", 
                          nombre=session['nombre'], 
                          apellido=session['apellido'], 
                          id=session['id'], 
                          usuarios=usuarios, 
                          noticia=noticia, 
                          comentarios=comentarios, 
                          favoritos_count=favoritos_count, 
                          usuario_ha_favorito=usuario_ha_favorito,
                          reports_count=reports_count,
                          usuario_ha_reportado=usuario_ha_reportado,
                          )


@app.route('/favoritos')
@login_required
def favoritos():
    noticias=Noticia.get_favoritas()
    return render_template("/favoritos.html", nombre=session['nombre'], apellido=session['apellido'], id=session['id'], noticias=noticias, today=today)
