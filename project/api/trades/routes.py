from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required


trades_blueprint = Blueprint('trades', __name__)
