DROP TABLE IF EXISTS users;
CREATE TABLE users (
email VARCHAR(50) NOT NULL,
pwd VARCHAR(50) NOT NULL,
fname VARCHAR(50) DEFAULT '' NOT NULL,
lname VARCHAR(50) DEFAULT '' NOT NULL,
PRIMARY KEY(email)
);

DROP TABLE IF EXISTS address_info;
CREATE TABLE address_info (
email varchar(50),
address varchar(50),
zipcode int,
state varchar(50),
city varchar(50),
foreign key(email) references users(email)
);

DROP TABLE IF EXISTS payment_info;
CREATE TABLE payment_info(
email varchar(50),
card_number int,
cvc int,
foreign key(email) references users(email)
);

DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions(
email varchar(50),
amount int,
tid int NOT NULL AUTO_INCREMENT,
foreign key(email) references users(email),
primary key(tid)
);

DROP TABLE IF EXISTS includes;
CREATE TABLE includes(
item_name varchar(50),
tid int,
count int,
foreign key(tid) references transactions(tid)
);

DROP TABLE IF EXISTS items;
CREATE TABLE items(
item_name varchar(50),
price decimal (4,2),
primary key(item_name)
);