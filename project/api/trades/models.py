from project import db

class Trade(db.Model):
    __tablename__ = "trade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_fair = db.Column(db.Boolean)

    user_id = db.Column(db.String(80), db.ForeignKey('user.username'))
    user = db.relationship(
        "User",
        cascade="all, delete",
        back_populates="trades"
    )

    trade_groups = db.relationship("TradeGroup", back_populates="trade")


class TradeGroup(db.Model):
    __tablename__ = "trade_group"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    was_benefitted = db.Column(db.Boolean)

    trade_id = db.Column(db.Integer, db.ForeignKey('trade.id'))
    trade = db.relationship(
        "Trade",
        cascade="all, delete",
        back_populates="trade_groups"
    )

    pokemons = db.relationship("TradePokemon", back_populates="trade_group")


class TradePokemon(db.Model):
    __tablename__ = "trade_pokemon"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer)

    trade_group_id = db.Column(db.Integer, db.ForeignKey('trade_group.id'))
    trade_group = db.relationship(
        "TradeGroup",
        cascade="all, delete",
        back_populates="pokemons"
    )
