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
		
        blackListFile = open("blacklist.txt", "r")
        whiteListFile = open("whitelist.txt", "r")
		
        if(whiteListFile.read()[:3] != "123"):
            self.useWhiteList = True
            for whiteListEntry in whiteList:
                self.whiteList.append(whiteListEntry)
		
        for blackListEntry in blackListFile:
            self.blackList.append(blackListEntry)

    def getPage(self):
        try:
            responseFromServer = requests.get(self.url)
            if responseFromServer.status_code != 404:
                response = responseFromServer.text.encode('utf-8')
        except Exception as e:
            print("Error loading the folowing page: " + self.url + "The error returned is:\n" + e)

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
			
            if self.isInBlackList(href) or not isInWhiteList(href):
                continue
            
            anchor.append(href)
            anchor.append(text)
            results.append(anchor) # Put content in array

        return results

    def isInBlackList(link):
        testURLre = re.search("https?:\/\/([a-z|A-Z|0-9]*\.?)*", link)
        testURL = testURLre.group(0)
        
        for blackListEntry in self.blackList:
            if testURL == blackListEntry:
                return True
        return False
	
    def isInWhiteList(link):
        if not self.useWhiteList:
            return True
        testURLre = re.search("https?:\/\/([a-z|A-Z|0-9]*\.?)*", link)
        testURL = testURLre.group(0)
        
        for whiteListEntry in self.whiteList:
            if testURL == whiteListEntry:
                return True
        return False
