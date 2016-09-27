#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests, re
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class Crawler(object):
    """docstring for Crawler."""
    def __init__(self, layers, seed):
        super(Crawler, self).__init__()
        self.layers = layers
        self.seed = seed

    def setSeed(self, seed):
        if self.validURL(url):
            self.seed = seed

    def validURL(self, url):
        """TODO: Add checks for validation of URL"""
        return True


class WebPage(object):
    """docstring for WebPage."""
    def __init__(self, url, domain = None):
        super(WebPage, self).__init__()
        self.URL = url
        if not domain is None:
            self.domain = domain
        else:
            self.domain = re.search("^https?\:\/\/([^\/?#]+)(?:[\/?#]|$)", str(self.URL)).group(0)

    def getPage(self):
        request = None
        try:
            request = requests.get(self.URL)
        except Exception as e:
            raise
        if(request.status_code == 200):
            return request.text
        else:
            return request.status_code

    def getAnchors(self):
        text = self.getPage()
        soup = BeautifulSoup(text, 'html.parser')
        results = []
        for link in soup('a'):
            anchor  = []
            try:
                if link.get('href') == None:
                    continue
                href = str(link.get('href'))
                #href = str(link.get('href')).encode('utf-8') if not link.get('href') == None else '#' # Get href out of anchor
                href = re.sub("^[:]?[\/]{2}", "http://", href) # If href starts with :// or // replace it with http://
                href = re.sub("^[\/\?]|^\.\/?", self.domain, href) # If href starts with a single slash replace it with the domain
                print(href)
            except Exception as e:
                print('Error1: ', e)

            #Try this and otherwise the link is False and won't be put in the DB
            try:
                if link.string == None:
                    text = None
                else:
                    text = link.string
            except UnicodeEncodeError or UnicodeDecodeError:
                # If string isn't encoded in iso 8859-1, ignore it and go next iteration
                continue

            anchor.append(href)
            anchor.append(text)
            results.append(anchor) # Put content in array

        return results




def main():
    pass

if __name__ == "__main__":
    main()
    webpage = WebPage("http://v14ebaalbe.helenparkhurst.net")
    print( webpage.getAnchors() )
