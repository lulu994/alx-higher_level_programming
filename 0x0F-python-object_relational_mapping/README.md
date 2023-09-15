# 0x0F. Python - Object-relational mapping

## GENERAL

<ol>
	<li>Why Python programming is awesome</li>
	<li>How to connect to a MySQL database from a Python script</li>
	<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
	<li>How to <code>INSERT</code> rows in a MySQL table from a Python script </li>
	<li>What ORM means</li>
	<li>How to map a Python Class to a MySQL table</li>
</ol>

## RESOURCES:

 <ol>
	<li><a href="/rltoken/IqdjUaZ31ZfP6eT-lTyUkA" title="Object-relational mappers" target="_blank">Object-relational mappers</a> </li>
	<li><a href="/rltoken/rMJpVJ1_YjMWfvY00I7Kpw" title="mysqlclient/MySQLdb documentation" target="_blank">mysqlclient/MySQLdb documentation</a> (<em>please don’t pay attention to <code>_mysql</code></em>)</li>
	<li><a href="/rltoken/DJz5W6Y13-6qUSTPTGrHYw" title="MySQLdb tutorial" target="_blank">MySQLdb tutorial</a> </li>
	<li><a href="/rltoken/9JWveMwNKe3IUErdEbDsUQ" title="SQLAlchemy tutorial" target="_blank">SQLAlchemy tutorial</a> </li>
	<li><a href="/rltoken/E9dLS6Shaezq4ivnGxN_RA" title="SQLAlchemy" target="_blank">SQLAlchemy</a> </li>
	<li><a href="/rltoken/QFgtVxz2w-C1y1OB8uls1g" title="mysqlclient/MySQLdb" target="_blank">mysqlclient/MySQLdb</a> </li>
	<li><a href="/rltoken/I5bvhPGTOu3_-T-4jpN-hg" title="Introduction to SQLAlchemy" target="_blank">Introduction to SQLAlchemy</a> </li>
	<li><a href="/rltoken/UvaHESHeqlRA0Z0uQFi0_A" title="Flask SQLAlchemy" target="_blank">Flask SQLAlchemy</a> </li>
	<li><a href="/rltoken/Zb8Yc2WycLLYX8gnLlwZKw" title="10 common stumbling blocks for SQLAlchemy newbies" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a> </li>
	<li><a href="/rltoken/XHPAX7-ydSou2BLWHII8Vw" title="Python SQLAlchemy Cheatsheet" target="_blank">Python SQLAlchemy Cheatsheet</a> </li>
	<li><a href="/rltoken/aeLSQ039BhLhamU2BjqsOw" title="SQLAlchemy ORM Tutorial for Python Developers" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
	<li><a href="/rltoken/cmfi9C_nRXrmnwaJfCPyxA" title="SQLAlchemy Tutorial" target="_blank">SQLAlchemy Tutorial</a></li>
</ol>

## INTRODUCTION TO FILES :closed_book::closed_book::closed_book::

0.	[**0-select_states.py**:](#0-select_statespy) Script that lists all <code>states</code> from the database <code>hbtn_0e_0_usa</code>
1.	[**1-filter_states.py**:](#1-filter_statespy) Script that lists all <code>states</code> with a <code>name</code> starting with <code>N</code> (upper N) from the database <code>hbtn_0e_0_usa</code>
2.	[**2-my_filter_states.py**:](#2-my_filter_statespy) Script that takes in an argument and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument.
3.	[**3-my_safe_filter_states.py**:](#3-my_safe_filter_statespy) Wait, do you remember the previous task? Did you test <code>"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"</code> as an input?What? Empty?Yes, it’s an <a href="/rltoken/f6dtded2o4a09_WEQpLypw" title="SQL injection" target="_blank">SQL injection</a> to delete all records of a table…Once again, write a script that takes in arguments and displays all values in the <code>states</code> table of <code>hbtn_0e_0_usa</code> where <code>name</code> matches the argument. But this time, write one that is safe from MySQL injections!
4.	[**4-cities_by_state.py**:](#4-cities_by_statepy) Script that lists all <code>cities</code> from the database <code>hbtn_0e_4_usa</code>
5.	[**5-filter_cities.py**:](#5-filter_citiespy) Script that takes in the name of a state as an argument and lists all <code>cities</code> of that state, using the database <code>hbtn_0e_4_usa</code>
6.	[**model_state.py**:](#model_statepy) <img src="https//holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210401%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210401T013705Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=81da5420b5840eaa7cdece86ec76c6144b74d9256d296b39fa8c160bb7d03803" alt="" style="">python file that contains the class definition of a <code>State</code> and an instance <code>Base = declarative_base()</code>
7.	[**8-model_state_fetch_first.py**:](#8-model_state_fetch_firstpy) Script that prints the first <code>State</code> object from the database <code>hbtn_0e_6_usa</code>
8.	[**9-model_state_filter_a.py**:](#9-model_state_filter_apy) Script that lists all <code>State</code> objects that contain the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code>
9.	[**10-model_state_my_get.py**:](#10-model_state_my_getpy) Script that prints the <code>State</code> object with the <code>name</code> passed as argument from the database <code>hbtn_0e_6_usa</code>
10.	[**11-model_state_insert.py**:](#11-model_state_insertpy) Script that adds the <code>State</code> object “Louisiana” to the database <code>hbtn_0e_6_usa</code>
11.	[**12-model_state_update_id_2.py**:](#12-model_state_update_id_2py) Script that changes the name of a <code>State</code> object from the database <code>hbtn_0e_6_usa</code>
12.	[**13-model_state_delete_a.py**:](#13-model_state_delete_apy) Script that deletes all <code>State</code> objects with a name containing the letter <code>a</code> from the database <code>hbtn_0e_6_usa</code>
13.	[**model_city.py, 14-model_city_fetch_by_state.py**:](#model_citypy-14-model_city_fetch_by_statepy) Python file similar to <code>model_state.py</code> named <code>model_city.py</code> that contains the class definition of a <code>City</code>.Next, write a script <code>14-model_city_fetch_by_state.py</code> that prints all <code>City</code> objects from the database <code>hbtn_0e_14_usa</code>
