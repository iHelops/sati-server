from flask import request
import os
import magic
from exceptions import ApiError


def get_file_size(stream):
    size = stream.seek(0, os.SEEK_END)
    stream.seek(0)
    return size


def get_file_ext(stream):
    header = stream.read(1024)
    stream.seek(0)
    file_format = magic.from_buffer(header, mime=True).split('/')
    return file_format[1]


def file_required(extensions: list, max_size: int = 2):
    def _file_required(fn):
        def wrapper(*args, **kwargs):
            try:
                file = request.files['file']
            except KeyError:
                raise ApiError.BadRequest('File not found. Send file in field "file"')

            if get_file_size(file.stream) > max_size * (1024 * 1024):
                raise ApiError.BadRequest(f'File is too big (max size: {max_size}MB)')

            file_ext = get_file_ext(file.stream)
            if not file_ext in extensions:
                raise ApiError.BadRequest('Wrong file type')

            file.headers.add_header('extension', file_ext)

            return fn(file, *args, **kwargs)

        return wrapper

    return _file_required
