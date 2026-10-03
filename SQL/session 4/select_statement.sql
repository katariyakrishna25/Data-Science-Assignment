-- SESSION 4 - SELECT Statement Basics


-- QUESTION 1
-- Create MusicPlaylist table

CREATE TABLE MusicPlaylist (
    id INT PRIMARY KEY,
    song_name VARCHAR(100),
    artist VARCHAR(100),
    genre VARCHAR(50),
    duration INT
);


-- Insert 5 sample songs

INSERT INTO MusicPlaylist (id, song_name, artist, genre, duration)
VALUES
(1, 'Kesariya', 'Arijit Singh', 'Bollywood', 268),
(2, 'Tum Hi Ho', 'Arijit Singh', 'Bollywood', 262),
(3, 'Apna Bana Le', 'Arijit Singh', 'Bollywood', 261),
(4, 'Heeriye', 'Jasleen Royal', 'Pop', 191),
(5, 'Chaleya', 'Arijit Singh', 'Bollywood', 201);


-- Display all columns and all songs

SELECT *
FROM MusicPlaylist;


-- QUESTION 2
-- Display only song_name and artist
-- Show first 3 records

SELECT song_name, artist
FROM MusicPlaylist
LIMIT 3;


-- QUESTION 3
-- Display unique restaurant names from FoodOrders

CREATE TABLE FoodOrders (
    id INT PRIMARY KEY,
    restaurant VARCHAR(100),
    food_item VARCHAR(100),
    order_date DATE
);


-- Insert sample FoodOrders data

INSERT INTO FoodOrders (id, restaurant, food_item, order_date)
VALUES
(1, 'Spice Hub', 'Paneer Tikka', '2026-09-01'),
(2, 'Food Point', 'Pizza', '2026-09-02'),
(3, 'Spice Hub', 'Biryani', '2026-09-03'),
(4, 'Burger King', 'Burger', '2026-09-04'),
(5, 'Food Point', 'Pasta', '2026-09-05');


-- Display unique restaurant names

SELECT DISTINCT restaurant
FROM FoodOrders;


-- QUESTION 4
-- Use column aliases

SELECT
    food_item AS Dish,
    order_date AS `Date Ordered`
FROM FoodOrders;


-- QUESTION 5
-- Correct query using DISTINCT and LIMIT

SELECT DISTINCT food_item, restaurant
FROM FoodOrders
LIMIT 2;