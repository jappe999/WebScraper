import pymysql
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
            print("Error 0x01:")
            print(e)
            exit()

    def fetch(self, number):
        self.cursor.execute("SELECT ID, url FROM queue WHERE visited = 1 AND indexed = 0 ORDER BY ID DESC LIMIT " + str(number) + ";")
        results = self.cursor.fetchall()
        return results


    def update(self, id):
        try:
            self.cursor.execute("UPDATE queue SET indexed = '1' WHERE ID = " + str(id) + ";")
        except Exception as e:
            print("Error 0x02:")
            print(e)

    def addKeywords(self, id_url, keywords):
        try:
            for keyword in keywords:
                print(keyword)
                self.cursor.execute("INSERT INTO keywords (id_url, keywords) values (" + str(id_url) + ", '" + keyword + "');")
                self.db.commit()
        except Exception as e:
            print("Error 0x03:")
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
