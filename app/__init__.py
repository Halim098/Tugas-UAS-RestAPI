from flask import Flask
from app.models import db
from flask_jwt_extended import JWTManager
from app.routes import api
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Gunakan konfigurasi dari config.py

    db.init_app(app)
    JWTManager(app)
    app.register_blueprint(api, url_prefix='/api')

    return app
