create database bookmyshow;

use bookmyshow;

create table sign_up(
	name varchar(200) not null unique,
    email varchar(200) not null unique,
    password varchar(20) not null 
    );
    
show tables;
select * from sign_up;

DROP TABLE IF EXISTS sign_up;