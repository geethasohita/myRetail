from flask import jsonify

from app import app


class MyRetailError(Exception):
    pass


class BadRequestException(MyRetailError):
    code = 400
    description = 'Bad Request'


@app.errorhandler(MyRetailError)
def handle_exception(err):
    response = {'error': err.description, 'message': ''}
    if len(err.args) > 0:
        response['message'] = err.args[0]
    return jsonify(response), err.code


@app.errorhandler(500)
def handle_500exception(err):
    response = {'error': 'Unknown error', 'message': 'Unknown error. Please contact the administrator.'}
    return jsonify(response), 500
