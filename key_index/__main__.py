#!/usr/bin/python3

import re, time
from database import Database
from keywords import *

def main(number):
    database = Database('root', '42069blazeIt', 'beta')
    while True:
        response = database.fetch(number)
        time.sleep(1)

        for line in response:
            try:
                url = re.sub('^(http://|https://)(www\.)?', '', line[1]) # Line[1] is the URL from table queue.
                url = re.sub('(/)$', '', url)
                print(url)
                path = '/home/user/Desktop/WebScraper/Data/' + url + '/index.html'
                blob = open(path, 'r+').read().lower()

                keywords = [key['content'] for key in getKeywords(blob)]
                print(getTitle(blob))

                #database.addKeywords(line[0], keywords) # Line[0] is the ID of the URL in table queue.
                #database.update(line[0])
            except Exception as e:
                print(e)
                continue
    database.close() # Close database if loop stopped.



if __name__ == '__main__':
    main(10) # Call main definition with the parameter
              # that represents the amount of URL's proccessed each loop.
