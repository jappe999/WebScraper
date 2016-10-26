import requests, json
from threading import Thread
from webPage import webPage
import fileSystem

IP = "http://localhost:420"

def main(ip):
    localQueue = []
    foundedURLs = []
    while True:
        localQueue = getUrlData(foundedURLs, ip)
        foundedURLs = []
        crawler = Crawler(localQueue)
        crawler.crawl(0)


def getUrlData(data, ip):
    data = json.dumps(data)
    doc = requests.post(ip, data)
    return doc.json()

if __name__ == "__main__":
    main(IP)


class Crawler(object):
    def __init__(self, urls):
        self.urls = urls
        self.foundedURLs = []

    def crawl():
        while len(urls) > 0:
            t = Thread(taget=self.getPage(self.urls[0]))
            t.deamon = True
            t.start()
            del(self.urls[0])

    def getPage():
        response = webPage.getPage(url) # ... get pageresponse,...
        if not (response == None):
            domain = webPage.getDomain(url) # ... get domain from that repsonse...
            anchors = webPage.getAnchors(domain, response) # ... and get hrefs from the response
            for anchor in anchors: # Repeat the crawl function for every anchor
                if anchor[0] not in (self.foundedURLs): # If the anchor is already in the database, ignore it
                    self.foundedURLs.append(anchor[0])



