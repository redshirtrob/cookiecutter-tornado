import json
import tornado.web
from tornado import gen

from data.memory_store import MemoryStore

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


class ExampleHandler(BaseHandler):

    SUPPORTED_METHODS = ('GET', 'POST', 'OPTIONS')

    @gen.coroutine
    def get(self, example_id=None):
        if example_id is None:
            result = yield self.application.store.get_examples()
        else:
            result = yield self.application.store.get_example_by_id(example_id)
        self.write(json.dumps(result))
        self.finish()

    @gen.coroutine
    def post(self):
        self.application.store.create_example(json.loads(self.request.body))
        self.finish()
