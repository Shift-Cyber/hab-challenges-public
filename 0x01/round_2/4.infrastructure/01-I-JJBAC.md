# Connector - 125pts
### 01-I-JJBAC
*Author: Nate Singer (Helix)*

Cloud computing is a way to use the internet to access and store data and software remotely. Instead of keeping files and programs on your own computer, you can access them through the internet on remote servers. This means you can access your files and programs from any device with an internet connection. It's like renting a space in a big computer building instead of having your own computer. It can also allow for cloud-based software that multiple users can access and collaborate on simultaneously. Cloud computing makes it easy to access and store data and software remotely.

## Teaching Points
1. What is MySQL?
2. How do I connect to a MySQL server?
3. What commands do I use to read out tables from a server?

## Challenge Prompt
Connect to the mysql server at `dyxvqmjwaj.qualifier.hackabit.com` and read out the flag. Here are some user accounts:

`user1:uyqhxgxcxd`
`user2:ehaigdexhh`
`user3:xfgyuvtapt`
`user4:tnvgijqxei`
`user5:hybplwmndy`

Root login is:
root:gbjhwbgdho

**Flag:** flag{oh_sql_my_sql}

## Solution Guide
1. connect with user 1
2. show databases
3. use challenge database
4. show tables
5. switch to user4 evenutally 
5. select * from flags

## Reference Material
### What is a MySQL server?
MySQL is a popular open-source relational database management system (RDBMS) used for storing and retrieving data. A MySQL server is a program that provides access to the MySQL database management system and serves as a central repository for data. It provides a way to store, organize, and access large amounts of information, making it ideal for use in a variety of applications, such as websites, online forums, content management systems, and more. The MySQL server is designed to be fast, reliable, and easy to use, and it runs on a variety of platforms, including Windows, Linux, and macOS.

### How do I connect to a MySQL server?
There are several ways to connect to a MySQL server, including the following:

1. Command Line Interface (CLI): The MySQL client can be used from the command line to connect to a MySQL server and interact with the database. To connect, you need to provide the following information:
- Hostname or IP address of the server
- Port number (default is 3306)
- MySQL username and password
2. PHP: If you want to connect to a MySQL server from a PHP script, you can use the PHP MySQL extension. This extension provides functions for connecting to a MySQL server, executing SQL statements, and fetching the results. Here is an example of how you can connect to a MySQL server using PHP:

```
<?php
$host = "hostname";
$user = "username";
$password = "password";
$dbname = "database_name";

// Create connection
$conn = mysqli_connect($host, $user, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
?>
```

3. Graphical User Interface (GUI) Tools: There are many GUI tools available that allow you to connect to a MySQL server and perform various operations, such as creating tables, inserting data, and running SQL queries. Some popular GUI tools include MySQL Workbench, phpMyAdmin, and HeidiSQL.

In all of these methods, you need to have the correct hostname or IP address, username, password, and database name to be able to connect to the MySQL server.

### What commands do I use to read out tables from a server?
In MySQL, you can use the SELECT statement to read out data from tables. Here are a few examples of how you can use the SELECT statement:

To retrieve all columns and rows from a table:
```
SELECT * FROM table_name;
```

To retrieve specific columns from a table:
```
SELECT column1, column2, column3 FROM table_name;
```

To retrieve data based on a condition:
```
SELECT * FROM table_name WHERE column_name = some_value;
```

To sort the data in ascending or descending order:
```
SELECT * FROM table_name ORDER BY column_name ASC;
SELECT * FROM table_name ORDER BY column_name DESC;
```

To limit the number of rows returned:
```
SELECT * FROM table_name LIMIT number_of_rows;
```

These are just a few examples of how you can use the SELECT statement to read data from tables in a MySQL database. The SELECT statement is very flexible and can be used in many different ways to retrieve data based on specific conditions and criteria.
