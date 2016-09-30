#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from threading import Thread
from time import sleep

class Crawler(object):
    """docstring for Crawler."""
    def __init__(self, maxSites, seed):
        super(Crawler, self).__init__()
        self.maxSites = maxSites
        self.seed = seed
        if not self.validURL(seed):
            raise Exception("The provided URL is not valid");
        self.queue = [seed]

    def setSeed(self, seed):
        if self.validURL(url):
            self.seed = seed

    def validURL(self, url):
        #TODO: Add checks for validation of URL
        return True

    def crawl(self):
        while self.maxSites > 0:
            try:
                url = self.queue[0]
                del(self.queue[0])
                self.maxSites -= 1

                webpage = WebPage(url)

                t = Thread(target=webpage.addAnchors())
                t.daemon = True
                t.start()
            except Exception as e:
                pass
            sleep(.1)

            #TODO: add db-connection and save HTML
            #print(webpage.getHTML())
            print(self.maxSites)


class WebPage(object):
    """docstring for WebPage."""
    def __init__(self, url, domain = None):
        super(WebPage, self).__init__()
        self.URL = url
        if not domain is None:
            self.domain = domain
        else:
            print(str(self.URL))
            if re.match("^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)", str(self.URL)):
                self.domain = re.search("^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)", str(self.URL)).group(0)

    def getPage(self):
        request = None
        try:
            request = requests.get(self.URL)
        except Exception as e:
            raise
        if(request.status_code == 200):
            self.text = request.text.encode('iso-8859-1', 'replace')
            return request.text
        else:
            return request.status_code

    def getAnchors(self, safeHtml=False):
        text = self.getPage()
        soup = BeautifulSoup(text, 'html.parser')
        results = []

        for link in soup('a'):
            anchor  = []
            try:
                if link.get('href') == None:
                    continue
                href = str(link.get('href'))
                #href = str(link.get('href')).encode('utf-8') if not link.get('href') == None else '#' # Get href out of anchor
                href = re.sub("^[:]?[\/]{2}", "http://", href) # If href starts with :// or // replace it with http://
                href = re.sub("^\/", self.domain, href) # If href starts with a single slash replace it with the domain
                href = re.sub("^\.\/", self.domain, href)
                href = re.sub("^\?", self.domain + "?", href)
            except Exception as e:
                print('Error1: ', e)

            #Try this and otherwise the link is False and won't be put in the DB
            try:
                if link.string == None:
                    text = None
                else:
                    text = link.string
            except UnicodeEncodeError or UnicodeDecodeError:
                # If string isn't encoded in iso 8859-1, ignore it and go next iteration
                continue

            anchor.append(href)
            anchor.append(text)
            results.append(anchor) # Put content in array

        return results

    def addAnchors(self):
        anchers = self.getAnchors()

        #TODO: Test if link is already checked
        for anchor in anchers:
            print(True)
            self.queue.append(anchor[0])

    def getHTML(self):
        if hasattr(self, 'text'):
            return self.text
        else:
            return ""


def main():
    pass

if __name__ == "__main__":
    main()
    webCrawler = Crawler(7600, "http://dmoz.com/")
    webCrawler.crawl()
    #page = WebPage("http://v14ebaalbe.helenparkhurst.net/")
    #print(page.getAnchors())
