#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Import libraries
import re, urllib
import requests as r
from bs4 import BeautifulSoup
from urlparse import urlparse as parser

url      = 'http://dmoz.com/' # The start URL
uri      = parser(url)
domain   = '{}://{}/'.format(uri.scheme, uri.netloc)
response = r.get(url) # Get content from http://dmoz.com/
soup     = BeautifulSoup(response.text, 'html.parser') # Init BeautifulSoup with the response of http;//dmoz.com/
results  = []

for link in soup('a'):
    anchor  = []
    href = str(link.get('href')) # Get href out of anchor
    href = re.sub("^[:]?[\/]{2}", "http://", href) # If href starts with :// or // replace it with http://
    href = re.sub("^[\/]{1}", domain, href) # If href starts with a single slash replace it with the domain

    #Try this and otherwise the link is False and won't be put in the DB
    try:
        text = link.string.encode('iso-8859-1') if not link.string == None else 'None' # Try encode to iso 8859-1 if not empty
        text = link.string.encode('utf-8') if not link.string == None else 'None' # Try encode to utf-8 if not empty
        html = link.encode('utf-8') if not link == None else 'None' # Try encode to utf-8 if not empty
    except UnicodeEncodeError or UnicodeDecodeError:
        # If string isn't encoded in iso 8859-1, ignore it
        continue

    print '{}, {}, {}\n'.format(href, text, html) # Print retrieved content
    anchor.append(href)
    anchor.append(text)
    results.append(anchor) # Put content in array

print 'Source: {}'.format(soup.title.text)
