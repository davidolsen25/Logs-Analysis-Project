#!/usr/bin/python2.7

import psycopg2


def PopularArticles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "SELECT articles.title, COUNT(*) as num from articles join log on \
    articles.slug = substr(log.path, 10) WHERE log.status = '200 OK' GROUP BY \
    articles.title ORDER BY num DESC LIMIT 3;"
    c.execute(query)
    rows = c.fetchall()

    print "\n"" Most Popular Articles:" + "\n"

    for row in rows:
        print ' "%s" -- %s views' % (row[0], row[1])

    print "\n"

    db.close()

PopularArticles()


def PopularAuthors():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "SELECT authors.name, PopularAuthorsId.views from authors \
    join PopularAuthorsId on authors.id = PopularAuthorsId.author ORDER BY \
    views DESC;"
    c.execute(query)
    rows = c.fetchall()

    print " Most Popular Authors:" + "\n"

    for row in rows:
        print ' %s -- %s views' % (row[0], row[1])

    print "\n"

    db.close()

PopularAuthors()


def ErrorDays():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = "SELECT to_char(ErrorsPerDay.time, 'FMMonth FMDDth, FMYYYY') from \
    ErrorsPerDay join ViewsPerDay on ErrorsPerDay.time = ViewsPerDay.time \
    WHERE ErrorsPerDay.num > ViewsPerDay.num/100 ORDER BY \
    ErrorsPerDay.time ASC;"
    c.execute(query)
    rows = c.fetchall()

    print " Dates when more than 1% of requests lead to errors:" + "\n"

    for row in rows:
        print ' %s' % (row[0])

    print "\n"

    db.close()

ErrorDays()

