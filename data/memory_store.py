from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from tornado import gen

from .core import Base
from .models import ExampleModel

ENGINE = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=ENGINE)

Base.metadata.create_all(ENGINE)

class MemoryStore(object):
    def __init__(self):
        self.session = Session()

    @gen.coroutine
    def create_example(self, dct):
        """Create an example"""
        
        example = ExampleModel.from_dict(dct)
        self.session.add(example)
        self.session.commit()
        raise gen.Return()

    @gen.coroutine
    def get_examples(self):
        """Get all examples"""
        
        examples = self.session.query(ExampleModel).all()
        if examples is not None:
            raise gen.Return([e.to_dict() for e in examples])

    @gen.coroutine
    def get_example_by_id(self, example_id):
        """Get an example by id"""

        example = self.session.query(ExampleModel).filter(ExampleModel.id == example_id).one_or_none()
        if example is not None:
            raise gen.Return(example.to_dict())
    
