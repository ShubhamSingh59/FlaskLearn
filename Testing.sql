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
insert into jobs (id, title, location)
values ('2' , 'Web Dev', 'Jaipur');
select * from jobs;