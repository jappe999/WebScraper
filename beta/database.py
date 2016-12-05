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

    def getQueue(self, numberOfLinks=10):
        self.cursor.execute("SELECT url FROM queue WHERE visited = '0' LIMIT {};".format(numberOfLinks))
        result = self.cursor.fetchall()
        self.remove(result)
        return result


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

    def remove(self, obj):
        sql = "UPDATE queue SET visited='1' WHERE url = '{}';"
        for line in obj:
            url = re.sub("[\(\)\']", "", line[0])
            t = Thread(target=self.execute(sql.format(url)))
            t.daemon = True
            t.start()

    def clear(self):
        self.cursor.execute("DELETE FROM queue;")

    def execute(self, command):
        self.cursor.execute(command)
        self.db.commit()

    def close(self):
        self.db.close()
