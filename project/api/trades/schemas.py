from project import ma
from marshmallow import fields
from marshmallow import validate


class TradeFairnessSchema(ma.Schema):
    group_one_exp = fields.Integer(required=True, validate=[validate.Range(min=1)])
    group_two_exp = fields.Integer(required=True, validate=[validate.Range(min=1)])
