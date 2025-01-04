import os

class Config:
    # Ambil URL dari variabel lingkungan
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', None)
    
    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError("DATABASE_URL environment variable not set")
    
    print(f"Using database URL: {SQLALCHEMY_DATABASE_URI}")  # Debugging untuk memastikan URL yang benar

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 5,
        "max_overflow": 10,
        "pool_timeout": 30,
    }
