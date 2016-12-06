import pymysql, re
from threading import Thread
from sys import exit

class Database(object):
    def __init__(self, user, password, database):
        try:
            self.db = pymysql.connect (
                        host="127.0.0.1",
                        port=3306,
                        user=user,
                        password=password,
                        db=database
                      )
            self.cursor = self.db.cursor()
        except Exception as e:
            print(e)
            exit()

    def fetch(self, number):
        self.cursor.execute("SELECT ID, url FROM queue WHERE visited = '1' LIMIT {};".format(number))
        results = self.cursor.fetchall()
        print(results)
        #for result in results:
        #    self.execute("UPDATE queue SET indexed = '1' WHERE ID = {};".format(result))
        return results


    def writeToDb(self, url):
        try:
            self.cursor.execute("INSERT INTO queue (url, visited) VALUES ('{}', '0');".format(url))
            self.db.commit()
        except Exception as e:
            print(e)

    def setQueue(self, obj):
        for url in obj:
            t = Thread(target=self.writeToDb(url))
            t.daemon = True
            t.start()
        return True

    def execute(self, command):
        self.cursor.execute(command)
        self.db.commit()

    def close(self):
        self.db.close()
