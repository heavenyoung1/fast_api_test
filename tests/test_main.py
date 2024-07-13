import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):

    def test_read_companies(self):
        response = client.get("/home")
        self.assertEqual(response.status_code, 200)
        # Проверяем, что шаблон возвращает страницу, содержащую список компаний
        self.assertIn("companies", response.text)


if __name__ == '__main__':
    unittest.main()