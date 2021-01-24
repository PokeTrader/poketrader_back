from project import ma
from marshmallow import fields
from marshmallow import validate


class UserRegisterSchema(ma.Schema):
    username = fields.Str(required=True, validate=[validate.Length(min=4, max=80)])
    password = fields.Str(required=True, validate=[validate.Length(min=6)])


class UserSigninSchema(ma.Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
