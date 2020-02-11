from marshmallow import fields
from config import ma


class ClientSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    phone = fields.String(required=True)
    num_doc = fields.String(required=True)


#
#
# class BankSAccountTypeSchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     name = fields.String(required=True)
#
#
# class BankAccSchema(ma.Schema):
#     id = fields.Integer()
#     account_number = fields.String(required=True)
#
#     account_type_id = fields.Integer(required=True, load_only=True)
#     account_type = fields.Nested(BankSAccountTypeSchema, required=True, dump_only=True)
#     bank_id = fields.Integer(required=True, load_only=True)
#     bank = fields.Nested(BankSchema, required=True, dump_only=True)
#     suscribed = fields.Boolean(default=False, data_key='subscribed')