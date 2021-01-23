from flask_bcrypt import check_password_hash
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token

from project import db
from .models import User

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError


def create_user(user_schema):
    user = User()
    user.username = user_schema['username']
    user.password = user_schema['password']
    user.password = generate_password_hash(user.password).decode('utf-8')

    db.session.add(user)

    try:
        db.session.commit()
    except (IntegrityError, FlushError) as e:
        db.session.rollback()
        raise e


def valid_credentials(user_schema):
    user = User.query.filter_by(username=user_schema['username']).first()
    return user and check_password_hash(user.password, user_schema['password'])


def authenticate(user_schema):
    if not valid_credentials(user_schema):
        return None

    return create_access_token(identity=user_schema['username'])