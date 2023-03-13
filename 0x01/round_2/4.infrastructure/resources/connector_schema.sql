/* create users for readonly access */
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'uyqhxgxcxd';
CREATE USER 'user1'@'%' IDENTIFIED BY 'uyqhxgxcxd';

CREATE USER 'user2'@'localhost' IDENTIFIED BY 'ehaigdexhh';
CREATE USER 'user2'@'%' IDENTIFIED BY 'ehaigdexhh';

CREATE USER 'user3'@'localhost' IDENTIFIED BY 'xfgyuvtapt';
CREATE USER 'user3'@'%' IDENTIFIED BY 'xfgyuvtapt';

CREATE USER 'user4'@'localhost' IDENTIFIED BY 'tnvgijqxei';
CREATE USER 'user4'@'%' IDENTIFIED BY 'tnvgijqxei';

CREATE USER 'user5'@'localhost' IDENTIFIED BY 'hybplwmndy';
CREATE USER 'user5'@'%' IDENTIFIED BY 'hybplwmndy';

/* create database -- show databases; */
CREATE DATABASE challenge;

/* select database */
USE challenge;

/* create table of jokes -- show tables; */
CREATE TABLE IF NOT EXISTS `jokes` (
    `id` SMALLINT NOT NULL AUTO_INCREMENT,
    `rating` varchar(255) NOT NULL,
    `joke` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* add user records and flag -- select * from users; */
INSERT INTO `jokes` (id, rating, joke) values (default,'true','Any joke can be a one-liner with enough semicolons');
INSERT INTO `jokes` (id, rating, joke) values (default,'good','I � Unicode');
INSERT INTO `jokes` (id, rating, joke) values (default,'numeric','Why dont jokes work in octal? Because 7 10 11');
INSERT INTO `jokes` (id, rating, joke) values (default,'meh','I could tell you a joke about UDP but I dont know if you would get it.');
INSERT INTO `jokes` (id, rating, joke) values (default,'better','Its better than my TCP joke - I have to keep telling it over and over again.');
INSERT INTO `jokes` (id, rating, joke) values (default,'rhythmic','Old MacDonald had a char*, s-t-d-i-o!');
INSERT INTO `jokes` (id, rating, joke) values (default,'nice','walks UDP package into bar A');
INSERT INTO `jokes` (id, rating, joke) values (default,'exceptional','Perl');
INSERT INTO `jokes` (id, rating, joke) values (default,'meh','The mark of the beast: rw-rw-rw-');
INSERT INTO `jokes` (id, rating, joke) values (default,'good','.titanic { float:none;}');
INSERT INTO `jokes` (id, rating, joke) values (default,'okay','There are 10 kinds of people. Those that understand binary and those that dont.');


/* create table of users -- show tables; */
CREATE TABLE IF NOT EXISTS `animals` (
    `id` MEDIUMINT NOT NULL AUTO_INCREMENT,
    `animal` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `animals` (id, animal) values (default,'tiger');
INSERT INTO `animals` (id, animal) values (default,'blue-whale');
INSERT INTO `animals` (id, animal) values (default,'vaquita');
INSERT INTO `animals` (id, animal) values (default,'rhinoceros');
INSERT INTO `animals` (id, animal) values (default,'water-buffalo');


/* create table of flags -- show tables; */
CREATE TABLE IF NOT EXISTS `flags` (
    `id` MEDIUMINT NOT NULL AUTO_INCREMENT,
    `flag` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `flags` (id, flag) values (default,'flag{nah}');
INSERT INTO `flags` (id, flag) values (default,'flag{oh_sql_my_sql}');


/* set readonly access -- show grants for x@localhost; */
GRANT SELECT ON challenge.jokes TO 'user1'@'localhost';
GRANT SELECT ON challenge.jokes TO 'user1'@'%';
GRANT SELECT ON challenge.animals TO 'user1'@'localhost';
GRANT SELECT ON challenge.animals TO 'user1'@'%';

GRANT SELECT ON challenge.jokes TO 'user2'@'localhost';
GRANT SELECT ON challenge.jokes TO 'user2'@'%';

GRANT SELECT ON challenge.jokes TO 'user3'@'localhost';
GRANT SELECT ON challenge.jokes TO 'user3'@'%';
GRANT SELECT ON challenge.animals TO 'user3'@'localhost';
GRANT SELECT ON challenge.animals TO 'user3'@'%';

GRANT SELECT ON challenge.flags TO 'user4'@'localhost';
GRANT SELECT ON challenge.flags TO 'user4'@'%';

GRANT SELECT ON challenge.animals TO 'user5'@'localhost';
GRANT SELECT ON challenge.animals TO 'user5'@'%';

/* reload the table */
FLUSH PRIVILEGES;
