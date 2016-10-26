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

    def getPage(self):
        response = ''
        try:
            response = requests.get(self.url)
            response = response.text
        except Exception as e:
            print(e)

        return response

    def getAnchors(self):
        text = self.getPage()
        soup    = BeautifulSoup(text, 'html5lib') # Init BeautifulSoup with the response of the webpage
        results = []
        for link in soup('a'):
            anchor  = []
            """try:
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
                continue"""

            #resolve the relative url to an absolute url
            href = urljoin(str(self.url), str(link))
            
            anchor.append(href)
            anchor.append(text)
            results.append(anchor) # Put content in array

        return results
