import requests, json
from threading import Thread
from webPage import webPage

IP = "http://localhost:420"

class Crawler(object):
    def __init__(self, urls):
        self.urls = urls
        self.foundedURLs = []
        self.threads = []

    def crawl(self):
        while len(self.urls) > 0:
            t = Thread(target=self.getPage(self.urls[0]))
            t.deamon = True
            t.start()
            self.threads.append(t)
            del(self.urls[0])

    def getPage(self, url):
        page = webPage(url)
        response = page.getPage() # ... get pageresponse,...
        if not (response == None):
            anchors = page.getAnchors() # ... and get hrefs from the response
            for anchor in anchors: # Repeat the crawl function for every anchor
                if anchor[0] not in (self.foundedURLs): # If the anchor is already in the database, ignore it
                    self.foundedURLs.append(anchor[0])

def main(ip):
    localQueue = []
    foundedURLs = ['HTTP://DMOZ.ORG/']
    foundedURLs = list(range(30))
    while True:
        #try:
        localQueue = getUrlData(foundedURLs, ip)
        break
        foundedURLs = []
            #print(localQueue)
        crawler = Crawler(localQueue)
        crawler.crawl()
        while True:
            if len(crawler.threads) < 1:
                break
            for i in range(len(crawler.threads)):
                if not crawler.threads[i].isAlive():
                    del(crawler.threads[i])
                    break
        #foundedURLs = crawler.foundedURLs
        #except Exception as e:
            #pass#print(e)

def getUrlData(data, ip):
    try:
        chunks = []
        while len(data) > 20:
            chunks.append(data[:20])
            del(data[:20])

            for chunk in chunks:
                postData = json.dumps(chunk)
                requests.post(ip, postData)

            postData = json.dumps(data)
            doc = requests.post(ip + "/get", postData)
            urls = doc.json()

        return urls
    except Exception as e:
        print("error 2: " + str(e))

if __name__ == "__main__":
    main(IP)
