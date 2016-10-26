#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

class database(object):
    def __init__(self):
        self.directory = './data/'
        self.directoryMeta = '{}meta-info/'.format(self.directory)
        self.directorySites = '{}site-info/'.format(self.directory)
        self._initDatabase()

    #Prepare all directories
    def _initDatabase(self):
        try:
            # Try and create the data directory
            if not os.path.exists(self.directory):
                os.mkdir(self.directory)

            # Try and create the meta-info directory
            if not os.path.exists(self.directoryMeta):
                os.mkdir(self.directoryMeta)

            # Try and create the site-info directory
            if not os.path.exists(self.directorySites):
                os.mkdir(self.directorySites)
        except Exception as e:
            print(e)

    def appendToQueue(self, obj):
        with open('{}queue.txt'.format(self.directory), 'a+') as fw:
            for x in obj:
                y = x[0]
                if not self.isInQueue(y):
                    fw.write(y+'\n')

    # Returns True or False
    def isInQueue(self, key):
        with open('{}queue.txt'.format(self.directory), 'r+') as fr:
            r = fr.read()
            if key in r:
                return True
            return False

    def writeToMeta(self, domain, obj):
        with open('{}{}.json'.format(self.directoryMeta, domain), 'a+') as fw:
            for x in obj:
                fw.write(x)

    def writeToSites(self, domain, obj):
        with open('{}{}.meta'.format(self.directorySites, domain), 'a+') as fw:
            for x in obj:
                fw.write(x)
