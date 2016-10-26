#!/usr/bin/python
# -*- coding: UTF-8 -*-

from crawler import crawler
from threading import Thread

URLs = ['http://dmoz.com', 'http://wikipedia.org']

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
    for url in URLs:
        t = Thread(target=crawler(url, depth=1).crawl(url))
        t.daemon = True
        t.start()

if __name__ == '__main__':
    main()
