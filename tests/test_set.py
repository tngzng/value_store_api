import unittest
import json

from app import app
from app import value_store


class TestSet(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_set__no_parameters(self):
        res = self.client.get('/set')
        json_res = json.loads(res.data)

        self.assertEqual(json_res['count'], 0)

    def test_set__multiple_parameters(self):
        res = self.client.get('/set?candace towns=oklahoma&breyanna stevenson=georgia')
        json_res = json.loads(res.data)

        self.assertEqual(json_res['count'], 2)
        self.assertEqual(value_store.get('candace towns'), 'oklahoma')
        self.assertEqual(value_store.get('breyanna stevenson'), 'georgia')
