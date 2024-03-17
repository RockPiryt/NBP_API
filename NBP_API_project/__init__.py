from flask import Flask
from configuration import Configuration

from NBP_API_project import operations


app = Flask(__name__)
app.config.from_object(Configuration)



# @app.route('/')
# def index():
#     return 'Hello I am Paulina'