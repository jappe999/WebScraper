#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
        self.visitedHrefs = deque()
        self.runs = 0

    # Async function to...
    def _scrape(self, url):
        response = webPage.getPage(url) # ... get pageresponse,...
        if not response == None:
            #self.visitedHrefs.append(url)
            domain = webPage.getDomain(url) # ... get domain from that repsonse...
            anchors = webPage.getAnchors(domain, response.text) # ... and get hrefs from the response
            for anchor in anchors: # Repeat the crawl function for every anchor
                if anchor[0] not in (self.visitedHrefs and self.hrefs): # If the anchor is already in the database, ignore it
                    #print anchor[0]
                    self.hrefs.append(anchor[0]) # And last but not least: Put the retrieved anchors in a list for the next iteration

    def crawl(self, url):
        self.unvisitedHrefs.append(url)
        while self.currentDepth < self.depth:
            print '\nLayer: {}'.format(self.currentDepth+1)
            self.runs = 0
            self._assignTasks()
            while self.getTasksLeft():
                time.sleep(.1)

            self.unvisitedHrefs = self.hrefs
            self.hrefs = deque()

            self.currentDepth += 1
        self.printResults()
        self.stop()

    def _assignTasks(self):
        while self.unvisitedHrefs:
            url = self.unvisitedHrefs.popleft()
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
        self.visitedHrefs.append(url)
        t = Thread(target=self._scrape(url))
        t.daemon = True
        t.start()

    def printResults(self):
        print '\n'
        for href in self.visitedHrefs:
            print href

    def stop(self):
        sys.exit()
