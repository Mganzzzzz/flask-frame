from exception import RestException
from exception.exception_code import ErrorCode


class ServerException(RestException):
    message = "server internal error"
    status_code = ErrorCode.InternalServerError
