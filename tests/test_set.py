import json

from app import value_store
from tests import base


class TestSet(base.BaseAPITestCase):
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
