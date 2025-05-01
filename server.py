from flask import Flask, render_template
from flask_app import app

from flask_app.controllers import usuarios_controller
from flask_app.controllers import autentication_controller
from flask_app.controllers import administrador_controller
from flask_app.controllers import noticias_controller


@app.route('/favoritos')
def favoritos():
    return render_template('favoritos.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


if __name__ == '__main__':
    app.run(debug=True)