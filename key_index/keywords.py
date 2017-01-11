from bs4 import BeautifulSoup
import html5lib

def getKeywords(blob):
    soup = BeautifulSoup(blob, 'html5lib') # Init BeautifulSoup
    keys = soup.findAll(attrs={"name":"keywords"})
    return keys

def getDescription(blob):
    soup = BeautifulSoup(blob, 'html5lib') # Init BeautifulSoup
    description = soup.findAll(attrs={"name":"description"})
    return description

def getTitle(blob):
    soup = BeautifulSoup(blob, 'html5lib') # Init BeautifulSoup
    title = soup.find('title', text=True)
    return title
