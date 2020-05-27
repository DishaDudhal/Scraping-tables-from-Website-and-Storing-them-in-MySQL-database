create database scraping_sample;
show databases;
use scraping_sample;
grant all on scraping_sample.* to 'root'@'localhost';
show tables;
create table Planned_Outages (
Date_select varchar(255) collate utf8_unicode_ci default Null,
Sector_Type text collate utf8_unicode_ci default Null,
Station text collate utf8_unicode_ci default Null,
State text collate utf8_unicode_ci default Null,
Agency text collate utf8_unicode_ci default Null,
Unit_no text collate utf8_unicode_ci default Null,
Capacity text collate utf8_unicode_ci default Null,
Reason text collate utf8_unicode_ci default Null,
Outage_date text collate utf8_unicode_ci default Null,
Outage_time text collate utf8_unicode_ci default Null,
Expected_revival_date text collate utf8_unicode_ci default Null,
Inserted_at text collate utf8_unicode_ci default Null
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

show tables;
desc planned_outages;

select * from planned_outages;

select count(*) from planned_outages;

create table Planned (
Date_select varchar(255) collate utf8_unicode_ci default Null,
Sector_Type text collate utf8_unicode_ci default Null,
Station text collate utf8_unicode_ci default Null,
State text collate utf8_unicode_ci default Null,
Agency text collate utf8_unicode_ci default Null,
Unit_no text collate utf8_unicode_ci default Null,
Capacity text collate utf8_unicode_ci default Null,
Reason text collate utf8_unicode_ci default Null,
Outage_date text collate utf8_unicode_ci default Null,
Outage_time text collate utf8_unicode_ci default Null,
Expected_revival_date text collate utf8_unicode_ci default Null,
Inserted_at text collate utf8_unicode_ci default Null
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

select * from planned;
