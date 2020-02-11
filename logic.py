from models import Product, Client, Transaction, Receipt, Provider
from initial_data import client_data, receipts_data, transaction_data, providers_data, products_data
from config import db


class DataMigration:
    @classmethod
    def add_data(cls, Instance, data, db):
        """
        Adds instances to the current session.
        Args:
            Instance: Instance to be added.
            data: Dict containing information about the instance.
            db: SqchAlchemy database connection.

        Returns:
            List containing the added instances.
        """
        instances = []
        for d in data:
            instance = Instance(**d)
            db.session.add(instance)
            instances.append(instance)
        return instances

    @classmethod
    def migrate_initial_data(cls):
        """
        Populates the database with dummy data.
        Returns:
            None
        """
        clients = DataMigration.add_data(Client, client_data, db)
        providers = DataMigration.add_data(Provider, providers_data, db)
        [p_d.update({'provider': providers[0]}) for p_d in products_data]
        products = DataMigration.add_data(Product, products_data, db)
        [p_d.update({'client': clients[0]}) for p_d in receipts_data]
        receipts = DataMigration.add_data(Receipt, receipts_data, db)
        [p_d.update({'product': products[0], 'receipt': receipts[0]}) for p_d in transaction_data]
        DataMigration.add_data(Transaction, transaction_data, db)

        db.session.commit()


class ClientsLogic:
    @classmethod
    def get_all_clients(self):
        return Client.query.all()


class ProductsLogic:
    @classmethod
    def get_all_products(self):
        return Product.query.all()


class ReceiptsLogic:
    @classmethod
    def get_all_receipts(self):
        return Receipt.query.all()


