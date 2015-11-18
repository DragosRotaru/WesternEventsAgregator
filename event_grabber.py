import requests
from bs4 import BeautifulSoup, SoupStrainer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Source, Event

engine = create_engine('sqlite:///Westernevents.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

def htmlGrabber(URL):
    r = requests.get(URL)
    r.raise_for_status()
    return r.text

# Parse faculty of mathematics calendar and add to database (http://www.math.uwo.ca/calendar/month.php?getgate=yyyymmdd)
def mathcalparser(yyyymmdd):
    mathevents = []
    urlstring = 'http://www.math.uwo.ca/calendar/month.php?getdate=' + yyyymmdd
    onlytr = SoupStrainer("tr")
    soup = BeautifulSoup(htmlGrabber(string), 'html.parser', parse_only = onlytr)



source1 = source(name="Faculty of Mathematics calendar", url="http://www.math.uwo.ca/calendar/month.php" )
session.add(source1)
session.commit()

event1 = event(name="Root Beer", description="16oz of refreshing goodness",
                     date_time="$1.99", link="Beverage", source=source1)

session.add(event1)
session.commit()
