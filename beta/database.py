import pymysql
from threading import Thread
from colorama import init, Fore, Back, Style
from urllib2 import quote, unquote
from sys import exit

class Database(object):
    def __init__(self, user, password, database):
        try:
            init()
            self.db = pymysql.connect (
                        host="127.0.0.1",
                        port=3306,
                        user=user,
                        password=password,
                        db=database
                      )
            self.cursor = self.db.cursor()
        except Exception as e:
            print(Fore.RED + "BETA error 0x1:")
            print(e)
            print(Style.RESET_ALL)
            exit()

    def getQueue(self, numberOfLinks=10):
        self.cursor.execute("SELECT url FROM queue WHERE visited = '0' LIMIT " + str(numberOfLinks) + ";")
        result = self.cursor.fetchall()
        self.remove(result)
        for i in range(len(result)):
            result[i] = unquote(result[i]).decode('utf-8')
        return result


    def writeToDb(self, url):
        try:
            self.cursor.execute("INSERT INTO queue (url, visited) VALUES ('" + self.escapeURL(url) + "', '0');")
            self.db.commit()
        except Exception as e:
            print(Fore.RED + "BETA error 0x2:")
            print(e)
            print(Style.RESET_ALL)

    def setQueue(self, obj):
        for url in obj:
            t = Thread(target=self.writeToDb(url))
            t.daemon = True
            t.start()
        return True

    def escapeURL(self, url):
        return quote(url.encode("utf-8"))

    def updateQueue(self, url):
        try:
            self.cursor.execute("UPDATE queue SET visited='1' WHERE url = '" +  self.escapeURL(url) + "';")
            self.db.commit()
        except Exception as e:
            print(Fore.RED + "BETA error 0x3:")
            print(e)
            print(Style.RESET_ALL)
		
    def remove(self, obj):
        for line in obj:
            url = line[0]
            t = Thread(target=self.updateQueue(url))
            t.daemon = True
            t.start()

    def clear(self):
        self.cursor.execute("DELETE FROM queue;")

    def execute(self, command):
        self.cursor.execute(command)
        self.db.commit()

    def close(self):
        self.db.close()
