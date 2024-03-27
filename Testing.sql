create database testdb;
use testdb;
create table jobs (
	id int not null,
    title varchar(250) not null,
    location varchar(250) not null,
    salary int,
	currency varchar(10),
    primary key (id)
);
create table user(
	id int not null unique,
    username varchar(250) not null unique,
    email varchar(500) not null unique,
    password varchar(100) not null,
    primary key (id)
);
select * from user;
insert into jobs (id, title, location)
values ('2' , 'Web Dev', 'Jaipur');
insert into jobs (id, title, location)
values	('3' , 'Web Dev', 'Ramnagar');
select * from jobs;

select @@hostname;