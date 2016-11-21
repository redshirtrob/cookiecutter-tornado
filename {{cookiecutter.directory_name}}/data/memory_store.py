from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_
from tornado import gen

from .core import Base
from .models import {{cookiecutter.model_name}}Model

ENGINE = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=ENGINE)

Base.metadata.create_all(ENGINE)

class MemoryStore(object):
    def __init__(self):
        self.session = Session()

    @gen.coroutine
    def create_{{cookiecutter.model_name.lower()}}(self, dct):
        """Create an {{cookiecutter.model_name.lower()}}"""
        
        {{cookiecutter.model_name.lower()}} = {{cookiecutter.model_name}}Model.from_dict(dct)
        self.session.add({{cookiecutter.model_name.lower()}})
        self.session.commit()
        raise gen.Return()

    @gen.coroutine
    def get_{{cookiecutter.model_name.lower()}}s(self):
        """Get all {{cookiecutter.model_name.lower()}}s"""
        
        {{cookiecutter.model_name.lower()}}s = self.session.query({{cookiecutter.model_name}}Model).all()
        if {{cookiecutter.model_name.lower()}}s is not None:
            raise gen.Return([e.to_dict() for e in {{cookiecutter.model_name.lower()}}s])

    @gen.coroutine
    def get_{{cookiecutter.model_name.lower()}}_by_id(self, {{cookiecutter.model_name.lower()}}_id):
        """Get an {{cookiecutter.model_name.lower()}} by id"""

        {{cookiecutter.model_name.lower()}} = self.session.query({{cookiecutter.model_name}}Model).filter({{cookiecutter.model_name}}Model.id == {{cookiecutter.model_name.lower()}}_id).one_or_none()
        if {{cookiecutter.model_name.lower()}} is not None:
            raise gen.Return({{cookiecutter.model_name.lower()}}.to_dict())
    
