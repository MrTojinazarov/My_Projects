CREATE DATABASE product_list;

USE product_list;

CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(30) UNIQUE,
    password VARCHAR(30)
);

