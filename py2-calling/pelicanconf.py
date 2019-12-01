#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



AUTHOR = u'No True Calling'
SITENAME = u'No True Calling'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 4

THEME='twenty'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom Filter For Template

def sidebar(value):
  if value.startswith('archives') or value.startswith('category'):
    return 'right-sidebar'
  elif value == 'index':
    return 'index'
  else:
    return 'no-sidebar'


JINJA_FILTERS = {'sidebar': sidebar}

# def static_files_in_output():
  
