#!/usr/bin/env python3

import psycopg2
import sys


def connect(db_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        c = psycopg2.connect("dbname={}".format(db_name))
        cursor = c.cursor()
        return c, cursor
    except psycopg2.Error as e:
        print("Unable to connect to database")
        sys.exit(1)


# Takes query as input and returns fetchall results
def news_query_results(query):
    c, cursor = connect("news")
    cursor.execute(query)
    result = cursor.fetchall()
    c.close()
    return result


# Returns articles and corresponding views, sorted by the latter
def popular_articles():
    query = ("select * from popular_articles")
    result = news_query_results(query)
    output_string = ""
    for i in result:
        output_string += '"{}" -- {} views\n'.format(i[0], i[1])
    return output_string


# Returns author names and views, sorted by the latter
def popular_authors():
    query = ("select * from popular_authors")
    result = news_query_results(query)
    output_string = ""
    for i in result:
        output_string += '{} -- {} views\n'.format(i[0], i[1])
    return output_string


# Returns days and percentage of errors for days with over 1% errors
def errors():
    query = ("select * from errors_day")
    result = news_query_results(query)
    output_string = ""
    for i in result:
        output_string += '{} -- {}% errors\n'.format(" ".join(i[0].split()),
                                                     i[1])
    return output_string


output = popular_articles() + "\n" + popular_authors() + "\n" + errors()


# Print output
def output_print():
    print(output)


# Write output to file output.txt
def output_write(file):
    with open(file, "w") as f:
        f.write(output)
