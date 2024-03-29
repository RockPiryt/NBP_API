from NBP_API_project import db
from NBP_API_project.errors import errors_bp
from flask import Response, jsonify


class ErrorResponse:
    def __init__(self, message: str, http_status: int):
        self.payload = {
            'success': False,
            'message': message
        }

        self.http_status = http_status

    def make_response(self) -> Response:
        response = jsonify(self.payload)
        response.status_code = self.http_status
        return response


@errors_bp.app_errorhandler(404)
def not_found_error(err):
    return ErrorResponse(err.description, 404).make_response()


@errors_bp.app_errorhandler(400)
def bad_request_error(err):
    messages = err.data.get('messages', {}).get('json', {})
    return ErrorResponse(messages, 400).make_response()


@errors_bp.app_errorhandler(500)
def internal_server_error(err):
    db.session.rollback()
    return ErrorResponse(err.description, 500).make_response()
