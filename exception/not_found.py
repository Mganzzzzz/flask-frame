from exception import RestException
from werkzeug.exceptions import HTTPException
from exception.auth_exception import AuthLoginFailed
from exception.exception_code import ErrorCode
from utils.utils import log


class NotFound(RestException):
    message = "resorce not found"
    status_code = ErrorCode.NotFound


if __name__ == '__main__':
    e = AuthLoginFailed()
    log(isinstance(e, HTTPException))
    log(isinstance(e, RestException))

