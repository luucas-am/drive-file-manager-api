from fastapi import HTTPException


class ServerError(Exception):
    def __init__(self, name: str):
        self.name = name


class HTTPInternalException(HTTPException):
    status_code = 500

    def __init__(self, detail: str | None = None):
        if detail is not None:
            self.detail = detail
        super().__init__(status_code=self.status_code, detail=self.detail)


class BadRequestException(HTTPInternalException):
    status_code = 400
    detail = "Invalid Request"


class NotFoundException(HTTPInternalException):
    status_code = 404
    detail = "Not Found"


class UnauthorizedException(HTTPInternalException):
    status_code = 401
    detail = "Not Authorized"