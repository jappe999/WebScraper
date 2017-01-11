#!/usr/bin/python3

from database import Database
from keywords import *

def main(number):
    database = Database('root', '42069blazeIt', 'beta')
    while True:
        response = database.fetch(number)

        for line in response:
            try:
                url = re.sub('^(http://|https://)(www\.)?', '', line[1]) # Line[1] is the URL from table queue.
                url = re.sub('(/)$', '', url)
                print(url)
                path = '/home/user/WebScraper/Data/Meta/' + url + '/main.meta'

                keywords = getKeywords(path)
                print(getTitle(path))

                #database.addKeywords(line[0], keywords) # Line[0] is the ID of the URL in table queue.
                #database.update(line[0])
            except Exception as e:
                print(e)
                continue
    database.close() # Close database if loop stopped.



if __name__ == '__main__':
    main(100) # Call main definition with the parameter
              # that represents the amount of URL's proccessed each loop.
