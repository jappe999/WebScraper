#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .crawler import crawler
crawler = crawler(depth=2)

def main():
    print("""
This program scrapes the Internet for top-level domains, meta-information and other important data.\n
It starts from the domain \'http://dmoz.com/\' and follows an huge network of hyperlinks.\n
\n
MIT License\n
Build by:
\t@papierbouwer
\t@hahaha1234 and
\t@jappe999
    """)
    url = 'http://webdrawings.nl/'
    crawler.crawl(url)

if __name__ == '__main__':
    main()
