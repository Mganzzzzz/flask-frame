from exception import RestException
from exception.exception_code_enum import ErrorCode

class FormValidFail(RestException):
    messages = ""
    status_code = ErrorCode.InternalServerError
    fields = []

    def __init__(self, errorMsgs=None):
        if errorMsgs is not None:
            self.message = errorMsgs

