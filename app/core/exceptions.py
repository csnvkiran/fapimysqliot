class EntityInfoException(Exception):
    ...


class EntityInfoNotFoundError(EntityInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Entity Info Not Found"


class EntityInfoInfoAlreadyExistError(EntityInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Entity Info Already Exists"
