CREATE DATABASE Blogpost;

USE Blogpost;

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY Key,
    person VARCHAR(50),
    phone VARCHAR(30),
    login VARCHAR(30) UNIQUE,
    password VARCHAR(30)
);

CREATE TABLE Blog_post(
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(30),
    post VARCHAR(2048),
    datetime VARCHAR(50)
);

INSERT INTO Blog_post(login, post, datetime) VALUES ('Sirojiddin', "Axvolim zor", "Sat Aug 24 10:58:49 2024");