# Logs Analysis Project

Reporting tool written in Python3 and created as an exercise in the Udacity
*Full Stack Web Developer* Nanodegree. The database *news* was provided and
is not part of this repo.

## How To Run

1. Have the *news* database set up
2. Run `create-views.py` once to create views in database
3. `Import reports` and run either:
    * `reports.output_print()` to print reports
    * `reports.output_write(file)` to write reports to *file* in plain text

## Documentation

* *create-views.py* creates and commits the three views necessary for the
  reports. The `create view` commands are also provided in the next
  section.
* *reports.py* provides 2 functions to either print or write to file
  formatted reports
* *output.txt* contains an example output from the program, i.e. the result
  of `reports.output_write("output.txt")`.

## Views

#### Popular articles

```sql
create view popular_articles as
select articles.title, count(log.id) as views
from articles left join log on log.path like ('%' || articles.slug)
group by articles.title
order by views desc
limit 3;
```

#### Popular authors

```sql
create view popular_authors as
select authors.name, count(log.id) as views
from articles
left join log on log.path like ('%' || articles.slug)
right join authors on articles.author = authors.id
group by authors.id
order by views desc;
```

#### Errors

```sql
create view errors_day as
select to_char(time, 'Month DD, YYYY') as day,
(count(case status when '404 NOT FOUND' then 1 else null end)::real/
count(status)*100)::real as err_perc
from log
group by day
having (count(case status when '404 NOT FOUND' then 1 else null end)::real/
count(status)*100)::real > 1;
```

## Further Links

* [Udacity: Full Stack Web Developer Nanodegree](https://de.udacity.com/course/full-stack-web-developer-nanodegree--nd004/)