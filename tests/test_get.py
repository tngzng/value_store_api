import json

from app import value_store
from tests import base


class TestGet(base.BaseAPITestCase):
    def test_get__missing_keys_parameter(self):
        res = self.client.get('/get')

        self.assertEqual(res.status_code, 404)

    def test_get(self):
        value_store.set('candace towns', 'oklahoma')
        value_store.set('breyanna stevenson', 'georgia')
        res = self.client.get('/get?keys=candace towns,breyanna stevenson')
        json_res = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(json_res['candace towns'], 'oklahoma')
        self.assertEqual(json_res['breyanna stevenson'], 'georgia')
