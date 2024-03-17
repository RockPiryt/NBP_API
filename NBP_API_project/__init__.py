from flask import Flask
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# MY_EMAIL = os.getenv("my_email")
# API_KEY_GMAIL = os.getenv("api_key_gmail")

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello I am Paulina'