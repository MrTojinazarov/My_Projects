CREATE DATABASE Liberary;
USE Liberary;

CREATE TABLE books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30),
    author VARCHAR(50),
    genre VARCHAR(30),
    quantity INT
);

INSERT INTO books (name, author, genre, quantity) VALUES
("O'tkan kunlar", "Abdulla Qodiriy", "drama", 25),
("Mehrobdan chayon", "Abdulla Qodiriy", "roman", 30),
("Kecha va kunduz", "Cho'lpon", "drama", 28);

CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(30) UNIQUE,
    password VARCHAR(30)
);

INSERT INTO users(login, password) VALUES
('Sirojiddin', "mr2344");