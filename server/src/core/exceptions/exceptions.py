from fastapi import HTTPException, status


class BadRequest(HTTPException):
    def __init__(self, detail: str = 'Bad Request') -> None:
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)


class Unauthorized(HTTPException):
    def __init__(self, detail: str = 'Unauthorized Request') -> None:
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class Forbidden(HTTPException):
    def __init__(self, detail: str = 'Forbidden Request') -> None:
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, detail=detail)


class NotFound(HTTPException):
    def __init__(self, detail: str = 'Not Found') -> None:
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class UnprocessableEntity(HTTPException):
    def __init__(self, detail: str = 'Unprocessable Entity') -> None:
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=detail
        )


class InternalServerError(HTTPException):
    def __init__(self, detail: str = 'Internal Server Error') -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail
        )
