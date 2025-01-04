import os
from sqlalchemy.pool import QueuePool

class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', None)
    if DATABASE_URL is None:
        raise ValueError("DATABASE_URL environment variable not set")
    print("Database URL:", DATABASE_URL)  # Debugging
    
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 5,
        "max_overflow": 10,
        "pool_timeout": 30,
        "poolclass": QueuePool,
    }
