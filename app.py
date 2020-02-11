import pyodbc
from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from config import WebConfiguration

app = Flask(__name__)

SQL_SERVER_URL =  f"mssql+pyodbc://{WebConfiguration.DB_USER_NAME}:" \
                                        f"{WebConfiguration.DB_PASSWORD}@localhost:1433/" \
                                        f"{WebConfiguration.DB_NAME}?driver={WebConfiguration.DRIVER}"

app.config["SQLALCHEMY_DATABASE_URI"] = SQL_SERVER_URL

db = SQLAlchemy(app)
api = Api(app)


class Products(Resource):
    def get(self):
        return {'books_count': 25}

    def post(self):
        json = request.get_json()
        return {'you_sent': json}

class Users(Resource):
    def get(self, num):
        return {'result': num*10}

api.add_resource(Users, '/user/<int:num>')
api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.run(debug=True)