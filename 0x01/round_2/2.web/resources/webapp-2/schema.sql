/* create user for readonly access -- SELECT * FROM mysql.user */
CREATE USER 'webapp2user'@localhost IDENTIFIED BY 'password123';

/* create database -- show databases; */
CREATE DATABASE webapp2;

/* set readonly access -- show grants for webapp2user@localhost; */
GRANT SELECT ON webapp2.* TO 'webapp2user'@localhost;

/* reload the table */
FLUSH PRIVILEGES;

/* select database */
USE webapp2;

/* create table of users -- show tables; */
CREATE TABLE IF NOT EXISTS `users` (
    `user_id` MEDIUMINT NOT NULL AUTO_INCREMENT,
    `username` varchar(255) NOT NULL,
    `pwhash` varchar(255) NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/* add user records and flag -- select * from users; */
INSERT INTO `users` (user_id, username, pwhash) values (default,'singern','$2a$10$ShekzV0pcSJ6oDfzR0qw0Ojw6OMO66eCfp1y2QR6YWJpbxkf4.r1y');
INSERT INTO `users` (user_id, username, pwhash) values (default,'another_user','$2a$10$XCyABNUVNqLwAYCiKl0mRu1B8iDDZURJoaE6wr2Js/EYNL/39zH2G');
INSERT INTO `users` (user_id, username, pwhash) values (default,'flag_user','flag{maveric_pull_the_lever!}');
