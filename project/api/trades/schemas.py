from project import ma
from marshmallow import fields
from marshmallow import validate
from marshmallow import EXCLUDE


class TradeFairnessSchema(ma.Schema):
    group_one_exp = fields.Integer(required=True, validate=[validate.Range(min=1)])
    group_two_exp = fields.Integer(required=True, validate=[validate.Range(min=1)])


class TradePokemonSchema(ma.Schema):
    name = fields.Str(required=True)
    sprite_url = fields.Str(data_key='sprite')

    class Meta:
        unknown = EXCLUDE

class TradeGroupSchema(ma.Schema):
    was_benefitted = fields.Boolean(data_key='wasBenefitted')
    pokemons = fields.List(fields.Nested(TradePokemonSchema))

class TradeSchema(ma.Schema):
    is_fair = fields.Boolean(data_key='isFair')
    trade_groups = fields.List(
        fields.Nested(TradeGroupSchema),
        data_key='tradeGroups',
        validate=[validate.Length(equal=2)]
    )
