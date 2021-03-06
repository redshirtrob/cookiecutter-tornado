import tornado.ioloop

from {{cookiecutter.model_name.lower()}}.server.server import TornadoApp
from {{cookiecutter.model_name.lower()}}.data.memory_store import MemoryStore

PORT=9000

def main(args):
    application = TornadoApp()
    application.store = MemoryStore()
    application.listen(PORT)
    print "Listening on %d" % (PORT)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description="Tornado Template Service")
    args = parser.parse_args()
    main(args)
