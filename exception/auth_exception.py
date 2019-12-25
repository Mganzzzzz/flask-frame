from exception import RestException
from exception.exception_code import ErrorCode


class AuthLoginFailed(RestException):
    message = "login fail"
    status_code = ErrorCode.AuthFail
