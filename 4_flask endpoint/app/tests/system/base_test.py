from unittest import TestCase
from app.app import app

class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client
        pass