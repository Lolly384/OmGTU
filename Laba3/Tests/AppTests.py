import unittest
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_convert1(self):
        response = self.app.post('/convert', data={
            'amount': '10',
            'from_currency': 'EUR',
            'to_currency': 'USD'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'10 EUR =', response.data)
        self.assertIn(b'USD', response.data)

    def test_convert2(self):
        response = self.app.post('/convert', data={
            'amount': '1',
            'from_currency': 'USD',
            'to_currency': 'RUB'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1 USD =', response.data)
        self.assertIn(b'RUB', response.data)

if __name__ == '__main__':
    unittest.main()