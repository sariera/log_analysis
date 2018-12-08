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


def popular_article():
    '''print the most popular three articles of all time'''

    (db, c) = connect()
    query = \
        """select title, count(title) as views from log, articles
    where log.path = concat('/article/', articles.slug)
    group by title
    order by views desc
    limit 3
    """
    c.execute(query)
    result = c.fetchall()
    db.close()
    print '''
Popular Articles:
'''
    for i in range(0, len(result), 1):
        print '"' + result[i][0] + '" - ' + str(result[i][1]) + ' views'