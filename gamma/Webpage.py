#!/usr/bin/python
# -*- coding: UTF-8 -*-

import FileSystem, re, requests, htmlmin, os.path
from bs4 import BeautifulSoup
from urllib.parse import urlparse as parser
from urllib.parse import urljoin

class Webpage(object):
    def __init__(self, url):
        self.url           = url
        self.blacklist     = []
        self.use_whitelist = True
        self.whitelist     = []

        dir_name = os.path.dirname(os.path.realpath(__file__))
        BLACKLIST_FILE = open(dir_name + '/blacklist.txt', 'r')
        WHITELIST_FILE = open(dir_name + '/whitelist.txt', 'r')

        for whitelist_entry in WHITELIST_FILE:
            self.whitelist.append(whitelist_entry[:len(whitelist_entry) - 1])

        for blacklist_entry in BLACKLIST_FILE:
            self.blacklist.append(blacklist_entry[:len(blacklist_entry) - 1])

    def strip_content(self, html):
        soup = BeautifulSoup(html, 'html5lib')

        # Remove all script and style tags
        for elem in soup.findAll(['script', 'style']):
            elem.extract()

        stripped_html = str(soup)
        minified_html = htmlmin.minify(stripped_html)

        return minified_html

    def get_page(self):
        try:
            response          = requests.get(self.url)
            stripped_response = self.strip_content(response.text)

            return stripped_response
        except Exception as e:
            print('Error loading the folowing page: %s The error returned is:\n %s' % (self.url, e, ))

        return ''

    def relevant(self, uri):
        search_results = re.search('(#|mailto\:)', uri)
        return True if search_results == None else False

    def get_anchors(self, response):
        # Init BeautifulSoup with the response of the webpage
        soup    = BeautifulSoup(response, 'html5lib')
        results = []

        # For every anchor found on the page
        for uri in soup('a'):
            text = uri.string
            uri  = uri.get('href')

            # Resolve the relative url to an absolute url
            href = urljoin(str(self.url), str(uri))

            if self.is_in_blacklist(href) or href in results or not self.relevant(href):
                continue

            anchor = [ href, text ]
            results.append(anchor)

        return results

    def is_in_blacklist(self, href):
        url_regex = re.search('http(s)?:\/\/([a-z|A-Z|0-9]*\.?)*', href)

        if not url_regex:
            return False

        url = url_regex.group(0)
        if url in self.blacklist:
            return True
        return False

    def is_in_whitelist(self, href):
        if not self.use_whitelist:
            return True

        url_regex = re.search('https?:\/\/([a-z|A-Z|0-9]*\.?)*', href)
        url       = url_regex.group(0)

        if url in self.whitelist:
            return True

        return False
