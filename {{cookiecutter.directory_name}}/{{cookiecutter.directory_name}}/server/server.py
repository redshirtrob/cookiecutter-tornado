import tornado.web

from .handlers import {{cookiecutter.model_name}}Handler

class TornadoApp(tornado.web.Application):
    def __init__(self):
        routes = [
            (r'/{{cookiecutter.model_name.lower()}}s[/]?', {{cookiecutter.model_name}}Handler),
            (r'/{{cookiecutter.model_name.lower()}}s/(\d*)[/]?', {{cookiecutter.model_name}}Handler),
        ]
        settings = { 'debug': True }
        tornado.web.Application.__init__(self, routes, **settings)
