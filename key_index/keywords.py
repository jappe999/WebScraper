from bs4 import BeautifulSoup
import html5lib
import re

def getKeywords(path):
    f = open(path,"r" )
    c = f.read()
    soup = BeautifulSoup(c, "html5lib")
    tags = soup.findAll(attrs={"name":re.compile("(og:)?keywords")})
    keys = []
    for tag in tags:
        keys.append(tag["content"].split(','))
    f.close()
    return keys


def getTitle():
    f = open("main.meta","r" )
    c = f.read()
    soup = BeautifulSoup(c, "html5lib")
    title = soup.title.get_text()
    return title
