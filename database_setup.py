import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


event_source_table = Table('eventsource', Base.metadata,
    Column('event_id', Integer, ForeignKey('event.id')),
    Column('source _id', Integer, ForeignKey('source.id'))
)

event_tag_table = Table('eventtag', Base.metadata,
    Column('event_id', Integer, ForeignKey('event.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)
suggestedevent_source_table = Table('suggestedeventsource', Base.metadata,
    Column('suggestedevent_id', Integer, ForeignKey('suggestedevent.id')),
    Column('source _id', Integer, ForeignKey('source.id'))
)

suggestedevent_tag_table = Table('suggestedeventtag', Base.metadata,
    Column('suggestedevent_id', Integer, ForeignKey('suggestedevent.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

resource_tag_table = Table('resourcetag', Base.metadata,
    Column('resource_id', Integer, ForeignKey('resource.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

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
    tags = relationship("Tag",
                    secondary=event_tag_table,
                    backref="events")
    sources = relationship("Source",
                    secondary=event_source_table,
                    backref="events")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'date_time': self.date_time,
            'url': self.url,
        }

class SuggestedEvent(Base):
    __tablename__ = 'suggestedevent'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String)
    description = Column(String(250))
    date_time = Column(Integer)
    tags = relationship("Tag",
                    secondary=suggestedevent_tag_table,
                    backref="suggestedevents")
    sources = relationship("Source",
                    secondary=suggestedevent_source_table,
                    backref="suggestedevents")

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'date_time': self.date_time,
            'url': self.url,
        }

class Resource(Base):
    __tablename__ = 'resource'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    description = Column(String)
    tags = relationship("Tag",
                    secondary=resource_tag_table,
                    backref="resources")
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'url': self.url,
            'description': self.description,
        }


engine = create_engine('sqlite:///Westernevents.db')


Base.metadata.create_all(engine)
