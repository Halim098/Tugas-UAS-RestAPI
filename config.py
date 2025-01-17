import os

class Config:
    # Ambil URL dari variabel lingkungan
    SQLALCHEMY_DATABASE_URI = 'postgresql://posgres_owner:Qvzu3A6LwIEM@ep-super-wave-a10esii8.ap-southeast-1.aws.neon.tech/posgres?sslmode=require'
    
    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError("DATABASE_URL environment variable not set")
    
    print(f"Using database URL: {SQLALCHEMY_DATABASE_URI}")  # Debugging untuk memastikan URL yang benar

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', '12g3h1b2n3b12jhv3h1b2kh3b12bkKBKHBKJHb')

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_size": 5,
        "max_overflow": 10,
        "pool_timeout": 30,
    }
