# -*- coding: utf-8 -*-
""" Tests """

# pylint: disable=missing-docstring,no-self-use,wrong-import-order,wrong-import-position

from __future__ import absolute_import, division, unicode_literals

import logging
import os
import sys

import xbmcaddon

try:  # Python 3
    from http.client import HTTPConnection
except ImportError:  # Python 2
    from httplib import HTTPConnection

logging.basicConfig(level=logging.DEBUG)

# Add logging to urllib
HTTPConnection.debuglevel = 1

# Make UTF-8 the default encoding in Python 2
if sys.version_info[0] == 2:
    reload(sys)  # pylint: disable=undefined-variable  # noqa: F821
    sys.setdefaultencoding("utf-8")  # pylint: disable=no-member

# Set credentials based on environment data
# Use the .env file with Pipenv to make this work nicely during development
ADDON = xbmcaddon.Addon()
if os.environ.get('ADDON_USERNAME'):
    ADDON.setSetting('username', os.environ.get('ADDON_USERNAME'))
if os.environ.get('ADDON_PASSWORD'):
    ADDON.setSetting('password', os.environ.get('ADDON_PASSWORD'))
if os.environ.get('ADDON_PROFILE'):
    ADDON.setSetting('profile', os.environ.get('ADDON_PROFILE'))
