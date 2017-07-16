# Logs-Analysis-Project
by David Olsen

This program is a Python script which queries the database newsdata.sql using Postgresql. The design is only three Python functions which query the database and are then called. The design also includes three views which are stated below . The program is run from the command line of a Linux operating system or virtual machine with the command "$ python LogsAnalysisProject.py". In creating the program, I used Oracle's VirtualBox as Linux virtual machine and Vagrant to communicate between the host and guest.

The program answers three question about the database of news articles in the database newsdata.sql:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Three views were created for the program and must be loaded into the database to run the program (with news=> CREATE VIEW viewname as ...;):

CREATE VIEW PopularAuthorsId as SELECT articles.author, COUNT(*) as views FROM articles JOIN log on articles.slug = substr(log.path, 10) WHERE log.status = '200 OK' GROUP BY articles.author ORDER BY views DESC LIMIT 4;

CREATE VIEW ErrorsPerDay as SELECT log.time::date, COUNT(*) as num from log where log.status != '200 OK' GROUP BY log.time::date;

CREATE VIEW ViewsPerDay as SELECT log.time::date, COUNT(*) as num from log GROUP BY log.time::date;
