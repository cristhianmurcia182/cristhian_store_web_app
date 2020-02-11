import pyodbc
from flask import Flask, request
from flask_restful import Resource, Api
from config import app, api
from logic import ClientsLogic, ProductsLogic, ReceiptsLogic

from serializers import ClientSchema


class Clients(Resource):
    def get(self):
        data = ClientsLogic.get_all_clients()
        clients = ClientSchema(many=True).dump(data)
        return clients

    def post(self):
        json = request.get_json()
        return {'you_sent': json}

class Products(Resource):
    def get(self, num):
        return {'result': num*10}

api.add_resource(Clients, '/clients')

api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.run(debug=True)