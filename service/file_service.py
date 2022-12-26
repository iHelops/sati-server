from werkzeug.datastructures import FileStorage
from exceptions import ApiError
from models import File, User
import hashlib
from uuid import uuid4
import os


def get_file_hash(stream):
    sha1sum = hashlib.sha1()

    chunk = stream.read(2 ** 16)
    while len(chunk) != 0:
        sha1sum.update(chunk)
        chunk = stream.read(2 ** 16)

    stream.seek(0)
    return sha1sum.hexdigest()


def upload(user_id: str, file: FileStorage, file_type: str):
    user = User.objects(id=user_id).first()
    if not user:
        raise ApiError.BadRequest('User not found')

    file_hash = get_file_hash(file.stream)
    filename = f'{str(user.id)}_{str(uuid4())}.{file.headers.get("extension")}'

    file_search = File.objects(hash=file_hash).first()
    if file_search:
        return {'file_id': file_hash}

    upload_path = os.environ.get('UPLOAD_PATH')
    file.save(f'{upload_path}/{file_type}/{filename}')

    file = File(
        author=user,
        filename=filename,
        hash=file_hash,
        type=file_type
    )
    file.save()

    return {'file_id': file_hash}


def get_file(file_hash: str):
    file = File.objects(hash=file_hash).first()
    if not file:
        raise ApiError.FileNotFound()

    upload_path = os.environ.get('UPLOAD_PATH')

    file_path = f'{upload_path}/{file.type}/{file.filename}'
    if not os.path.isfile(file_path):
        raise ApiError.FileNotFound()

    file_ext = file_path.split('.')[-1]
    return file_path, file_ext
