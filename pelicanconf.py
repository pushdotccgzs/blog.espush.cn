#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'webmaster@espush.cn'
SITENAME = u'espush blog'
SITEURL = ''
SITESUBTITLE = 'IoT Cloud on ESP8266'
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

'''
# Blogroll
LINKS = (('Python.org', 'http://python.org/'),)
'''

# Social widget
'''
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
'''

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'local_notmyidea'
#GITHUB_URL = 'https://github.com/pushdotccgzs/'
DUOSHUO_SITEURL = 'http://blog.espush.cn'

#rsync --delete --exclude ".DS_Store" -pthrvz -c --rsh='ssh  -p 2200 ' output/ sunday@espush.cn:/www/blog
STATIC_PATHS = ['images', ]
