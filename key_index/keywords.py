from bs4 import BeautifulSoup
import html5lib

def getKeywords(path):
    text = open(path, 'r+').read().lower()
    soup = BeautifulSoup(text, 'html5lib') # Init BeautifulSoup
    soup.findAll(attrs={"name":"keywords"})

def getDescription(path):
    text = open(path, 'r+').read().lower()
    soup = BeautifulSoup(text, 'html5lib') # Init BeautifulSoup
    soup.findAll(attrs={"name":"description"})

def getTitle(path):
    pass
