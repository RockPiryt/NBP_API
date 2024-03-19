import os
from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path

base_dir = Path(__file__).resolve().parent

# Load .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Configuration:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = ' '
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Configuration):
    # SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_POSTGRES_DB_URI")
    pass


class TestingConfig(Configuration):
    DB_FILE_PATH = base_dir / 'tests' / 'tests.db'
    #SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_SQLITE_DB_URI")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_FILE_PATH}'
    DEBUG = True
    TESTING = True


config_dict = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}

# To check correct loading
# print(Config.SECRET_KEY)
