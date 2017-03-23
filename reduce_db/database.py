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
        self.cursor.execute("SELECT ID FROM queue WHERE url like '%:%' LIMIT " + str(numberOfLinks) + ";")
        result = self.cursor.fetchall()
        return result

    def execute(self, command):
        try:
            self.cursor.execute(command)
            self.db.commit()
        except Exception as e:
            print('MySQL executing error', str(e))

    def close(self):
        self.cursor.close()
        self.db.close()
