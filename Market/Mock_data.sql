CREATE DATABASE market;

USE market;

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(30) UNIQUE,
    password VARCHAR(30)
);

INSERT INTO users(login, password) VALUES
('Sirojiddin', 'mr2344');



CREATE TABLE items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    item VARCHAR(30) UNIQUE,
    price VARCHAR(30),
    quantity INT
);


INSERT INTO items(item, price, quantity) VALUES
('Makaron', "10000 so'm", '50'),
("Tarvuz", "9350 so'm", '120');