import requests
import Event
from bs4 import BeautifulSoup, SoupStrainer

def htmlGrabber(URL):
    r = requests.get(URL)
    r.raise_for_status()
    return r.text

# parser for faculty of mathematics calendar (http://www.math.uwo.ca/calendar/month.php?getgate=yyyymmdd)
def mathcalparser(yyyymmdd):
    mathEvents = []
    urlstring = 'http://www.math.uwo.ca/calendar/month.php?getdate=' + yyyymmdd
    onlytr = SoupStrainer("tr")
    soup = BeautifulSoup(htmlGrabber(string), 'html.parser', parse_only = onlytr)
    
