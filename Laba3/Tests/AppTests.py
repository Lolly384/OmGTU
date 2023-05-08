import unittest
from main import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_convert(self):
        response = self.app.post('/convert', data={
            'amount': '10',
            'from_currency': 'USD',
            'to_currency': 'EUR'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'10 USD =', response.data)
        self.assertIn(b'EUR', response.data)

if __name__ == '__main__':
    unittest.main()