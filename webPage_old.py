#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import requests as r

class webPage(object):
    def __init__(self, proxies=""):
        pass

    def _getPage(self, url):
        response = None
        url = url.replace('\"', '')
        url = url.replace('^(\/\/)', 'http://')
        try:
            response = r.get(url)
        except Exception as e:
            pass
            #print 'Error: {}'.format(e)
        return response

    def _getAnchors(self, text):
        c = re._compile("<a\s*(?i)href\s*=\s*(\"([^\"]*\")|'[^']*'|([^'\">\s]+))", re.M) # Regex for get text out of href attr
        anchors = c.findall(text)
        results = []
        for anchor in anchors:
            a = list(anchor)
            print a[0]
            a[0] = a[0].replace('^((?!(http:|https:))?[\/]{2})', 'http://')
            results.append(a[0])

        return results
