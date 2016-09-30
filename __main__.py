#!/usr/bin/python
# -*- coding: UTF-8 -*-

from crawler import crawler
from termcolor import colored

url = 'http://dmoz.com/'
crawler = crawler(url, depth=2)

def main():
    print("""
This program scrapes the Internet for top-level domains, meta-information and other important data.
It starts from the domain \'http://dmoz.com/\' and follows an huge network of hyperlinks.

MIT License\n
Build by:
\t@papierbouwer
\t@hahaha1234 and
\t@jappe999
    """)
    crawler.crawl(url)

if __name__ == '__main__':
    main()
