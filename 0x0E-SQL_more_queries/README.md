# 0x0E. SQL - More queries

## GENERAL

<ol>
	<li>How to create a new MySQL user</li>
	<li>How to manage privileges for a user to a database or table</li>
	<li>What’s a <code>PRIMARY KEY</code></li>
	<li>What’s a <code>FOREIGN KEY</code></li>
	<li>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</li>
	<li>How to retrieve datas from multiple tables in one request</li>
	<li>What are subqueries</li>
	<li>What are <code>JOIN</code> and <code>UNION</code></li>
</ol>

## INTRODUCTION TO FILES

0.	[**0-privileges.sql**:](#0-privilegessql) Script that lists all privileges of the MySQL users <code>user_0d_1</code> and <code>user_0d_2</code> on your server (in <code>localhost</code>).
1.	[**1-create_user.sql**:](#1-create_usersql) Script that creates the MySQL server user <code>user_0d_1</code>.
2.	[**2-create_read_user.sql**:](#2-create_read_usersql) Script that creates the database <code>hbtn_0d_2</code> and the user <code>user_0d_2</code>.
3.	[**3-force_name.sql**:](#3-force_namesql) Script that creates the table <code>force_name</code> on your MySQL server.
4.	[**4-never_empty.sql**:](#4-never_emptysql) Script that creates the table <code>id_not_null</code> on your MySQL server.
5.	[**5-unique_id.sql**:](#5-unique_idsql) Script that creates the table <code>unique_id</code> on your MySQL server.
6.	[**6-states.sql**:](#6-statessql) Script that creates the database <code>hbtn_0d_usa</code> and the table <code>states</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.
7.	[**7-cities.sql**:](#7-citiessql) Script that creates the database <code>hbtn_0d_usa</code> and the table <code>cities</code> (in the database <code>hbtn_0d_usa</code>) on your MySQL server.
8.	[**8-cities_of_california_subquery.sql**:](#8-cities_of_california_subquerysql) Script that lists all the cities of California that can be found in the database <code>hbtn_0d_usa</code>.
9.	[**9-cities_by_state_join.sql**:](#9-cities_by_state_joinsql) Script that lists all cities contained in the database <code>hbtn_0d_usa</code>.
10.	[**10-genre_id_by_show.sql**:](#10-genre_id_by_showsql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a>script that lists all shows contained in <code>hbtn_0d_tvshows</code> that have at least one genre linked.
11.	[**11-genre_id_all_shows.sql**:](#11-genre_id_all_showssql) Import the database dump of <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>10-genre_id_by_show.sql</code>)script that lists all shows contained in the database <code>hbtn_0d_tvshows</code>.
12.	[**12-no_genre.sql**:](#12-no_genresql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>11-genre_id_all_shows.sql</code>)script that lists all shows contained in <code>hbtn_0d_tvshows</code> without a genre linked.
13.	[**13-count_shows_by_genre.sql**:](#13-count_shows_by_genresql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>12-no_genre.sql</code>)script that lists all genres from <code>hbtn_0d_tvshows</code> and displays the number of shows linked to each.
14.	[**14-my_genres.sql**:](#14-my_genressql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>13-count_shows_by_genre.sql</code>)script that uses the <code>hbtn_0d_tvshows</code> database to lists all genres of the show <code>Dexter</code>.
15.	[**15-comedy_only.sql**:](#15-comedy_onlysql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>14-my_genres.sql</code>)script that lists all Comedy shows in the database <code>hbtn_0d_tvshows</code>.
16.	[**16-shows_by_genre.sql**:](#16-shows_by_genresql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>15-comedy_only.sql</code>)script that lists all shows, and all genres linked to that show, from the database <code>hbtn_0d_tvshows</code>.
17.	[**100-not_my_genres.sql**:](#100-not_my_genressql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>16-shows_by_genre.sql</code>)script that uses the <code>hbtn_0d_tvshows</code> database to list all genres not linked to the show <code>Dexter</code>
18.	[**101-not_a_comedy.sql**:](#101-not_a_comedysql) Import the database dump from <code>hbtn_0d_tvshows</code> to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" title="download" target="_blank">download</a> (same as <code>100-not_my_genres.sql</code>)script that lists all shows without the genre <code>Comedy</code> in the database <code>hbtn_0d_tvshows</code>.
19.	[**102-rating_shows.sql**:](#102-rating_showssql) Import the database <code>hbtn_0d_tvshows_rate</code> dump to your MySQL server <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql" title="download" target="_blank">download</a>script that lists all shows from <code>hbtn_0d_tvshows_rate</code> by their rating.
