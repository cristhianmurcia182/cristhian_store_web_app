import unittest
from logic import ClientsLogic, ProductsLogic, ReceiptsLogic
from models import Client, Product


class TestSum(unittest.TestCase):

    def test_client_creation(self):
        body = {"name": "Simon Bolivrl", "phone": "123131", "num_doc":"123123"}
        new_client = ClientsLogic.create(**body)
        self.assertTrue(type(new_client) is Client)

    def test_client_creation(self):
        body = {"name": "chocolatina jet", "unitary_cost": "123131"}
        new_product = ProductsLogic.create(**body)
        self.assertTrue(type(new_product) is Product)

    def test_product_get(self):
        self.assertTrue(type(ProductsLogic.get_all_products()) is list)

    def test_receipts_get(self):
        self.assertTrue(type(ReceiptsLogic.get_all_receipts()) is list)

if __name__ == '__main__':
    unittest.main()