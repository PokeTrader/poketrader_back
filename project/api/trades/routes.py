from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required, get_jwt_identity

from marshmallow.exceptions import ValidationError


from .schemas import TradeFairnessSchema, TradeSchema
from .services.fairness import calculate_fairness
from .services.trades import save_trade

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


@trades_blueprint.route('/api/trades', methods=['POST'])
@jwt_required
def post_trade():
    schema = TradeSchema()

    trade_data = request.get_json()

    try:
        trade_params = schema.load(trade_data)
    except ValidationError as e:
        return jsonify({'errors': e.normalized_messages()}), 400

    username = get_jwt_identity()
    trade = save_trade(trade_params, username)

    return jsonify({'success': True, 'id': trade.id}), 201


@trades_blueprint.route('/api/trades', methods=['GET'])
def get_trades():
    return jsonify({}), 200


@trades_blueprint.route('/api/trades/<id>', methods=['GET'])
def get_trade_by_id(id):
    return jsonify({}), 200