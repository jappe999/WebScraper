import requests, json
from threading import Thread
from webPage import webPage
from fileSystem import *
from urllib.parse import quote

IP = "http://localhost:420"

class Crawler(object):
    def __init__(self, urls):
        self.urls = urls
        self.foundURLs = []
        self.threads = []

    def crawl(self):
        while len(self.urls) > 0:
            t = Thread(target=self.getPage(self.urls[0][0]))
            t.deamon = True
            t.start()
            self.threads.append(t)
            del(self.urls[0])

    # Set page in filesystem
    def setPage(self, url, p):
        u = re.sub('^(http://|https://)(www\.)?', '', url)
        u = quote(u)
        c = getContents(p)
        m = getMeta(p)
        setData(m, u, 'Meta')
        setData(c, u, 'Content')

    def getPage(self, url):
        page = webPage(url)
        response = page.getPage() # ... get pageresponse,...
        try:
            if not response == '':
                self.setPage(url, response)
        except Exception as e:
            print(e)

        if not response == '':
            anchors = page.getAnchors(response) # ... and get hrefs from the response
            for anchor in anchors: # Repeat the crawl function for every anchor
                self.foundURLs.append(anchor[0])

def main(ip):
    localQueue = []
    # Three sources from where to start
    foundURLs = ['http://dmoz.com/']#, 'http://startpagina.nl/', 'http://w3schools.com/']
    while True:
        try:
            localQueue = getUrlData(foundURLs, ip)
            foundURLs = []
            crawler = Crawler(localQueue)
            crawler.crawl()
            while True:
                if len(crawler.threads) < 1:
                    break
                for i in range(len(crawler.threads)):
                    if not crawler.threads[i].isAlive():
                        del(crawler.threads[i])
                        break
            foundURLs = crawler.foundURLs
        except Exception as e:
            print("error 1: " + str(e))

def getUrlData(data, ip):
    try:
        chunks = []
        if len(data) > 20:
            while len(data) > 20:
                chunks.append(data[:20])
                del(data[:20])

        for chunk in chunks:
            postData = json.dumps(chunk)
            requests.post(ip, postData)

        postData = json.dumps(data)
        doc = requests.post(ip + "/get", postData)
        urls = doc.json()
        print(urls)

        return urls
    except Exception as e:
        print("error 2: " + str(e))

if __name__ == "__main__":
    main(IP)
