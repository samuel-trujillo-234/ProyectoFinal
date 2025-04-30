from flask import Flask, render_template
from flask_app import app

from flask_app.controllers import usuarios_controller
from flask_app.controllers import autentication_controller

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/favoritos')
def favoritos():
    return render_template('favoritos.html')


@app.route('/crear')
def crear():
    return render_template('crear.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')


if __name__ == '__main__':
    app.run(debug=True)