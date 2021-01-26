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

    def to_json(self, full=False):
        if full:
            return {
                'id': self.id,
                'isFair': self.is_fair,
                'groups': [group.to_json() for group in self.trade_groups]
            }

        return {
            'id': self.id,
            'isFair': self.is_fair,
            'groups': [len(group.pokemons) for group in self.trade_groups]
        }


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

    def to_json(self):
        return {
            'id': self.id,
            'wasBenefitted': self.was_benefitted,
            'pokemons': [pokemon.to_json() for pokemon in self.pokemons]
        }


class TradePokemon(db.Model):
    __tablename__ = "trade_pokemon"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40))
    sprite_url = db.Column(db.String(160))

    trade_group_id = db.Column(db.Integer, db.ForeignKey('trade_group.id'))
    trade_group = db.relationship(
        "TradeGroup",
        cascade="all, delete",
        back_populates="pokemons"
    )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'sprite': self.sprite_url
        }
