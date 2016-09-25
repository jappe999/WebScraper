#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Import libraries
import re, urllib
import requests as r
from bs4 import BeautifulSoup
from urlparse import urlparse as parser

class webPage(object):
    def __init__(self, proxies=""):
        pass

    def getDomain(self, url):
        uri     = parser(url)
        domain  = '{}://{}/'.format(uri.scheme, uri.netloc)
        return domain

    def getPage(self, url):
        response = None
        domain = self.getDomain(url)
        url = re.sub("^[:]?[\/]{2}", "http://", url) # If url starts with :// or // replace it with http://
        url = re.sub("^[\/]{1}", domain, url) # If url starts with a single slash replace it with the domain
        try:
            response = r.get(url)
        except Exception as e:
            pass
            #print 'Error: {}'.format(e)
        return response

    def getAnchors(self, domain, response):
        soup    = BeautifulSoup(response, 'html.parser') # Init BeautifulSoup with the response of the webpage
        results = []
        for link in soup('a'):
            anchor  = []
            try:
                href = str(link.get('href')).encode('utf-8') if not link.get('href') == None else '#' # Get href out of anchor
                href = re.sub("^[:]?[\/]{2}", "http://", href) # If href starts with :// or // replace it with http://
                href = re.sub("^[\/]{1}", domain, href) # If href starts with a single slash replace it with the domain
            except:
                print 'error'

            #Try this and otherwise the link is False and won't be put in the DB
            try:
                text = link.string.encode('iso-8859-1') if not link.string == None else 'None' # Try encode to iso 8859-1 if not empty
                text = link.string.encode('utf-8') if not link.string == None else 'None' # Try encode to utf-8 if not empty
                html = link.encode('utf-8') if not link == None else 'None' # Try encode to utf-8 if not empty
            except UnicodeEncodeError or UnicodeDecodeError:
                # If string isn't encoded in iso 8859-1, ignore it and go next iteration
                continue

            #print href
            anchor.append(href)
            anchor.append(text)
            results.append(anchor) # Put content in array

        '''
        c = re._compile("<a\s*(?i)href\s*=\s*(\"([^\"]*\")|'[^']*'|([^'\">\s]+))", re.M) # Regex for get text out of href attr
        anchors = c.findall(text)
        results = []
        for anchor in anchors:
            a = list(anchor)
            print a[0]
            a[0] = a[0].replace('^((?!(http:|https:))?[\/]{2})', 'http://')
            results.append(a[0])
        '''

        return results
