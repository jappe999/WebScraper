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
    newDirectory = ""

    for i in range(len(directory) - 1):
        newDirectory += directory[i]
        if directory[i:i+1] == "./" or directory[i:i+1] == " /":
              newDirectory += "ß"
    
    if directory[len(directory) - 1] == '.' or directory[len(directory) - 1] == ' ':
        newDirectory += 'ß'

    createFolder(newDirectory)

    file = 'index.html'
    with open(newDirectory + '/' + file, 'w+') as f:
        f.write(str(html))
        f.close()

