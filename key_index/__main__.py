#!/usr/bin/python3

from database import Database
from keywords import *

def main(number):
    database = Database('root', '42069blazeIt', 'beta')
    while True:
        response = database.fetch(number)

        for line in response:
            try:
                database.update(line[0])
                url = re.sub('^(http://|https://)(www\.)?', '', line[1])
                url = re.sub('(/)$', '', url)
                print(url)
                file = '/home/user/WebScraper/Data/Meta/' + url + '/main.meta'
            except Exception as e:
                print(e)
                continue

            try:
                keywords = getKeywords(file)
                print(getTitle(file))
                database.addKeywords(line[0], keywords)
            except Exception as e:
                print(e)
#        break
    database.close()



if __name__ == '__main__':
    main(100)
