# 0x0A. Python - Inheritance

## GENERAL

<ol>
	<li>Why Python programming is awesome </li>
	<li>What is a superclass, baseclass or parentclass</li>
	<li>What is a subclass</li>
	<li>How to list all attributes and methods of a class or instance</li>
	<li>When can an instance have new attributes</li>
	<li>How to inherit class from another</li>
	<li>How to define a class with multiple base classes </li>
	<li>What is the default class every class inherit from</li>
	<li>How to override a method or attribute inherited from the base class</li>
	<li>Which attributes or methods are available by heritage to subclasses</li>
	<li>What is the purpose of inheritance</li>
	<li>What are, when and how to use <code>isinstance</code>, <code>issubclass</code>, <code>type</code> and <code>super</code> built-in functions</li>
</ol>

## Resources
##### Read or watch:

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## INTRODUCTION TO FILES

0.	[**0-lookup.py**:](#0-lookuppy) Function that returns the list of available attributes and methods of an object
1.	[**1-my_list.py, tests/1-my_list.txt**:](#1-my_listpy-tests1-my_listtxt) Class <code>MyList</code> that inherits from <code>list</code>
2.	[**2-is_same_class.py**:](#2-is_same_classpy) Function that returns <code>True</code> if the object is <em>exactly</em> an instance of the specified class ; otherwise <code>False</code>.
3.	[**3-is_kind_of_class.py**:](#3-is_kind_of_classpy) Function that returns <code>True</code> if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise <code>False</code>.
4.	[**4-inherits_from.py**:](#4-inherits_frompy) Function that returns <code>True</code> if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise <code>False</code>.
5.	[**5-base_geometry.py**:](#5-base_geometrypy) An empty class <code>BaseGeometry</code>.
6.	[**6-base_geometry.py**:](#6-base_geometrypy) Class <code>BaseGeometry</code> (based on <code>5-base_geometry.py</code>).
7.	[**7-base_geometry.py, tests/7-base_geometry.txt**:](#7-base_geometrypy-tests7-base_geometrytxt) Class <code>BaseGeometry</code> (based on <code>6-base_geometry.py</code>).
8.	[**8-rectangle.py**:](#8-rectanglepy) Class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
9.	[**9-rectangle.py**:](#9-rectanglepy) Class <code>Rectangle</code> that inherits from <code>BaseGeometry</code> (<code>7-base_geometry.py</code>).
(task based on <code>8-rectangle.py</code>)
10.	[**10-square.py**:](#10-squarepy) Class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>)
11.	[**11-square.py**:](#11-squarepy) Class <code>Square</code> that inherits from <code>Rectangle</code> (<code>9-rectangle.py</code>).
(task based on <code>10-square.py</code>).
12.	[**100-my_int.py**:](#100-my_intpy) Class <code>MyInt</code> that inherits from <code>int</code>
13.     [**101-add_attribute.py**:](#101-add_attributepy) Function that adds a new attribute to an object if it’s possible
