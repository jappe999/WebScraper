#!/usr/bin/python
# -*- coding: UTF-8 -*-

from crawler import crawler
crawler = crawler(depth=4)

def main():
    url = 'http://wikipedia.org'
    crawler.crawl(url)

if __name__ == '__main__':
    main()
