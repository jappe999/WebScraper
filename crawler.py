#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Queue import Queue
from threading import Thread
from webPage import webPage
from urlparse import urlparse as parser
from collections import deque
import sys, time
webPage = webPage() # Init webPage object

class crawler(object):
    def __init__(self, depth):
        self.depth = depth # Maximum depth of crawling
        self.currentDepth = 0
        self.unvisitedHrefs = deque()
        self.hrefs = Queue() # Object with all the hrefs from x layers
        self.visitedHrefs = []

    def _scrape(self, url):
        print url
        response = webPage.getPage(url)
        if not response == None:
            domain = webPage.getDomain(url)
            anchors = webPage.getAnchors(domain, response.text) # Get hrefs from content
            for anchor in anchors: # Repeat the crawl function for every anchor, so it discovers new anchors
                if not anchor[0] in self.visitedHrefs:
                    print anchor[0]
                    self.unvisitedHrefs.append(anchor[0])

    def crawl(self, url):
        self.unvisitedHrefs.append(url)
        while self.currentDepth < self.depth:
            self._assignTasks()
            while self.getTasksLeft():
                time.sleep(2)
            print self.currentDepth
            self.currentDepth += 1

    def _assignTasks(self):
        while self.unvisitedHrefs:
            url = self.unvisitedHrefs.popleft()
            self._addToPool(url)
            self.visitedHrefs.append(url)
    def getTasksLeft(self):
        return self.unvisitedHrefs

    def _addToPool(self, url):
        t = Thread(target=self._scrape(url))
        t.daemon = True
        t.start()

    def printResults(self):
        print self.hrefs.get()

    def stop(self):
        sys.exit()
