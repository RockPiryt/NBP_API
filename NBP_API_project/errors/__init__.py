from flask import Blueprint

errors_bp = Blueprint('errors', __name__)

from NBP_API_project.errors import errors