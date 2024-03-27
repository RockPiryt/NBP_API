from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from configuration import config_dict

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=config_dict['development']):

    app = Flask(__name__)

    # Configuration from FILE configuration.py - use dict key
    app.config.from_object(config_dict[config_class])

    app.app_context().push()

    # Make relations between app and db/migrate instances
    db.init_app(app)
    migrate.init_app(app, db)

    # Imports/ blueprints
    from NBP_API_project import models
    from NBP_API_project import operations
    from NBP_API_project import errors

    return app
