from database import Database
from keywords import *

def main(number):
    database = Database('root', '42069blazeIt', 'beta')
    response = database.fetch(number)

    for line in response:
        database.update(line[0])
        directory = 'Data/Meta/' + re.sub('^(http://|https://)(www\.)?', '', line[1])
        keywords = getKeywords(directory)
        database.addKeywords(line[0], keywords)
    database.close()



if __name__ == '__main__':
    main(100)
