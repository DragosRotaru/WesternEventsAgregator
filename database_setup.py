import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Source(Base):
    __tablename__ = 'source'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'url': self.url,
        }

class SuggestedSource(Base):
    __tablename__ = 'suggestedsource'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    notes = Column(String)
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'url': self.url,
            'notes': self.notes
        }

class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String)
    description = Column(String(250))
    date_time = Column(Integer)
    source_id = Column(Integer, ForeignKey('source.id'))
    source = relationship(Source)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'date_time': self.date_time,
            'link': self.link,
        }




engine = create_engine('sqlite:///Westernevents.db')


Base.metadata.create_all(engine)
