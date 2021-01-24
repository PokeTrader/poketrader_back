from ..models import Trade, TradeGroup, TradePokemon, db


def __save_trade_pokemon(trade_pokemon_data, trade_group_id):
    pokemon = TradePokemon()
    pokemon.name = trade_pokemon_data['name']
    pokemon.sprite_url = trade_pokemon_data.get('sprite_url')
    pokemon.trade_group_id = trade_group_id

    db.session.add(pokemon)


def __save_trade_group(trade_group_data, trade_id):
    trade_group = TradeGroup()
    trade_group.was_benefitted = trade_group_data.get('wasBenefitted')
    trade_group.trade_id = trade_id

    db.session.add(trade_group)
    db.session.flush()

    for pokemon in trade_group_data['pokemons']:
        __save_trade_pokemon(pokemon, trade_group.id)


def save_trade(trade_data, user_id):
    trade = Trade()
    trade.is_fair = trade_data['is_fair']
    trade.user_id = user_id

    db.session.add(trade)
    db.session.flush()

    for trade_group in trade_data['trade_groups']:
        __save_trade_group(trade_group, trade.id)
    
    db.session.commit()
    return trade


