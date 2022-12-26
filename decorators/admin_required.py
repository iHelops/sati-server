from exceptions import ApiError


def admin_required(fn):
    def wrapper(user, *args, **kwargs):
        if user.role != 'admin':
            raise ApiError.Forbidden()

        return fn(user, *args, **kwargs)

    return wrapper
