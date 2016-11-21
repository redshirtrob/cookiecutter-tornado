from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, Integer, String

from .core import Base

class {{cookiecutter.model_name}}Model(Base):
    """{{cookiecutter.model_name}} Model"""
    __tablename__ = '{{cookiecutter.model_name.lower()}}'

    id = Column(Integer, primary_key=True)
    key = Column(String)

    @classmethod
    def from_dict(cls, dct):
        return cls(key=dct['key'])

    def to_dict(self):
        dct = super({{cookiecutter.model_name}}Model, self).to_dict()
        dct['key'] = self.key
        return dct
    
    def __repr__(self):
        return "<{{cookiecutter.model_name}}Model({} {})>".format(self.id, self.key)
