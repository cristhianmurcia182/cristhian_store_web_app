from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Provider(db.Model):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    unitary_cost = db.Column(db.Float(53))
    provider_id = db.Column(db.ForeignKey('providers.id'), index=True)

    provider = db.relationship('Provider', backref='product')

    def __init__(self, name, unitary_cost, provider=None):
        self.name = name
        self.unitary_cost = unitary_cost
        self.provider = provider




class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    num_doc = db.Column(db.String(255), nullable=False)

    def __init__(self, name, phone, num_doc):
        self.name = name
        self.phone = phone
        self.num_doc = num_doc


class Receipt(db.Model):
    __tablename__ = 'receipts'

    id = db.Column(db.Integer, primary_key=True)
    voucher = db.Column(db.String(255))
    detail = db.Column(db.Text)
    money_amount = db.Column(db.Float(53))
    taxes = db.Column(db.Float(53))
    total_money_amount = db.Column(db.Float(53))
    client_id = db.Column(db.ForeignKey('clients.id'), index=True)

    client = db.relationship('Client', backref='receipt')

    def __init__(self, voucher, detail, money_amount, taxes, client = None):
        self.voucher = voucher
        self.detail = detail
        self.money_amount = money_amount
        self.taxes = taxes
        self.client = client
        self.total_money_amount = money_amount - money_amount*taxes


class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    product_quantity = db.Column(db.Integer)
    money_amount = db.Column(db.Float(53))
    receipt_id = db.Column(db.ForeignKey('receipts.id'), index=True)
    product_id = db.Column(db.ForeignKey('products.id'), index=True)

    product = db.relationship('Product')
    receipt = db.relationship('Receipt')

    def __init__(self, product_quantity, money_amount, receipt = None, product = None):
        self.product_quantity = product_quantity
        self.receipt = receipt
        self.money_amount = money_amount
        self.product = product


if __name__ == '__main__':
    manager.run()

