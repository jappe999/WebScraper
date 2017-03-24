import pymysql, re, time
from threading import Thread
from colorama import init, Fore, Back, Style
from urllib.parse import quote, unquote
from sys import exit
from urllib.parse import quote

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
            print(Fore.RED + "INDEX error 0x1:")
            print(e)
            print(Style.RESET_ALL)
            exit()

    def getData(self, numberOfLinks=10):
        self.cursor.execute("SELECT ID, indexed FROM queue WHERE url like '%:%' AND visited>-1 LIMIT " + str(numberOfLinks) + ";")
        result = self.cursor.fetchall()
        for row in result:
            self.execute("UPDATE queue SET visited=-1 WHERE ID="+str(row[0])+";")
        return result

    def execute(self, command):
        try:
            self.cursor.execute(command)
            self.db.commit()
            return True
        except Exception as e:
            print('MySQL executing error', str(e))
            return False

    def close(self):
        self.cursor.close()
        self.db.close()
