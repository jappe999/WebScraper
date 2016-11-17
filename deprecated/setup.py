#!/usr/bin/env/python3

from os import system
from sys import exit

pipInstalls = ['bs4', 'requests', 'colorama', 'pymysql', 'html5lib']

def main():
        try:
            i = 0;
            items = ' '.join(pipInstalls)
            try:
                command = 'sudo python -m pip install {}'.format(items)
                system(command)
            except:
                i += 1

            try:
                command = 'sudo pip install {}'.format(items)
                system(command)
            except:
                i += 1

            try:
                command = 'sudo python3 -m pip install {}'.format(items)
                system(command)
            except:
                i += 1
            if i >= 3:
                print('You do not have pip installed')
                exit()
            print('Successfully initialized the Scraper.')
        except Exception as e:
            print('Error:', e)



if __name__ == '__main__':
    main()
