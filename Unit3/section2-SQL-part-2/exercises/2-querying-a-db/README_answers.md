## Querying a SQL Database

In this challenge you are given a SQL database with data inside. You will need to mine it for important information.

Open it up in terminal by typing
```bash
$ sqlite3 sitemetrics.db
```
To see the existing tables and columns, use the .schema command. Map this by hand or on SQL designer so you have a greater understanding of what we're working with.

#### Answer the following questions in this file, with the results and the sql you wrote to get it.
-------------

##### How many people are from California?  
SELECT COUNT(*) FROM users WHERE state="CA";
14

##### Who has the most page views? How many do they have, and where are they from?
SELECT * FROM users ORDER BY page_views ASC;
Edison Mcintyre
19937
Mauriceville, ME

##### Who has the least page views? How many do they have and where are they from?
SELECT * FROM users ORDER BY page_views DESC;
Hattie Ross
16
Hubbard, MA

##### Who are the most recent visitors to the site?(at least 3)
SELECT * FROM users ORDER BY last_visit ASC;
Terrance Allen
Selina Hardy
Otha Ortiz

196|Otha Ortiz|imogene@afteragain.org|Butterfield|FL|2014-10-08|9814
259|Selina Hardy|nina.cassandra.leah@as.me|Seadrift|DC|2014-10-08|8288
364|Terrance Allen|isabelle.lesley@fixed.org|Alma|RI|2014-10-08|2424

##### Who was the first visitor?
Woodrow Duffy

163|Woodrow Duffy|ada.natasha@scissors.edu|Ingleside on the|MN|2013-10-08|9704

##### Who has an email address with the domain 'horse.edu'?
SELECT * FROM users WHERE email LIKE "%horse.edu%";
Fern Byers
Valentine Gonzales
11|Fern Byers|lino.jarod@hornhorse.edu|Magnolia|LA|2014-05-07|11770
400|Valentine Gonzales|steve.louis.jeremy@horse.edu|Valley View|SD|2014-09-06|11065

##### How many people are from the city Graford?
SELECT COUNT(*) FROM users WHERE city="Graford";
3

##### What are the names of all the cities that start with the letter V, in alphabetical order?
SELECT city FROM users ORDER BY city ASC;

Valley View
Valley View
Van
Van
Vega
Victoria
Victoria

##### What are the names and home cities for people searched for the word "drain"?

##### How many times was "trousers" a search term?
SELECT * FROM user_searches JOIN search_terms ON user_searches.term_id=search_terms.id WHERE search_terms.word = "trousers";
2


##### What were the search terms used by visitors who last visited on August 22 2014?

##### What was the most frequently used search term by people from Idaho?
SELECT search_terms.word, COUNT(*) FROM users JOIN user_searches JOIN search_terms ON user_searches.user_id = users.id AND user_searches.term_id = search_terms.id WHERE users.state="ID" GROUP BY search_terms.word;

##### What is the name of user 391, and what are his search terms?

