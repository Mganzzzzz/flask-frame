from exception import RestException
from exception.exception_code import ErrorCode
from utils.utils import log


class FormValidFail(RestException):
    message = ""
    status_code = ErrorCode.FormInvalid

    def __init__(self, errorMsgs=None):
        super().__init__()
        self.message = errorMsgs
