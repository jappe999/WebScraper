import pymysql, re, time
from threading import Thread
from colorama import init, Fore, Style
from urllib.parse import quote, unquote
from sys import exit

class Database(object):
    def __init__(self, user, password, database, host='127.0.0.1', port=3306):
        try:
            init()
            self.db = pymysql.connect (
                          host     = host,
                          port     = port,
                          user     = user,
                          password = password,
                          db       = database
                      )
            self.cursor = self.db.cursor()
        except Exception as e:
            Database.error(e, '0x1')
            exit()

    @staticmethod
    def error(err, err_code):
        print(Fore.RED + 'BETA database error %s:%s' % (err_code, err, ))
        print(Style.RESET_ALL)

    def get_queue(self, num_links=10):
        self.execute("SELECT url FROM queue WHERE visited = '0' LIMIT %d;" % (num_links, ))

        result   = self.cursor.fetchall()
        response = []

        self.remove(result)

        for i in range(len(result)):
            response.append(unquote(result[i][0]))
            response[i] = re.sub(r'(\\)*$', '', response[i])

        return response

    def write_to_db(self, url):
        try:
            self.execute("INSERT INTO queue (url, visited, unixtime) VALUES ('%s', 0, '%d');" % (self.escape_url(url), int(time.time()), ))

            print(Fore.GREEN + 'Added', url, 'to queue.')
            print(Style.RESET_ALL)
        except Exception as e:
            if not '(1062, "Duplicate entry ' in str(e):
                Database.error(e, '0x2')

    def set_queue(self, urls):
        for url in urls:
            t        = Thread(target=self.write_to_db(url))
            t.daemon = True
            t.start()

        return True

    def escape_url(self, url):
        return re.sub(r'(\\)*$', '', url)

    def update_queue(self, url):
        try:
            self.execute("UPDATE queue SET visited=1, unixtime='%d' WHERE url = '%s';" % (int(time.time()), self.escape_url(url), ))
        except Exception as e:
            Database.error(e, '0x3')

    def remove(self, urls):
        for line in urls:
            url      = line[0]
            t        = Thread(target=self.update_queue(url))
            t.daemon = True
            t.start()

    def execute(self, command):
        self.cursor.execute(command)
        self.db.commit()

    def close(self):
        self.db.close()
