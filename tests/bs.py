#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import requests as r
from bs4 import BeautifulSoup

url      = 'http://wikipedia.org'
response = r.get(url)
soup     = BeautifulSoup(response.text, 'html.parser')
results  = []

for link in soup('a'):
    #anchor  = []
    href = re.sub("^[:]?[\/]{2}", "http://", link.get('href'))
    try:
        title = link.string if not link.string == None else ''
    except:
        title = ''

    print '{}, {}\n'.format(href, title)
    '''anchor.append(href)
    results.append(anchor)'''

print 'Source: {}'.format(soup.title.text)
