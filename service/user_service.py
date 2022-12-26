from uuid import uuid4
from bson import ObjectId
from exceptions import ApiError
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
import mongoengine
from dtos import UserDto, MinifiedUserDto
from .mail_service import MailService


def registration(email: str, name: str, password: str):
    session = str(uuid4())
    activation_key = str(uuid4())
    user = User(
        email=email,
        name=name,
        password=generate_password_hash(password),
        activation_key=activation_key,
        sessions=[session]
    )

    try:
        user.save()
    except mongoengine.errors.NotUniqueError:
        raise ApiError.BadRequest('email already exist')

    try:
        mail = MailService()
        mail.send_activation_mail(email, activation_key)
    except:
        pass

    user_data = {**UserDto(user).get_dict(), 'session': session}
    return user_data


def login(email: str, password: str):
    user = User.objects(email=email).first()
    if not user or not check_password_hash(user.password, password):
        raise ApiError.BadRequest('wrong login or password')

    session = str(uuid4())
    if len(user.sessions) == 5:
        user.update(pull__sessions=user.sessions[0])

    user.update(push__sessions=session)

    user_data = {**UserDto(user).get_dict(), 'session': session}
    return user_data


def activate(key: str):
    try:
        user = User.objects(activation_key=key).first()
        user.update(activated=True)
    except AttributeError:
        raise ApiError.BadRequest('Incorrect activation link')


def check_auth(session: str):
    try:
        user = User.objects(sessions=session).first()
        user_data = UserDto(user).get_dict()
        return user_data
    except AttributeError:
        raise ApiError.UnauthorizedError()


def subscribe(from_user_id: str, to_user_id: str):
    from_user = User.objects(id=from_user_id).first()
    to_user = User.objects(id=to_user_id).first()

    if not from_user or not to_user:
        raise ApiError.BadRequest('User not found')

    if from_user == to_user:
        raise ApiError.BadRequest('You can\'t follow yourself')

    for user in from_user.subscriptions:
        if str(user.id) == str(to_user.id):
            raise ApiError.BadRequest('You are already following this user')

    from_user.update(push__subscriptions=to_user)
    return MinifiedUserDto(to_user).get_dict()


def unsubscribe(from_user_id: str, to_user_id: str):
    user = User.objects(id=from_user_id, subscriptions=to_user_id).first()
    if not user:
        raise ApiError.BadRequest('You are not following this user')

    user.update(pull__subscriptions=ObjectId(to_user_id))
    user.subscriptions.remove(User(id=to_user_id))


def get_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise ApiError.BadRequest('User not found')

    user = User.objects(id=user_id).first()
    if not user:
        raise ApiError.BadRequest('User not found')

    user_data = {**UserDto(user).get_dict()}
    [user_data.pop(i, None) for i in ['email', 'activated']]
    return user_data


def search(query: str):
    users = User.objects(name__contains=query)
    users_list = [MinifiedUserDto(user).get_dict() for user in users]
    return users_list


def change_avatar(user_id: str, avatar_id: str):
    user = User.objects(id=user_id).first()
    if not user:
        raise ApiError.BadRequest('User not found')

    user.update(avatar=avatar_id)
