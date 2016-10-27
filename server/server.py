import tornado.web

from .handlers import ExampleHandler

class TornadoApp(tornado.web.Application):
    def __init__(self):
        routes = [
            (r'/examples[/]?', ExampleHandler),
            (r'/examples/(\d*)[/]?', ExampleHandler),
        ]
        settings = { 'debug': True }
        tornado.web.Application.__init__(self, routes, **settings)
