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


def popular_authors():
    '''print the most popular article authors of all time'''

    (db, c) = connect()
    query = \
        """select authors.name, count(log.path) as views from log
    join articles
    on log.path = concat('/article/', articles.slug)
    join authors
    on authors.id = articles.author
    group by authors.name
    order by views desc
    """
    c.execute(query)
    result = c.fetchall()
    db.close()
    print '''
Popular Authors:
'''
    for i in range(0, len(result), 1):
        print '"' + result[i][0] + '" - ' + str(result[i][1]) + ' views'


def log_status():
    '''print the days have more than 1% of requests lead to errors'''

    (db, c) = connect()
    query = \
        """
select * from (select a.date, round(cast((b.hit_error * 100) as numeric) /
cast(a.total_views as numeric), 2) as error_rate
from ((select cast(time as date) as date,
count(*) as total_views from log group by 1) as a
join (select cast(time as date) as date, count(*) as hit_error from
log where status not like '%200%' group by 1) as b
on a.date = b.date)) as t
where error_rate > 1;
"""
    c.execute(query)
    result = c.fetchall()
    db.close()
    print '''
Days with more than 1% of errors:
'''
    for i in range(0, len(result), 1):
        print str(result[i][0]) + ' - ' + str(result[i][1]) + '% errors'

