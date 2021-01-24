from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required

from marshmallow.exceptions import ValidationError


from .schemas import TradeFairnessSchema
from .services import calculate_fairness

trades_blueprint = Blueprint('trades', __name__)

@trades_blueprint.route('/api/trades/fairness')
@jwt_required
def get_trade_fairness():
    schema = TradeFairnessSchema()

    params = {
        'group_one_exp': request.args.get('group_one'),
        'group_two_exp': request.args.get('group_two'),
    }

    try:
        trade_params = schema.load(params)
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400

    return jsonify(calculate_fairness(trade_params)), 200
