#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Queue import Queue
from threading import Thread
from webPage import webPage
import sys
webPage = webPage() # Init webPage object

class crawler(object):
    def __init__(self, depth):
        self.depth = depth
        self.currentDepth = 0
        self.results = Queue() # Object with all the results from x layers

    def _scrape(self, url, currentDepth):
        response = webPage._getPage(url)
        if not response == None:
            anchors = webPage._getAnchors(response.text)
            self.results.put(anchors)
            currentDepth += 1 # currentDepth gets higher so it will stop at the set depth
            for anchor in anchors: # Repeat the crawl function for every anchor, so it discovers new anchors
                self.crawl(str(anchor), currentDepth)

    def crawl(self, url, currentDepth=0):
        print currentDepth, self.depth, url
        if currentDepth < self.depth:
            t = Thread(target=self._scrape(url, currentDepth))
            t.daemon = True
            t.start()
        else:
            self.printResults()
            self.stop()

    def printResults(self):
        pass
        #print self.results.get()

    def stop(self):
        sys.exit()
