from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from configuration import config_dict

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name="development"):

    app = Flask(__name__)

    # Configuration from FILE configuration.py - use dict key
    app.config.from_object(config_dict[config_name])

    # app.app_context().push()

    # Make relations between app and db/migrate instances
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    # Imports/ blueprints
    from NBP_API_project.operations import operations_bp
    from NBP_API_project.errors import errors_bp
    
    app.register_blueprint(operations_bp)
    app.register_blueprint(errors_bp)

    return app
