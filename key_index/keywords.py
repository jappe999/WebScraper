from bs4 import BeautifulSoup
import html5lib
import re

def get_keywords():
    f = open("main.meta","r" )
    c = f.read()
    soup = BeautifulSoup(c, "html5lib")
    tags = soup.findAll(attrs={"name":re.compile("(og:)?keywords")})
    keys = []
    for lel in tags:
        keys.append(lel["content"].split(','))
    f.close()
    return keys


def get_title():
    f = open("main.meta","r" )
    c = f.read()
    soup = BeautifulSoup(c, "html5lib")
    title = soup.title.get_text()
    return title
