from bs4 import BeautifulSoup
import os, requests, re

def getMeta(page): #get meta from website
    soup            = BeautifulSoup(page, 'html5lib')
    desc, og, keys  = '', '', ''

    try:
        desc  = soup.findAll(attrs={"name":"description"})
        og    = soup.findAll(attrs={"property":"og:description"})
        keys  = soup.findAll(attrs={"name":"keywords"})
        title = soup.title
    except:
        pass

    meta  = (desc, keys, og, title)
    return str(meta)

def getContents(page): #get content from website
    content = False
    try:
        page = page.encode('utf-8')
    except Exception as e:
        pass # No need to print this error, because that's useless

    try:
        soup = BeautifulSoup(page, 'html5lib')

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
    except Exception as e:
        print(e)
        return False

def setData(html, url, data_type='Content'):
    directory = 'Data/' + data_type + '/' + re.sub('^(http://|https://)(www\.)?', '', url)
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
