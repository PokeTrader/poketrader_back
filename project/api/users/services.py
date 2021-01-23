from flask_bcrypt import generate_password_hash

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
