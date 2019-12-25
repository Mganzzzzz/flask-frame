from flask import jsonify, json, request
from enum import Enum
from werkzeug.exceptions import HTTPException
from utils.utils import log

class RestException(HTTPException):
    code = 200
    status_code = 500
    payload = None
    path = '/'
    message = '未知错误'
    response = None

    def __init__(self, message=None, status_code=None, payload=None):
        if status_code is not None:
            self.status_code = status_code
        if message is not None:
            self.message = message
        self.payload = payload
        self.path = self.get_path()
        super(RestException, self).__init__(message, None)

    def get_body(self, environ=None):
        body = dict(
            code=self.status_code,
            message=self.message,
            data=self.payload,
            path=self.path,
        )
        if isinstance(body['code'], Enum):
            body['code'] = body['code'].value
        return json.dumps(body)

    def get_headers(self, environ=None):
        return [("Content-Type", "application/json")]

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message

        return rv
    def get_path(self):
        method = request.method
        full_path = request.full_path
        return '{}  {}'.format(method, full_path.split('?')[0])
