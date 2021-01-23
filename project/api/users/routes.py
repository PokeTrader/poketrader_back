from flask import Blueprint
from flask import jsonify
from flask import request

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError

from marshmallow.exceptions import ValidationError

from project import db
from .models import User
from .schemas import UserRegisterSchema, UserSigninSchema
from .services import create_user, authenticate


users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/api/users/register', methods=['POST'])
def post_register():
    post_data = request.get_json()
    schema = UserRegisterSchema()

    try:
        user_schema = schema.load(post_data.get('user'))
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400

    try:
        create_user(user_schema)
    except (IntegrityError, FlushError) as e:
        return jsonify({'errors': 'Username already exists.'}), 400
    
    token = authenticate(user_schema)
    return jsonify({'success': True, 'token': token}), 201


@users_blueprint.route('/api/users/signin', methods=['POST'])
def post_signin():
    post_data = request.get_json()
    schema = UserSigninSchema()


    try:
        user_schema = schema.load(post_data.get('user'))
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400

    token = authenticate(user_schema)
    if not token:
        return jsonify({'errors': 'Invalid username/password combination'}), 401

    return jsonify({'success': True, 'token': token}), 201
