from flask_app.controllers.administrador_controller import administrador
from flask_app.controllers.autentication_controller import autentication
from flask_app.controllers.comentarios_controller import comentarios
from flask_app.controllers.favoritos_controller import favoritos
from flask_app.controllers.favorito_controller import favoritos as favorito
from flask_app.controllers.likes_comentarios_controller import likes_comentarios
from flask_app.controllers.likes_noticias_controller import likes_noticias
from flask_app.controllers.noticias_controller import noticias
from flask_app.controllers.report_comentarios_controller import report_comentarios
from flask_app.controllers.report_noticias_controller import report_noticias
from flask_app.controllers.usuarios_controller import usuarios

def register_controllers(app):
    app.register_blueprint(administrador, url_prefix='/administrador')
    app.register_blueprint(autentication, url_prefix='/autentication')
    app.register_blueprint(comentarios, url_prefix='/comentarios')
    app.register_blueprint(favoritos, url_prefix='/favoritos')
    app.register_blueprint(favorito, url_prefix='')
    app.register_blueprint(likes_comentarios, url_prefix='/likes_comentarios')
    app.register_blueprint(likes_noticias, url_prefix='/likes_noticias')
    app.register_blueprint(noticias, url_prefix='/noticias')
    app.register_blueprint(report_comentarios, url_prefix='/report_comentarios')
    app.register_blueprint(report_noticias, url_prefix='/report_noticias')
    app.register_blueprint(usuarios, url_prefix='/usuarios')