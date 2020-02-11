from flask_marshmallow import Marshmallow
from flask import Flask
from flask_restful import  Api
from flask_sqlalchemy import SQLAlchemy


class WebConfiguration:
    DB_USER_NAME = 'sa'
    DB_NAME = 'store'
    DB_PASSWORD = 'team_international_test*'
    DRIVER = '/usr/local/lib/libmsodbcsql.17.dylib'


app = Flask(__name__)

SQL_SERVER_URL = f"mssql+pyodbc://{WebConfiguration.DB_USER_NAME}:" \
                                        f"{WebConfiguration.DB_PASSWORD}@localhost:1433/" \
                                        f"{WebConfiguration.DB_NAME}?driver={WebConfiguration.DRIVER}"

app.config["SQLALCHEMY_DATABASE_URI"] = SQL_SERVER_URL

db = SQLAlchemy(app)
api = Api(app)

ma = Marshmallow()