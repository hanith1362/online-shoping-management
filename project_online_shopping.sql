create database maindatabase2;
create database sellerdatabase2;
create database customerdatabase2;
use maindatabase2;
create table maindata(
registrationId int auto_increment primary key,
name_seller varchar(225),
email varchar(225),
licence_No int,
seller_phone_number varchar(225),
product_Id int,
product_cat varchar(225),
pro_name varchar(225),
pro_price float,
pro_quantity int,
spent_amount_by_customer int,
pro_desc varchar(225),
customer_Id int,
cus_username varchar(225),
cus_password int,
cus_name varchar(225),
cus_phone_number varchar(225),
cus_email varchar(225),
cus_history timestamp not null default current_timestamp);
use sellerdatabase2;
create table seller1(
name_seller varchar(225),
email varchar(225),
licence_No int,
seller_phone_number varchar(225),
product_Id int,
product_cat varchar(225),
pro_name varchar(225),
pro_price float,
pro_desc varchar(225),
pro_sold int,
pro_left int);
create table seller2(
name_seller varchar(225),
email varchar(225),
licence_No int,
seller_phone_number varchar(225),
product_Id int,
product_cat varchar(225),
pro_name varchar(225),
pro_price float,
pro_desc varchar(225),
pro_sold int,
pro_left int);
create table seller3(
name_seller varchar(225),
email varchar(225),
licence_No int,
seller_phone_number varchar(225),
product_Id int,
product_cat varchar(225),
pro_name varchar(225),
pro_price float,
pro_desc varchar(225),
pro_sold int,
pro_left int);
use customerdatabase2;
create table customercredentials(
customer_Id int auto_increment primary key,
cus_username varchar(225),
cus_password int,
cus_name varchar(225),
cus_phone_number varchar(225),
cus_email varchar(225));
show tables;
select * from seller1;
use sellerdatabase2;
insert into seller1(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_desc,pro_sold,pro_left,avg_selling_price) values
('sai','sai1234@gmail.com',1101,'9875643121',01,'fruits','apples',15,'Tasty shimla apples',0,100,0),
('sai','sai1234@gmail.com',1101,'9875643121',02,'fruits','bananas',5,'Tasty bananas',0,100,0),
('sai','sai1234@gmail.com',1101,'9875643121',03,'fruits','oranges',10,'Tasty oranges',0,100,0);
insert into seller2(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_desc,pro_sold,pro_left,avg_selling_price) values
('kiran','kiran1234@gmail.com',2101,'7995141415',01,'cosmetics','soap',40,'beauty is in your hands',0,100,0),
('kiran','kiran1234@gmail.com',2101,'7995141415',02,'cosmetics','face_wash',50,'Glow your skin',0,150,0),
('kiran','kiran1234@gmail.com',2101,'7995141415',03,'cosmetics','face_wipes',30,'wipe dirt skin',0,50,0);
select * from seller2;
insert into seller3(name_seller,email,licence_No,seller_phone_number,product_Id,product_cat,pro_name,pro_price,pro_desc,pro_sold,pro_left,avg_selling_price) values
('althaf','altaf1234@gmail.com',3101,'7075791014',01,'clothing','shirts',500,'style high',0,100,0),
('althaf','althaf1234@gmail.com',3101,'7075791014',02,'clothing','jeans',800,'Fly high with jeans',0,50,0),
('althaf','althaf1234@gmail.com',3101,'7075791014',03,'clothing','t-shirts',300,'cooool with the Tt-shirts',0,200,0);
select * from seller3;
use customerdatabase2;
select * from customercredentials;
use maindatabase2;
select * from maindata;
drop table maindata;
use sellerdatabase2;
select * from seller2; 
alter table seller2 drop column avg_selling_price;
alter table seller1 drop column avg_selling_price;
alter table seller3 drop column avg_selling_price;