import os
from sqlalchemy.pool import QueuePool

class Config:
    # Menggunakan variabel lingkungan untuk koneksi database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@host:port/database?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Konfigurasi pooling untuk mengelola koneksi
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 5,
        "max_overflow": 10,
        "pool_timeout": 30,
        "poolclass": QueuePool,
    }
