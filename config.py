import os

DB_HOST = 'db.mlvjbuusruadndqlhyop.supabase.co'
DB_USER = 'postgres'
DB_PASSWORD = 'mXK8f5R32A3awd4W'
DB_NAME = 'postgres'
DB_PORT = '5432'

SECRET_KEY='12g3h1b2n3b12jhv3h1b2kh3b12bkKBKHBKJHb'


class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = SECRET_KEY