from flask import Flask
from flask_cors import CORS
from app.models import db
from flask_jwt_extended import JWTManager
from app.routes import api
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Gunakan konfigurasi dari config.py

    # Aktifkan CORS dengan pengaturan sesuai dengan yang Anda inginkan
    CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type", "Authorization"], "expose_headers": ["Content-Length"]}})

    db.init_app(app)
    JWTManager(app)
    app.register_blueprint(api, url_prefix='/api')

    return app
