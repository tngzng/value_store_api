from tests import base


class TestHealth(base.BaseAPITestCase):
    def test_get(self):
        res = self.client.get('/health')

        self.assertEqual(res.status_code, 200)
