#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re, urllib
import requests as r
from bs4 import BeautifulSoup
from urlparse import urlparse as parser

url      = 'http://dmoz.com/'
uri      = parser(url)
domain   = '{}://{}/'.format(uri.scheme, uri.netloc)
response = r.get(url)
soup     = BeautifulSoup(response.text, 'html.parser')
results  = []

for link in soup('a'):
    #anchor  = []
    href = str(link.get('href'))
    href = re.sub("^[:]?[\/]{2}", "http://", href)
    href = re.sub("^[\/]{1}", domain, href)

    #Try this and otherwise the link is False
    try:
        title = link.string.encode('iso-8859-1') if not link.string == None else 'None'
        title = link.string.encode('utf-8') if not link.string == None else 'None'
    except UnicodeEncodeError or UnicodeDecodeError:
        continue

    print '{}, {}\n'.format(href, title)
    '''anchor.append(href)
    results.append(anchor)'''

print 'Source: {}'.format(soup.title.text)
