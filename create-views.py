#!/usr/bin/env python3

import psycopg2


c = psycopg2.connect("dbname=news")
cursor = c.cursor()

# Create view to show 3 most popular articles
cursor.execute(
    "create view popular_articles as "
    "select articles.title, count(log.id) as views "
    "from articles left join log "
    "on log.path like ('%' || articles.slug) "
    "group by articles.title "
    "order by views desc "
    "limit 3;")

# Create view to show popular authors
cursor.execute(
    "create view popular_authors as "
    "select authors.name, count(log.id) as views "
    "from articles "
    "left join log on log.path like ('%' || articles.slug) "
    "right join authors on articles.author = authors.id "
    "group by authors.id "
    "order by views desc;")

# Create view to show days with percentage of errors over 1%
cursor.execute(
    "create view errors_day as "
    "select to_char(time, 'Month DD, YYYY') as day, "
    "(count(case status when '404 NOT FOUND' then 1 else null "
    "end)::real/ count(status)*100)::real as err_perc "
    "from log "
    "group by day "
    "having (count(case status when '404 NOT FOUND' then 1 else null "
    "end)::real/ count(status)*100)::real > 1;")

c.commit()
c.close()
