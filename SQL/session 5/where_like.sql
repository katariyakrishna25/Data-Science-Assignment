-- SESSION 5 - WHERE Clause + LIKE
use music_streaming_app;


-- QUESTION 1
-- Create Restaurants table

CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine VARCHAR(100),
    rating DECIMAL(2,1),
    city VARCHAR(50)
);


-- Insert 5 sample restaurants

INSERT INTO Restaurants (id, name, cuisine, rating, city)
VALUES
(1, 'Swagat', 'South Indian', 4.5, 'Ahmedabad'),
(2, 'Spice Hub', 'Chinese', 4.2, 'Surat'),
(3, 'Swadisht', 'Gujarati', 4.0, 'Ahmedabad'),
(4, 'Pizza Palace', 'Italian', 3.8, 'Surat'),
(5, 'Dragon House', 'Chinese', 4.6, 'Mumbai');


-- QUESTION 2
-- Find restaurants with rating greater than 4.0
-- and located in Ahmedabad or Surat

SELECT *
FROM Restaurants
WHERE rating > 4.0
AND city IN ('Ahmedabad', 'Surat');


-- QUESTION 3
-- Find restaurants whose names start with 'Swa'

SELECT *
FROM Restaurants
WHERE name LIKE 'Swa%';


-- QUESTION 4
-- Find restaurants with rating between 3.5 and 4.5

SELECT *
FROM Restaurants
WHERE rating BETWEEN 3.5 AND 4.5;


-- QUESTION 5
-- Find restaurants having Chinese, Italian
-- or South Indian cuisine

SELECT *
FROM Restaurants
WHERE cuisine IN ('Chinese', 'Italian', 'South Indian');