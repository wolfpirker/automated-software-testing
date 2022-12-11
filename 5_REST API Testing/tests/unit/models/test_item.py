from unittest import TestCase

from models.item import ItemModel


#
class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('choclate', 34)
        self.assertEqual(item.name, 'choclate',
                         "The name of the item after creation does not equal the constructor argument")
        self.assertEqual(item.price, 34,
                         "The price of the item after creation does not equal the constructor argument")

    def test_item_json(self):
        item = ItemModel('choclate', 34)
        expected = {
            'name': 'choclate',
            'price': 34
        }

        self.assertEqual(item.json(), expected,
                         "The JSON export of the item is incorrect. Received {}, expected {}".format(item.json(),
                                                                                                     expected))