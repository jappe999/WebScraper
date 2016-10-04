# WebScraper
A WebScraper made with python

## Looking for the wiki?
Are you looking for the wiki? Click [here](wiki/)


## Before running the script
If you use this program for the first time, you need to run [setup.py](https://github.com/jappe999/WebScraper/blob/master/setup.py). This installs the required packages this program need.

## The usage:
In the file [\_\_main\_\_.py](https://github.com/jappe999/WebScraper/blob/master/__main__.py) is a variable that's called _url_. This URL is the point from where the Scraper starts and dives into the amazing Internet.  
There is also another parameter that's called _depth_ and represents the number of layers it should search.  
**For example:**
```
url = 'http://example.com/'
crawler = crawler(url, depth=2)
crawler.crawl(url)
```
**The output could be:**
```
http://example.com/
--> http://example.com/page1
  --> http://example.com/page1/subpage1
  --> http://example.com/page1/subpage2
--> http://example.com/page2
  --> http://example.com/page1/subpage1
  --> http://example.com/page1/subpage2
  --> http://example.com/page1/subpage3
--> http://example.com/page3
```
This shows the content of 2 layers; The one from the 3 pages and the one from the pages within their "parent-page".
