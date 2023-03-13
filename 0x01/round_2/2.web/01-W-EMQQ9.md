# Injector - 125pts
### 01-W-EMQQ9
*Author: Nate Singer (Helix)*

Web applications, also known as "web apps," are software programs that run on the internet. They can be accessed using a web browser, like Google Chrome or Safari, on any device that has internet access. Web apps can do many things, like let you check your email, shop online, or play games. They are different from traditional desktop apps that you have to install on your computer. Web apps are built using programming languages like HTML, CSS, and JavaScript, and they run on servers that are connected to the internet. Examples of web apps include Google Docs, Facebook, and Instagram.

## Teaching Points
1. What is SQL injection?
2. Why is SQL injection one of the most dangerous vulenrabilities?
3. How to find an injection that will bypass filters

## Challenge Prompt
Someone didn't listen closely in programming class... yeah it was me I guess, I didn't. Here's a super secure login page, if you can bypass it you might even get a flag...

## Solution Guide
1. Notice input
2. See that you can break the page with characters like #
3. Identify that the payload is (' or 1=1#)

**Flag:** flag{maveric_pull_the_lever!}

## Reference Material
### How does a webserver store information?
A web server stores information in two main ways:
1. File System Storage: Websites and their assets, such as images, videos, and stylesheets, are stored as files on the web server's file system.
2. Database Storage: Websites also store information in databases, which are organized collections of data. This data can be structured in different ways, such as rows and columns in a table, or as a graph, depending on the type of database used. When a user visits a website, the web server retrieves the necessary data from the database and combines it with the files stored in the file system to generate the webpage that is sent to the user's browser.

### What is MySQL?
MySQL is a type of software that helps websites store and retrieve data. It's like a big library where all the information for a website is kept organized in books (tables). Each book has many pages (rows), and each page has different pieces of information (columns) about a specific topic.

For example, let's say you have a website about movies. You might have a book in the library that has information about each movie, such as its title, release date, director, and rating. Each page in this book would have information about one movie, and each column would have specific information, such as the title, release date, etc.

When someone visits the movie website, the website can use MySQL to search for specific movies and retrieve the information from the library. For example, if a user searches for all the movies released in 2022, MySQL would go to the book with movie information, find all the pages with movies released in 2022, and return that information to the website to be displayed to the user.

So, MySQL is a way for websites to store and retrieve information from a database, making it easy for users to find what they're looking for and for the website to show them the information they want to see.

### How does a webserver retrieve data from a database with MySQL?
Here's a simple SQL query that retrieves all data from a table called "movies":

```
SELECT * FROM movies;
```

The SELECT statement is used to specify which columns of data you want to retrieve, and the FROM clause specifies the table you want to retrieve data from. In this case, the * symbol means to retrieve all columns.

So, when you run this query, it will retrieve all the data from the movies table, and return it as a result set.

You can also retrieve specific columns by listing them after the SELECT keyword, like this:

```
SELECT title, release_date, director FROM movies;
```
This query will only retrieve the title, release_date, and director columns from the movies table.

You can also select entries where a condition occurs:
```
SELECT * from movies WHERE title="Hackers";
```

### What is SQLi?
SQL injection is a type of cyber attack that takes advantage of vulnerabilities in a website's code to inject malicious SQL (Structured Query Language) commands into the database that stores the website's data. The attacker then manipulates these commands to perform unauthorized actions, such as extracting sensitive data, modifying data, or executing system-level commands on the server.

SQL injection attacks often occur when a website takes user input, such as data entered into a form, and directly inserts it into an SQL query without first validating or escaping the input. This can allow an attacker to craft a malicious input that is interpreted as part of the SQL query, leading to unintended and potentially harmful consequences.

SQL injection is a serious security threat, and it is important for web developers to take steps to prevent SQL injection attacks by using proper input validation, parameterized queries, and other security measures.