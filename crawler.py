#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from Queue import Queue
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
        self.hrefs = deque() # Object with all the hrefs from x layers
        self.visitedHrefs = []
        self.runs = 0

    def _scrape(self, url):
        response = webPage.getPage(url)
        if not response == None:
            domain = webPage.getDomain(url)
            anchors = webPage.getAnchors(domain, response.text) # Get hrefs from content
            for anchor in anchors: # Repeat the crawl function for every anchor, so it discovers new anchors
                if anchor[0] not in self.visitedHrefs:
                    print anchor[0]
                    self.hrefs.append(anchor[0])

    def crawl(self, url):
        self.unvisitedHrefs.append(url)
        while self.currentDepth < self.depth:
            print '\nLayer: {}'.format(self.currentDepth+1)
            self.runs = 0
            self._assignTasks()
            while self.getTasksLeft():
                time.sleep(2)
            for href in self.hrefs:
                self.unvisitedHrefs.append(href)
            #time.sleep(120)
            self.currentDepth += 1
        self.stop()

    def _assignTasks(self):
        while self.unvisitedHrefs:
            url = self.unvisitedHrefs.popleft()
            print url
            self.visitedHrefs.append(url)
            self._addToPool(url)
            self.decreaseRuns()

    def decreaseRuns(self):
        self.runs -= 1

    def getTasksLeft(self):
        if (len(self.unvisitedHrefs) + self.runs) > 0:
            return True
        else:
            return False

    def _addToPool(self, url):
        t = Thread(target=self._scrape(url))
        t.daemon = True
        t.start()

    def printResults(self):
        print self.hrefs.get()

    def stop(self):
        sys.exit()
