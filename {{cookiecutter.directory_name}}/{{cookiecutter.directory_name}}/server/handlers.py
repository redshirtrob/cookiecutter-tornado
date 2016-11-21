import json
import tornado.web
from tornado import gen

from {{cookiecutter.model_name.lower()}}.data.memory_store import MemoryStore

class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header("Access-Control-Allow-Headers",
                        "Content-Type, Depth, User-Agent, X-File-Size, X-Requested-With, X-Requested-By, If-Modified-Since, X-File-Name, Cache-Control")


    def write_error(self, status_code, **kwargs):
        data = {
            'status_code': status_code
        }
        self.write(json.dumps(data))
        self.finish()

    @gen.coroutine
    def options(self):
        self.set_status(204)
        self.finish()


class {{cookiecutter.model_name}}Handler(BaseHandler):

    SUPPORTED_METHODS = ('GET', 'POST', 'OPTIONS')

    @gen.coroutine
    def get(self, {{cookiecutter.model_name.lower()}}_id=None):
        if {{cookiecutter.model_name.lower()}}_id is None:
            result = yield self.application.store.get_{{cookiecutter.model_name.lower()}}s()
        else:
            result = yield self.application.store.get_{{cookiecutter.model_name.lower()}}_by_id({{cookiecutter.model_name.lower()}}_id)
        self.write(json.dumps(result))
        self.finish()

    @gen.coroutine
    def post(self):
        self.application.store.create_{{cookiecutter.model_name.lower()}}(json.loads(self.request.body))
        self.set_status(201)
        self.finish()
