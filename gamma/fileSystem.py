from bs4 import BeautifulSoup
import os, requests, re

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return True
    except Exception as e:
        print(e)
        return False

def setData(html, url):
    directory = 'Data/' + re.sub('^(http://|https://)(www\.)?', '', url)
    createFolder(directory)
    file = 'index.html'
    with open(directory + '/' + file, 'w+') as f:
        f.write(str(html))
        f.close()

