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
        self.useWhiteList = False
        self.whiteList = []
        
        blackListFile = open("./gamma/blacklist.txt", "r")
        whiteListFile = open("./gamma/whitelist.txt", "r")
        
        #if(whiteListFile.read()[:3] != "123"):
        self.useWhiteList = True
        for whiteListEntry in whiteListFile:
            self.whiteList.append(whiteListEntry[:len(whiteListEntry) - 1])
        
        for blackListEntry in blackListFile:
            self.blackList.append(blackListEntry[:len(whiteListEntry) - 1])

    def getPage(self):
        try:
            response = requests.get(self.url)
        except Exception as e:
            print("Error loading the folowing page: " + self.url + "The error returned is:\n" + e)

        return response.text

    def getAnchors(self, response):
        soup    = BeautifulSoup(response, 'html5lib') # Init BeautifulSoup with the response of the webpage
        results = []
        for link in soup('a'):
            text = link.string            
            link = link.get('href')
            if link == None:
                continue
            anchor  = []

            #resolve the relative url to an absolute url
            href = urljoin(str(self.url), str(link))
            href = re.sub(r"(\#)[^\!\*\'\(\)\;\:\@\&\=\+\$\,\/\?\[\]]*", "", href)
 
            if self.isInBlackList(href) or (not self.isInWhiteList(href)) or href in results:
                continue
            
            anchor.append(href)
            anchor.append(text)
            results.append(anchor) # Put content in array
        return results

    def isInBlackList(self, link):
        testURLre = re.search("https?:\/\/([a-z|A-Z|0-9]*\.?)*", link)
        testURL = testURLre.group(0)

        if testURL in self.blackList:
            return True
        return False
    
    def isInWhiteList(self, link):
        if not self.useWhiteList:
            return True
        testURLre = re.search("https?:\/\/([a-z|A-Z|0-9]*\.?)*", link)
        testURL = testURLre.group(0)
        if testURL in self.whiteList:
            return True
        return False

