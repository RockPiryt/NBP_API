# import os
# from os.path import join, dirname
# from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from configuration import Configuration


#___________________________________________________________________________
# # Load .env file
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)


app = Flask(__name__)

#Configuration from FILE configuration.py
app.config.from_object(Configuration)

from NBP_API_project import operations

# SQLAlchemy (create Python object from tables records)
# db = SQLAlchemy(app)
# app.app_context().push()

# Migrate(app,db)







# # Configuration here (not recomended)
# # ----------------------------------- DB SQLite
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')


# # -----------------------------------DB PostgreSQL
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLalchemy_database_uri")



