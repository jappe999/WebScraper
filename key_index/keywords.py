from bs4 import BeautifulSoup
import html5lib

def getKeywords(blob):
    soup = BeautifulSoup(blob, 'html5lib') # Init BeautifulSoup
    keys = soup.find(attrs={'id':'mw-content-text'})
    return keys

def getDescription(blob):
    soup = BeautifulSoup(blob, 'html5lib') # Init BeautifulSoup
    subSoup = soup.find(attrs={"id":"mw-content-text"})
    description = subSoup.find('p')
    if description is None:
        description = subSoup.text
    return description

def getTitle(blob):
    soup = BeautifulSoup(blob, 'html5lib') # Init BeautifulSoup
    title = soup.find(attrs={'id':'firstheading'})
    return title.text
