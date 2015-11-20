from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Source, Event

engine = create_engine('sqlite:///Westernevents.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
print("0-print 1-edit 2-add 3-remove")
inputcommand = input("what would you like to do: ")

if inputcommand == 0 or inputcommand == 1 or inputcommand == 3:
    sources = session.query(Source).all()
    for i in sources:
        print(i+":")
        print("\n"+i.id)
        print("\n"+i.name)
        print("\n"+i.url+"\n")
    if inputcommand == 3:
        delnum = input("which source would you like to remove (type number)?")
        print("\n"+sources[delnum].id)
        print("\n"+sources[delnum].name)
        print("\n"+sources[delnum].url+"\n")
        if input("are you sure (type 'yes' for yes)?") is "yes":
            session.delete(sources[delnum])
    """ifinputcommand == 1:
        editnum = input("which source would you like to edit (type number)?")
        print("\n"+sources[editnum].name"\n")
        print(sources[editnum].url+"\n")
        inputname = input('Enter new source name in brackets: ')
        inputurl = input('Enter URL in brackets: ')
        print("new name:"+ inputname+"\n")
        print("new url:"+ inputurl+"\n")
        if input("proceed (type 'yes' to confirm)?") == "yes":
    """

if inputcommand is "2":
    inputname = input('Enter source name: ')
    inputurl = input('Enter URL: ')
    source = Source(name= inputname, url= inputurl )
    session.add(source)
    session.commit()

session.close()
