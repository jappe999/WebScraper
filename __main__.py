#!/usr/bin/python
# -*- coding: UTF-8 -*-

from crawler import crawler
crawler = crawler(depth=1)

def main():
    crawler.crawl()
    crawler.printResults()

if __name__ == '__main__':
    main()
