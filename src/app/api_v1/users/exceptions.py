from fastapi import HTTPException, status


class UserError(HTTPException):
    status_code = 400
    detail = "Bad Request"
    def __init__(
        self,
        status_code=None,
        detail= None,
        headers = None,
    ) -> None:
        super().__init__(
            status_code=status_code or self.status_code, detail=detail or self.detail, headers=headers
        )



class UserNotFoundError(UserError):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User not found"