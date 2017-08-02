#! python3.5

import psycopg2


c = psycopg2.connect("dbname=news")
cursor = c.cursor()

# Create view to show popular articles
cursor.execute(
    "create view popular_articles as select articles.title, "
    "count(log.id) as views from articles left join log on log.path "
    "like ('%' || articles.slug) group by articles.title order by "
    "views desc;")

c.commit()
c.close()
