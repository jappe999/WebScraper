from bs4 import BeautifulSoup
import os, requests, re
"""
class FileSystemConnection(object):
    \"""docstring for .\"""
    def __init__(self):
        pass
"""
def getMeta(url): #get meta from website
    response = requests.get(url)
    if response.status_code != 404:
        page        = response.text.encode('utf-8')
        soup        = BeautifulSoup(page, 'html5lib')
        desc, keys  = '', ''

        try:
            desc = soup.findAll(attrs={"name":"description"})
            og   = soup.findAll(attrs={"property": "og:description"})
            keys = soup.findAll(attrs={"name":"keywords"})
        except:
            pass
        
        title = soup.title
        meta  = (desc, keys, og, title)
        return str(meta)

def getContents(url): #get content from website
    content = False
    try:
        response = requests.get(url)
        if response.status_code != 404:
            page     = response.text.encode('utf-8')
            soup     = BeautifulSoup(page, 'html5lib')

            # kill all script and style elements
            for script in soup(["script", "style"]):
                script.extract()

            text = soup.get_text()
            text = '\n'.join(chunk for chunk in text if chunk)

            content = text.encode('utf-8')
    except UnicodeEncodeError:
        pass
    finally:
        return str(content)

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return True
    except:
        return False

def setData(html, url, data_type='Content'):
    directory = 'Data/' + data_type + '/' + re.sub('^(http://|https://|www\.)', '', url)
    createFolder(directory)
    page = trimPage(html)
    file = 'main.meta' if data_type == 'Meta' else 'main.txt'
    with open(directory + '/' + file, 'w+') as f:
        f.write(page)
        f.close()

def trimPage(page):
    trimmedPage = page.replace('\\n', '').replace('\\t', '')
    trimmedPage = re.sub('[\s]{2,}', '', trimmedPage)
    return trimmedPage

"""
u = 'http://dmoz.com//Games/Video_Games'
c = getContents(u)
m = getMeta(u)
setData(m, u, 'Meta')
setData(c, u, 'Content')
"""
