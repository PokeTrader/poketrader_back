from project.tests.base import BaseTestCase

class SetupTest(BaseTestCase):
    def test_ping(self):
        response = self.client.get('/api/ping')
        self.assert200(response)
