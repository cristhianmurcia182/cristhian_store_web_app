from models import Product, Client, Transaction, Receipt, Provider
from initial_data import client_data, receipts_data, transaction_data, providers_data, products_data
from config import db


class ClientsLogic:
    @classmethod
    def get_all_clients(cls):
        """
        Retrieves all the clients inside the database
        Returns:
            List containing Client instances.
        """
        return Client.query.all()

    @classmethod
    def create(cls, data):
        """
        Creates a Client instance and stores it into the database
        Args:
            data: Dict containing information about the client to be created

        Returns:
            Client instance.
        """
        client = Client(**data)
        db.session.add(client)
        db.session.commit()
        return client


class ProductsLogic:
    @classmethod
    def get_all_products(cls):
        """
        Retrieves all the products inside the database
        Returns:
            List containing Product instances.
        """
        return Product.query.all()

    @classmethod
    def create(cls, data):
        """
        Creates a Product instance and stores it into the database
        Args:
            data: Dict containing information about the client to be created

        Returns:
            Client instance.
        """
        providers = Provider.query.all()
        provider = providers[1] if type(providers) is list and len(providers) > 0 else None
        data.update({'provider': provider})
        # by default all the products will be associated to the "tiendas de 1" provider
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product


class ReceiptsLogic:
    @classmethod
    def get_all_receipts(cls):
        """
        Retrieves all the receipts inside the database
        Returns:
            List containing Receipt instances.
        """
        return Receipt.query.all()


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
