from models import Product, Client, Transaction, Receipt, Provider
from initial_data import client_data, receipts_data, transaction_data, providers_data, products_data
from app import db

class DataMigration:
    @classmethod
    def add_data(cls, Instance, data, db):
        instances = []
        for d in data:
            instance = Instance(**d)
            db.session.add(instance)
            instances.append(instance)
        return instances

    @classmethod
    def migrate_initial_data(cls):
        clients = DataMigration.add_data(Client, client_data, db)
        providers = DataMigration.add_data(Provider, providers_data, db)
        [p_d.update({'provider': providers[0]}) for p_d in products_data]
        products = DataMigration.add_data(Product, products_data, db)



DataMigration.migrate_initial_data()
