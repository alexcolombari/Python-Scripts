#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Alex Colombari (http://github.com/alexcolombari)
Date: 2019-08-20
"""

import sys

if sys.version_info.major >= 3:
    from urllib.error import URLError
    from urllib.request import urlopen
else:
    from urllib2 import URLError, urlopen

def checkConnectivity():
    try:
        urlopen("http://google.com", timeout=3)
        print("Connection working!")
    except URLError as E:
        print("Connection error:%s" % E.reason)

checkConnectivity()
