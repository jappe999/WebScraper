#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Queue import Queue
from threading import Thread
from webPage import webPage
webPage = webPage()

class crawler(object):
    def __init__(self, depth):
        self.depth = depth
        self.results = Queue()

    def scrape(self):
        response = webPage._getPage('https://webdrawings.nl')
        anchors = webPage._getAnchors(response.text)
        self.results.put(anchors)

    def crawl(self):
        currentDepth = 0
        while currentDepth < self.depth + 1:
            t = Thread(target=self.scrape())
            t.daemon = True
            t.start()
            currentDepth += 1

    def printResults(self):
        print self.results.get()
