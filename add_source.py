from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Source, Event

engine = create_engine('sqlite:///Westernevents.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

inputname = input('Enter source name: ')
inputurl = input('Enter URL: ')
source = Source(name= inputname, url= inputurl )
session.add(source)
session.commit()

session.close()
