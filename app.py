from flask import Flask, request
from flask_restful import Resource, Api
from config import app, api
from logic import ClientsLogic, ProductsLogic, ReceiptsLogic

from serializers import ClientSchema, ProductSchema, ReceiptSchema


class Clients(Resource):
    def get(self):
        data = ClientsLogic.get_all_clients()
        clients = ClientSchema(many=True).dump(data)
        return clients, 200

    def post(self):
        data = request.get_json()

        client = ClientsLogic.create(data)

        if client:
            client = ClientSchema().dump(client)

        return client, 201


class Products(Resource):
    def get(self):
        data = ProductsLogic.get_all_products()
        products = ProductSchema(many=True).dump(data)
        return products, 200

    def post(self):
        data = request.get_json()
        product = ProductsLogic.create(data)

        if product:
            product = ProductSchema().dump(product)

        return product, 201


class Receipts(Resource):
    def get(self):
        data = ReceiptsLogic.get_all_receipts()
        receipts = ReceiptSchema(many=True).dump(data)
        return receipts, 200


api.add_resource(Clients, '/clients')

api.add_resource(Products, '/products')

api.add_resource(Receipts, '/receipts')

if __name__ == '__main__':
    app.run(debug=True)