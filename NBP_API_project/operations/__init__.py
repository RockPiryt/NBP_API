from flask import Blueprint

operations_bp = Blueprint('operations', __name__)

from NBP_API_project.operations import operations