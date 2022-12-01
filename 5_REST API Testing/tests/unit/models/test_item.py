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

    # done as integration test; instead of
    # unit testing with database mocking
    # def test_find_by_name(self):
    #    pass

    # def test_save_to_db(self):
    #    pass

    # def test_delete_from_db(self):
    #    pass
