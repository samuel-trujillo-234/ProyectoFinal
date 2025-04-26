from flask_app import app
import os
from flask_app.controllers import usuarios_controller
from flask_app.controllers import autentication

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)