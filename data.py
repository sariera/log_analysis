#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2


def connect(dbname='news'):
    '''Connecting to POSTGRESQL database'''

    try:
        db = psycopg2.connect('dbname = news')
        c = db.cursor()
        return (db, c)
    except:
        print 'An error occurred while connecting to database'
