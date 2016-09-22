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
            print 'Error: {}'.format(e)
        return response

    def _getAnchors(self, text):
        c = re._compile("\s*(?i)href\s*=\s*(\"([^\"]*\")|'[^']*'|([^'\">\s]+))", re.M)
        anchors = c.findall(text)
        return anchors
