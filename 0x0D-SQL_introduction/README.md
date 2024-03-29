# 0x0D. SQL - Introduction

## GENERAL

<ol>
	<li>What’s a database</li>
	<li>What’s a relational database</li>
	<li>What does SQL stand for</li>
	<li>What’s MySQL</li>
	<li>How to create a database in MySQL</li>
	<li>What does <code>DDL</code> and <code>DML</code> stand for</li>
	<li>How to <code>CREATE</code> or <code>ALTER</code> a table</li>
	<li>How to <code>SELECT</code> data from a table</li>
	<li>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</li>
	<li>What are <code>subqueries</code></li>
	<li>How to use MySQL functions</li>
</ol>

## RESOURCE

- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM) 
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
- [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)(no need to read the chapter “Privileges”)
- [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
- [SQL technique: functions](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [installing MySQL in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

## Tasks

* **0. List databases**
  * [0-list_databases.sql](./0-list_databases.sql): MySQL script that lists all databases.

* **1. Create a database**
  * [1-create_database.sql](./1-create_database.sql): MySQL script that creates the database `hbtn_0c_0`.

* **2. Delete a database**
  * [2-remove_databases.sql](./2-remove_databases.sql): MySQL script that deletes the database `hbtn_0c_0`.

* **3. List tables**
  * [3-list_tables.sql](./3-list_tables.sql): MySQL script that lists all tables.

* **4. First table**
  * [4-first_table.sql](./4-first_table.sql): MySQL script that creates a table `first_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)

* **5. Full description**
  * [5-full_table.sql](./5-full_table.sql): MySQL script that prints the full description of the table `first_table`.

* **6. List all in table**
  * [6-list_values.sql](./6-list_values.sql): MySQL script that lists all rows of the table
  `first_table`.

* **7. First add**
  * [7-insert_value.sql](./7-insert_value.sql): MySQL script that inserts a new row in the table `first_table`.
  * Description:
    * `id` = `89`
    * `name` = `Best School`

* **8. Count 89**
  * [8-count_89.sql](./8-count_89.sql): MySQL script that displays the number records with `id = 89` in the table `first_table`.

* **9. Full creation**
  * [9-full_creation.sql](./9-full_creation.sql): MySQL script that creates and fills a table `second_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)
    * `score`: INT
  * Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

* **10. List by best**
  * [10-top_score.sql](./10-top_score.sql): MySQL script that lists the `score` and `name` of all records of the table `second_table` in order of descending `score`.

* **11. Select the best**
  * [11-best_score.sql](./11-best_score.sql): MySQL script that lists the `score` and `name` of all records with a `score >= 10` in the table `second_table` in order of descending score.

* **12. Cheating is bad**
  * [12-no_cheating.sql](./12-no_cheating.sql): MySQL script that updates the score of Bob to 10 the table `second_table`.

* **13. Score too low**
  * [13-change_class.sql](./13-change_class.sql): MySQL script that removes all records with a `score <= 5` in the table `second_table`.

* **14. Average**
  * [14-average.sql](./14-average.sql): MySQL script that computes the average `score` of all records in the table `second_table`.

* **15. Number by score**
  * [15-groups.sql](./15-groups.sql): MySQL script that lists the `score` and number of records with the same score in the table `second_table` in order of descending count.

* **16. Say my name**
  * [16-no_link.sql](./16-no_link.sql): MySQL script that lists the `score` and `name` of all records in the table `second_table` in order of descending `score`.
  * Does not display rows without a `name` value.

* **17. Go to UTF8**
  * [100-move_to_utf8.sql](./100-move_to_utf8.sql): MySQL script that converts the `hbtn_0c_0` database to UTF8.

* **18. Temperatures #0**
  * [101-avg_temperatures.sql](./101-avg_temperatures.sql): MySQL script that displays the average temperature (Fahrenheit) by city in descending order.

* **19. Temperatures #1**
  * [102-top_city.sql](./102-top_city.sql): MySQL script that displays the three cities with the highest average temperature from July to August in descending order.

* **20. Temperature #2**
  * [103-max_state.sql](./103-max_state.sql): MySQL script that displays the max temperature of each state in order of state name.

## FILES

### 0-list_databases.sql

**<p>Script that lists all databases of your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$ 
</code></pre>

### 1-create_database_if_missing.sql

**<p>Script that creates the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

### 2-remove_database.sql

**<p>Script that deletes the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$ 
</code></pre>

### 3-list_tables.sql

**<p>Script that lists all the tables of a database in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
guillaume@ubuntu:~/$ 
</code></pre>

### 4-first_table.sql

**<p>Script that creates a table called <code>first_table</code> in the current database in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 
</code></pre>

### 5-full_table.sql

**<p>Script that prints the full description of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$ 
</code></pre>

### 6-list_values.sql

**<p>Script that lists all rows of the table <code>first_table</code> from the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

### 7-insert_value.sql

**<p>Script that inserts a new row in the table <code>first_table</code> (database <code>hbtn_0c_0</code>) in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
89  Holberton School
89  Holberton School
guillaume@ubuntu:~/$ 
</code></pre>

### 8-count_89.sql

**<p>Script that displays the number of records with <code>id = 89</code> in the table <code>first_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 
</code></pre>

### 9-full_creation.sql

**<p>Script that creates a table <code>second_table</code> in the database <code>hbtn_0c_0</code> in your MySQL server and add multiples rows.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>

### 10-top_score.sql

**<p>Script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>

### 11-best_score.sql

**<p>Script that lists all records with a <code>score &gt;= 10</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 
</code></pre>

### 12-no_cheating.sql

**<p>Script that updates the score of Bob to <code>10</code> in the table <code>second_table</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>

### 13-change_class.sql

**<p>Script that removes all records with a <code>score &lt;= 5</code> in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 
</code></pre>

### 14-average.sql

**<p>Script that computes the score average of all records in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 
</code></pre>

### 15-groups.sql

**<p>Script that lists the number of records with the same score in the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 
</code></pre>

### 16-no_link.sql

**<p>Script that lists all records of the table <code>second_table</code> of the database <code>hbtn_0c_0</code> in your MySQL server.</p><p>In this example, new data have been added to the table <code>second_table</code>.</p>**

<pre><code>guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 
</code></pre>

### 100-move_to_utf8.sql

**<p>Script that converts <code>hbtn_0c_0</code> database to UTF8 (<code>utf8mb4</code>, collate <code>utf8mb4_unicode_ci</code>) in your MySQL server.</p><p>You need to convert all of the following to <code>UTF8</code></p>**

<pre><code>guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$ 
</code></pre>

### 101-avg_temperatures.sql

**<p>Import in <code>hbtn_0c_0</code> database this table dump <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" title="download" target="_blank">download</a></p><p>script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).</p>**

<pre><code>guillaume@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$ 
</code></pre>

### 102-top_city.sql

**<p>Import in <code>hbtn_0c_0</code> database this table dump <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" title="download" target="_blank">download</a> (same as <code>Temperatures #0</code>)</p><p>script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)</p>**

<pre><code>guillaume@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
guillaume@ubuntu:~/$ 
</code></pre>

### 103-max_state.sql

**<p>Import in <code>hbtn_0c_0</code> database this table dump <a href="https//s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" title="download" target="_blank">download</a> (same as <code>Temperatures #0</code>)</p><p>script that displays the max temperature of each state (ordered by State name).</p>**

<pre><code>guillaume@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$ 
</code></pre>					      

