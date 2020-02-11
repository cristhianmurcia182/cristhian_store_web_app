from marshmallow import fields, post_dump
from config import ma


class ProviderSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)


class ClientSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    phone = fields.String()
    num_doc = fields.String()


class ProductSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    unitary_cost = fields.Float()
    num_doc = fields.String()
    provider = fields.Nested(ProviderSchema, dump_only=True)

    @post_dump(pass_many=True)
    def post_dump(self, data, **kwargs):
        for elem in data:
            if 'provider' in elem:
                elem['provider_name'] = elem.get('provider', {}).get('name')
                del elem['provider']
        return data


class ReceiptSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    voucher = fields.String()
    detail = fields.String()
    money_amount = fields.Float()
    taxes = fields.Float()
    total_money_amount = fields.Float()

    client = fields.Nested(ClientSchema, dump_only=True)

    @post_dump(pass_many=True)
    def post_dump(self, data, **kwargs):
        for elem in data:
            if 'client' in elem:
                elem['client_name'] = elem.get('client', {}).get('name')
                del elem['client']
        return data


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