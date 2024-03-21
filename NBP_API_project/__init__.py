from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from configuration import config_dict

app = Flask(__name__)

#Configuration from FILE configuration.py - use dict key
app.config.from_object(config_dict['development'])

from NBP_API_project import operations

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app,db)

from NBP_API_project import models