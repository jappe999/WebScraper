#!/usr/bin/python
# -*- coding: UTF-8 -*-

from crawler import crawler
crawler = crawler(depth=4)

def main():
    print """
This program scrapes the Internet for top-level domains, meta-information and other important data.\n
It starts from the domain \'http://wikipedia.org\' and follows an huge network of hyperlinks.\n
\n
MIT License\n
Build by:
\t@papierbouwer
\t@midyro and
\t@jappe999
    """
    url = 'http://wikipedia.org'
    crawler.crawl(url)

if __name__ == '__main__':
    main()
