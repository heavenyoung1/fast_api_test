import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        pass # Этот метод выполняется перед каждым тестом 

    def test_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World!"}

    def test_read_home(self):
        response = client.get("/home")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])

        # Дополнительные проверки на содержание HTML
        content = response.content.decode("utf-8")
        self.assertIn("Other Noteworthy Projects", content)
        self.assertIn("skills", content)
        self.assertIn("projects", content)

    def test_create_job(self):
        job_data = {
            "name": "string",
            "position": "string",
            "link_job": "string",
            "period": "string",
            "function": [
                "string"
            ],
            "id": 5
        }
        response = client.post("/jobs", json=job_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], job_data["name"])


        

    def tearDown(self) -> None:
        pass # Этот метод выполняется после каждого теста

if __name__ == '__main__':
    unittest.main()

    