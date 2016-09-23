#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re, string
import requests as r

url = 'http://wikipedia.org'
url = re.sub("^[:]?[\/]{2}", "http://", url)
response = r.get(url)

c = re._compile("(<\s*a\s*(?i)href\s*=\s*(\"([^\"]*\")|'[^']*'|([^'\">\s]+))|<\s*meta\s*(?i).*\s*/>", re.M) # Regex for get text out of href attr
anchors = c.findall(response.text)
results = []
for anchor in anchors:
    a = list(anchor)
    a[0] = a[0].replace('\"', '')
    a[0].replace("^[:][\/]{2}", 'http://')

    '''if not slash == '':
        print slash
        a[0] = 'http://{}'.format(str(slash[0]))
    '''
    print a[0]
    results.append(a[0])

print slashes
