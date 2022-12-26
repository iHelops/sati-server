class ApiError(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status


def BadRequest(message):
    return ApiError(message, 400)


def UnauthorizedError():
    return ApiError('User is not authorized', 401)


def FileNotFound():
    return ApiError('File not found', 404)


def Forbidden():
    return ApiError('Forbidden', 403)
