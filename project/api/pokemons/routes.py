from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required

from .services import fetch_pokemon

pokemons_blueprint = Blueprint('pokemons', __name__)


@pokemons_blueprint.route('/api/pokemons/<name>')
@jwt_required
def get_pokemon_info(name):
    pokemon_data = fetch_pokemon(name)
    if pokemon_data:
        return jsonify({'pokemon': pokemon_data}), 200
    return jsonify({'errors': 'Pokémon not found'}), 404
