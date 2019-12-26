from enum import Enum
import json


class ErrorCode(Enum):
    AuthFail = 101
    NotFound = 102
    InternalServerError = 102
    FormInvalid = 104
    TokenExprie = 105
    TokenError = 106

if __name__ == '__main__':
    code = ErrorCode.NotFound
    print(type(code.value))
