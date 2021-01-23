from flask import Blueprint
from flask import jsonify
from flask import request

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError

from marshmallow.exceptions import ValidationError

from project import db
from .models import User
from .schemas import UserRegisterSchema
from .services import create_user


users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/api/users/register', methods=['POST'])
def post_register():
    post_data = request.get_json()
    schema = UserRegisterSchema()

    try:
        user = schema.load(post_data.get('user'))
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400
    
    try:
        create_user(post_data.get('user'))
    except (IntegrityError, FlushError) as e:
        return jsonify({'errors': 'Username already exists.'}), 400
    

    return jsonify({'success': True}), 201
