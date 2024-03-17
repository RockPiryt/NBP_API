import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Configuration:
    DEBUG = True
    SECRET_KEY = os.getenv("flask_secret_key")


# To check correct loading
# print(Config.SECRET_KEY)