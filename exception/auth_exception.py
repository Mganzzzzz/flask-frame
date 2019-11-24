from exception import RestException
from exception.exception_code_enum import ErrorCode


class AuthLoginFailed(RestException):
    message = "not login"
    status_code = ErrorCode.AuthFail
