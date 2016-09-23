#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re, MySQLdb
import requests as r
from bs4 import BeautifulSoup

url = '//wikipedia.org'
url = re.sub("^[:]?[\/]{2}", "http://", url)
response = r.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    print '{}\n'.format(link)

print 'Source: {}'.format(soup.title.text)
