from ..models import Trade, TradeGroup, TradePokemon, db


def __save_trade_pokemon(trade_pokemon_data, trade_group_id):
    pokemon = TradePokemon()
    pokemon.name = trade_pokemon_data['name']
    pokemon.sprite_url = trade_pokemon_data.get('sprite_url')
    pokemon.trade_group_id = trade_group_id

    db.session.add(pokemon)


def __save_trade_group(trade_group_data, trade_id):
    print(trade_group_data)
    trade_group = TradeGroup()
    trade_group.was_benefitted = trade_group_data.get('was_benefitted')
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

def fetch_trades_by_user(user_id):
    trades = Trade.query.filter_by(user_id=user_id).order_by(Trade.id.desc()).all()
    return [trade.to_json() for trade in trades]


def fetch_trade_by_id(trade_id, user_id):
    trade = Trade.query.filter_by(user_id=user_id, id=trade_id).first()
    if trade:
        return trade.to_json(full=True)
    return None