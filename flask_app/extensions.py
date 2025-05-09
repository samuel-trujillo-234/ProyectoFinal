from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def init_app(app):
    """Initialize all extensions with the Flask app."""
    bcrypt.init_app(app)
