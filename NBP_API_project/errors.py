from NBP_API_project import app
from flask import Response, jsonify

class ErrorResponse:
    def __init__(self, message: str, http_status: int):
        self.payload = {
            'success': False,
            'message': message
        }

        self.http_status = http_status

    def make_response(self)-> Response:
        response = jsonify(self.payload)
        response.status_code = self.http_status
        return response

@app.errorhandler(404)
def not_found_error(err):
    return ErrorResponse(err.description, 404).make_response()

@app.errorhandler(400)
def not_found_error(err):
    messages = err.data.get('messages', {}).get('json',{})
    return ErrorResponse(messages, 400).make_response()