import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):

    def test_read_companies(self):
        response = self.client.get("/home")
        self.assertEqual(response.status_code, 200)
        self.assertIn("companies", response.content.decode())


if __name__ == '__main__':
    unittest.main()