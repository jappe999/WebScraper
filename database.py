#!/usr/bin/python
# -*- coding: UTF-8 -*-

class database(object):
    def __init__(self):
        self.directory = './data/'
        self.directoryMeta = '{}meta-info/'.format(self.directory)
        self.directorySites = '{}site-info/'.format(self.directory)

    def _initDatabase(self):
        try:
            open(self.directory, 'r+')
        except:
            pass
