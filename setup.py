#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='WebScraper',
      version='2.0.0',
      description='WebScraper, THE way to scrape the Web',
      author='Mitch Rob, Jasper van der Linden & Erik Baalbergen',
      author_email='jappe999@github.com',
      url='http://github.com/jappe999/WebScrapper',
      install_requires={
        'bs4': [
            'beautiful'
        ],
        'pymysql': ['*'],
        'html5lib': ['*'],
        'requests': ['*'],
        'colorama': ['*']
      }
     )
