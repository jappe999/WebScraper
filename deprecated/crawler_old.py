#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Queue import Queue
from threading import Thread
from webPage import webPage
from urlparse import urlparse as parser
import sys
webPage = webPage() # Init webPage object

class crawler(object):
    def __init__(self, depth):
        self.depth = depth # Maximum depth of crawling
        self.results = Queue() # Object with all the results from x layers
        self.hrefsVisited = []

    def _scrape(self, url, currentDepth):
        response = webPage._getPage(url)
        if not response == None:
            uri     = parser(url)
            domain  = '{}://{}/'.format(uri.scheme, uri.netloc)
            anchors = webPage._getAnchors(domain, response.text) # Get hrefs from content
            self.results.put(anchors)
            #print anchors
            currentDepth += 1 # currentDepth gets higher so it will stop at the set depth
            for anchor in anchors: # Repeat the crawl function for every anchor, so it discovers new anchors
                if not anchor[0] in self.hrefsVisited:
                    print anchor[0]
                    self.crawl(anchor[0], currentDepth)

    def crawl(self, url, currentDepth=1):
        self.hrefsVisited.append(url)
        print currentDepth, self.depth, url
        if currentDepth < self.depth:
            t = Thread(target=self._scrape(url, currentDepth))
            t.daemon = True
            t.start() # Start Thread
        else:
            self.printResults()
            self.stop()

    def printResults(self):
        pass
        #print self.results.get()

    def stop(self):
        sys.exit()
