from bs4 import BeautifulSoup
import html5lib

def getKeywords(path):
    text = open(path, 'r+').read()
    soup = BeautifulSoup(text, 'html5lib') # Init BeautifulSoup
    for meta in soup('meta'):
        tag = meta.get('name')
        print(tag)

def getTitle(path):
    pass
