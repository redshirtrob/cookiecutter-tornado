from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, Integer, String

from .core import Base

class ExampleModel(Base):
    """Example Model"""
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True)
    key = Column(String)

    @classmethod
    def from_dict(cls, dct):
        return cls(key=dct['key'])

    def to_dict(self):
        dct = super(ExampleModel, self).to_dict()
        dct['key'] = self.key
        return dct
    
    def __repr__(self):
        return "<ExampleModel({} {})>".format(self.id, self.key)
