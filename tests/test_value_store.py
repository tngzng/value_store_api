import unittest

from app import ValueStore


class TestValueStore(unittest.TestCase):
    def setUp(self):
        self.value_store = ValueStore()

    def test_set_and_get(self):
        self.value_store.set('candace towns', 'oklahoma')
        value = self.value_store.get('candace towns')
        self.assertEqual(value, 'oklahoma')
