## Coding Dojo - Python Bootcamp Jan 2025
## Final project
## Wavely


from flask_app import app
from flask import render_template, request, redirect, session, flash
from functools import wraps
from flask_app.models.noticia_model import Noticia
from flask_app.models.usuario_model import Usuario
from flask_app.models.comentario_model import Comentario
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
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), 
    os.getenv('UPLOAD_FOLDER', 'uploads')  # valor por defecto si no existe
)

# Convertir cadena separada por comas a conjunto
extensiones = os.getenv('ALLOWED_EXTENSIONS', 'jpg,jpeg,png,gif')  # valor por defecto
ALLOWED_EXTENSIONS = set(extensiones.split(','))

# Crear directorio de subidas si no existe
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
    usuarios=Usuario.get_all()
    noticia=Noticia.get_one(id)
    noticia_conteudo=noticia.noticia
    if noticia.usuario_id == session['id']:
        return render_template("/noticias/editar_noticia.html", nombre=session['nombre'], sobrenombre=session['sobrenombre'], id=session['id'], usuarios=usuarios, noticia=noticia, noticia_conteudo=noticia_conteudo)
    else:
        flash(f'Solo el usuario que creó la noticia puede editarla', "error")
    return redirect("/noticias")


@app.route("/update_noticia", methods=['POST'])
@login_required
def atualizar_noticia():
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
        'hechos': request.form['hechos'],
        'sesgo': request.form['sesgo'],
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
    Comentario.delete_comentarios_noticia(id)
    Noticia.delete(id)
    flash(f"La noticia y todos los comentarios asociados a ella han sido eliminados.", "warning")
    return redirect ('/noticias')


@app.route("/mostrar_noticia/<int:id>")
@login_required
def mostrar_noticia(id):
    usuarios=Usuario.get_all()
    noticia=Noticia.get_one(id)
    comentarios=Comentario.select(id)
    return render_template("/mostrar_noticia.html", id=session['id'], usuarios=usuarios, noticia=noticia, comentarios=comentarios)

