import unittest

from app import app


class BaseAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
