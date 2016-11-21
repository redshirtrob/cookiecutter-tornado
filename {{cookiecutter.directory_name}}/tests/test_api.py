from tornado.testing import AsyncHTTPTestCase

from {{cookiecutter.model_name.lower()}}.server.server import TornadoApp
from {{cookiecutter.model_name.lower()}}.data.memory_store import MemoryStore


class Test{{cookiecutter.model_name.upper()}}Api(AsyncHTTPTestCase):
    def get_app(self):
        application = TornadoApp()
        application.store = MemoryStore()
        return application

    def test_get_{{cookiecutter.model_name.lower()}}s(self):
        response = self.fetch('/{{cookiecutter.model_name.lower()}}s/')
        self.assertEqual(response.code, 200)

    def test_post_{{cookiecutter.model_name.lower()}}s(self):
        response = self.fetch(
            '/{{cookiecutter.model_name.lower()}}s/',
            method='POST',
            body='{"key": "value"}'
        )
        self.assertEqual(response.code, 201)
