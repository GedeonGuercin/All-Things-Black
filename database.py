#!/usr/bin/env python

#-----------------------------------------------------------------------
# database.py
# Author: Gedeon, Yenet, Donald
#-----------------------------------------------------------------------

import sqlite3
import contextlib

#-----------------------------------------------------------------------

_DATABASE_URL = 'file:data.sqlite?mode=ro'

def get_name():

    names = []
    with sqlite3.connect(_DATABASE_URL, uri=True) as connection:

        with contextlib.closing(connection.cursor()) as cursor:


    return names

