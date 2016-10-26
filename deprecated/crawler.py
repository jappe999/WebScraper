#!/usr/bin/python

# -*- coding: UTF-8 -*-

from threading import Thread
from webPage import webPage
from database import database
import sys, time
webPage = webPage() # Init webPage object

class crawler(object):
    def __init__(self, url, depth, maxPages=False):
        self.urlBegin = url
        self.depth = depth # Maximum depth of crawling
        self.currentDepth = 0
        self.unvisitedHrefs = []
        self.hrefs = [] # Object with all the hrefs from x layers
        self.visitedHrefs = []
        self.discoveredHrefs = []
        self.runs = 0
        self.timeBegin = time.time()
        self.database = database()

    # Async function to...
    def _scrape(self, url):
        response = webPage.getPage(url) # ... get pageresponse,...
        if not response == None:
            #self.visitedHrefs.append(url)
            domain  = webPage.getDomain(url) # ... get domain from that repsonse...
            path    = webPage.getPath(url)
            anchors = webPage.getAnchors(domain, path, response) # ... and get hrefs from the response
            self.database.appendToQueue(anchors)
            #self.database.removeFromQueue(url)
            for anchor in anchors: # Repeat the crawl function for every anchor
                if anchor[0] not in (self.visitedHrefs and self.hrefs): # If the anchor is already in the database, ignore it
                    self.discoveredHrefs.append(anchor[0])
                    self.hrefs.append(anchor[0]) # And last but not least: Put the retrieved anchors in a list for the next iteration

    def crawl(self, url):
        self.hrefs.append(url)
        self.unvisitedHrefs.append(url)
        while self.currentDepth < self.depth:
            print('\nLayer: {}'.format(self.currentDepth+1))
            self.runs = 0
            self._assignTasks()
            while self.getTasksLeft():
                time.sleep(.1)

            self.unvisitedHrefs = self.hrefs
            self.hrefs = []

            self.currentDepth += 1
        self.printResults()
        self.stop()

    def _assignTasks(self):
        while self.unvisitedHrefs:
            url = self.popLeft(self.unvisitedHrefs)
            self.visitedHrefs.append(url)
            self._addToPool(url)
            self.decreaseRuns()

    def popLeft(self, arr):
        url = arr[0]
        del(arr[0])
        return url

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
        print('\n')
        t = (time.time() - self.timeBegin)
        print('\nTime spent:', t)
        print('Hyperlinks found:', len(self.discoveredHrefs))
        hrefs = ''
        try:
            hrefs = ','.join(self.discoveredHrefs)
            open('./queue.txt', 'w+').write(hrefs)
        except Exception as e:
            print(e)
        finally:
            print('That\'s about {} Bytes'.format(len(hrefs)))
            div = (len(self.discoveredHrefs) / t)
            print('That\'s {} hyperlinks per second discovered.'.format(div))

        print('\nBegun from:', self.urlBegin)

    def stop(self):
        sys.exit()
