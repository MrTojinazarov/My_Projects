CREATE DATABASE USERS;

USE USERS;

CREATE TABLE USER (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    country VARCHAR(50)
);


INSERT INTO USER (name, city, country) VALUES
('Azizbek', 'Tashkent', 'Uzbekistan'),
('Nodira', 'Samarkand', 'Uzbekistan'),
('Murod', 'Bukhara', 'Uzbekistan'),
('Dilnoza', 'Khiva', 'Uzbekistan'),
('Jamshid', 'Namangan', 'Uzbekistan'),
('Shoxrux', 'Fergana', 'Uzbekistan'),
('Madina', 'Andijan', 'Uzbekistan'),
('Aziza', 'Kokand', 'Uzbekistan'),
('Rustam', 'Nukus', 'Uzbekistan'),
('Laylo', 'Qarshi', 'Uzbekistan');


INSERT INTO USER (name, city, country) VALUES
('Azizbek', 'Moskva', 'Russia'),
('Nodira', 'Leningrad', 'Russia'),
('Murod', 'Nyu York', 'USA'),
('Dilnoza', 'Washington', 'USA'),
('Jamshid', 'Dehli', 'India');


-- 1 - topshiriq;

SELECT country, count(city) as city_country
From USER
Group by country;

-- 2 - topshiriq 

SELECT country, COUNT(*) AS user_count
FROM USER
GROUP BY country
ORDER BY user_count DESC
LIMIT 2;

