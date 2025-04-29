from flask import Flask, render_template
from flask_app import app


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)