# -*- coding: utf-8 -*-
"""
:copyright: (c) 2016 by Mike Taylor
:license: CC0 1.0 Universal, see LICENSE for more details.
"""

import os


_cwd = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    SECRET_KEY = "foob"
    BASEURL    = 'http://127.0.0.1:5000'
    BASE_ROUTE = '/'
    LOG_FILE   = os.path.join(_cwd, 'foob.log')

class ProdConfig(Config):
    ENV   = 'prod'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class DevConfig(Config):
    ENV   = 'dev'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestConfig(Config):
    ENV   = 'test'
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
