
-- SESSION 9 - JOINS - Part 1


-- QUESTION 1
-- Create restaurants and dishes tables.
-- Insert at least 3 restaurants and 2-3 dishes for each restaurant.

USE foodie_app;

CREATE TABLE restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE dishes (
    id INT PRIMARY KEY,
    restaurant_id INT,
    dish_name VARCHAR(100),
    price DECIMAL(10,2)
);

INSERT INTO restaurants (id, name, city)
VALUES
(1, 'Spice Garden', 'Ahmedabad'),
(2, 'Food Corner', 'Surat'),
(3, 'Pizza House', 'Mumbai'),
(4, 'Tasty Bites', 'Vadodara');

INSERT INTO dishes (id, restaurant_id, dish_name, price)
VALUES
(101, 1, 'Paneer Tikka', 250),
(102, 1, 'Veg Biryani', 220),
(103, 1, 'Dal Makhani', 180),
(104, 2, 'Gujarati Thali', 300),
(105, 2, 'Pav Bhaji', 150),
(106, 2, 'Masala Dosa', 120),
(107, 3, 'Margherita Pizza', 280),
(108, 3, 'Farmhouse Pizza', 350),
(109, 3, 'Garlic Bread', 130);


-- QUESTION 2
-- INNER JOIN: Display dishes with restaurant name and city.

SELECT
    dishes.dish_name,
    restaurants.name AS restaurant_name,
    restaurants.city,
    dishes.price
FROM restaurants
INNER JOIN dishes
ON restaurants.id = dishes.restaurant_id;


-- QUESTION 3
-- LEFT JOIN: Display all restaurants, even if they have no dishes.

SELECT
    restaurants.name AS restaurant_name,
    restaurants.city,
    dishes.dish_name,
    dishes.price
FROM restaurants
LEFT JOIN dishes
ON restaurants.id = dishes.restaurant_id;


-- QUESTION 4
-- RIGHT JOIN: Display all dishes, including dishes
-- that do not match any restaurant.

-- First, insert a dish with an invalid restaurant_id.

INSERT INTO dishes (id, restaurant_id, dish_name, price)
VALUES
(110, 99, 'Unknown Special Dish', 199);

SELECT
    dishes.dish_name,
    dishes.price,
    dishes.restaurant_id,
    restaurants.name AS restaurant_name
FROM restaurants
RIGHT JOIN dishes
ON restaurants.id = dishes.restaurant_id;


-- QUESTION 5
-- Show all playlists, even if some playlists are empty.
-- Use LEFT JOIN.

CREATE TABLE playlists (
    id INT PRIMARY KEY,
    playlist_name VARCHAR(100)
);

CREATE TABLE songs (
    id INT PRIMARY KEY,
    playlist_id INT,
    song_name VARCHAR(100)
);

INSERT INTO playlists (id, playlist_name)
VALUES
(1, 'My Favorites'),
(2, 'Workout Songs'),
(3, 'Relaxing Music');

INSERT INTO songs (id, playlist_id, song_name)
VALUES
(1, 1, 'Kesariya'),
(2, 1, 'Apna Bana Le'),
(3, 3, 'Perfect');

SELECT
    playlists.playlist_name,
    songs.song_name
FROM playlists
LEFT JOIN songs
ON playlists.id = songs.playlist_id;
