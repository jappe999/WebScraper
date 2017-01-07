#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Import libraries
import re, requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse as parser
from urllib.parse import urljoin

class webPage(object):
    def __init__(self, url):
        self.url = url
        self.blackList = []
        
        blackListFile = open("blacklist.txt", "r")
        for blackListEntry in blackListFile:
            self.blackList.append(blackListEntry)

    def getPage(self):
        response = ''
        try:
            response = requests.get(self.url)
            if response.status_code != 404:
                response = response.text.encode('utf-8')
            else:
                response = ''
        except Exception as e:
            print(e)

        return response

    def getAnchors(self, response):
        text    = response
        soup    = BeautifulSoup(text, 'html5lib') # Init BeautifulSoup with the response of the webpage
        results = []
        for link in soup('a'):
            link = link.get('href')
            if link == None:
                continue
            anchor  = []

            #resolve the relative url to an absolute url
            href = urljoin(str(self.url), str(link))

            anchor.append(href)
            anchor.append(text)
            if !self.isInBlackList(anchor):
                results.append(anchor) # Put content in array

        return results

    def isInBlackList(link):
        testURLre = re.search("https?:\/\/([a-z|A-Z|0-9]*\.?)*", link)
        testURL = testURLre.group(0)
        
        for blackListEntry in self.blackList:
            if testURL == blackListEntry:
                return True
        return False
