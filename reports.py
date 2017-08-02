#! python3.5

import psycopg2


# Takes query as input and returns fetchall results
def news_query_results(query):
    c = psycopg2.connect("dbname=news")
    cursor = c.cursor()
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


print(popular_articles())
print(popular_authors())
