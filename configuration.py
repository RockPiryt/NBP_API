import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from pathlib import Path


# Load .env file
load_dotenv(find_dotenv())


class Configuration:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = ' '
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Configuration):
    username_postdb = os.getenv("postgreSQL_username")
    password_postdb = os.getenv("postgreSQL_password")
    database_postdb = os.getenv("postgreSQL_database")
    host_postdb = os.getenv("postgreSQL_host")
    SQLALCHEMY_DATABASE_URI= f"postgresql://{username_postdb}:{password_postdb}@{host_postdb}/{database_postdb}"
    DEBUG = True


class TestingConfig(Configuration):
    base_dir = Path(__file__).resolve().parent
    DB_FILE_PATH = base_dir / 'tests' / 'tests.db'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE_PATH}'
    DEBUG = True
    TESTING = True


config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
