#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Import libraries
import re, requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse as parser

class webPage(object):
    def __init__(self, proxies=[]):
        pass

    def getDomain(self, url):
        uri     = parser(url)
        domain  = '{}://{}'.format(uri.scheme, uri.netloc)
        return domain

    def getPath(self, url):
        uri     = parser(url)
        return uri.path + '/'

    def getPage(self, url):
        domain = self.getDomain(url)
        path   = self.getPath(url)
        url = re.sub("^[:]?[\/]{2}", "http://", url) # If url starts with :// or // replace it with http://
        url = re.sub("^[\/]{1}", domain, url) # If url starts with a single slash replace it with the domain
        url = re.sub("^([?#].*){1}", domain + path + url, url)
        response = ''
        try:
            response = requests.get(url)
            response = response.text
        except Exception as e:
            print(e)

        return response

    def getAnchors(self, domain, path, response):
        soup    = BeautifulSoup(response, 'html.parser') # Init BeautifulSoup with the response of the webpage
        results = []
        for link in soup('a'):
            anchor  = []
            try:
                href = link.get('href') if not link.get('href') == None else '#' # Get href out of anchor
                href = re.sub("^[:]?[\/]{2}", "http://", href) # If href starts with :// or // replace it with http://
                href = re.sub("^[\/]{1}", domain + '/', href) # If href starts with a single slash replace it with the domain
                href = re.sub("^([?#].*){1}", domain + path + href, href)
            except Exception as e:
                print('Error: ', e)

            #Try this and otherwise the link is False and won't be put in the DB
            try:
                text = link.string.encode('iso-8859-1') if not link.string == None else 'None' # Try encode to iso 8859-1 if not empty
                text = link.string.encode('utf-8') if not link.string == None else 'None' # Try encode to utf-8 if not empty
                html = link.encode('utf-8') if not link == None else 'None' # Try encode to utf-8 if not empty
            except UnicodeEncodeError or UnicodeDecodeError:
                # If string isn't encoded in iso 8859-1, ignore it and go next iteration
                continue

            anchor.append(href)
            anchor.append(text)
            results.append(anchor) # Put content in array

        return results