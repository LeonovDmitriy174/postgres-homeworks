-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) not NULL,
	last_name varchar(100) not NULL,
	title varchar(100) not NULL,
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(100) not NULL,
	contact_name varchar(100) not NULL
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	employee_id int REFERENCES employees(employee_id) not NULL,
	customer_id varchar(10) REFERENCES customers(customer_id) not NULL,
	order_date date not NULL,
	ship_city varchar(100) not NULL
);