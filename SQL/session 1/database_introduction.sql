-- SESSION 1 - Database Introduction & SQL Basics


-- QUESTION 1
-- Create a database named music_streaming_app

CREATE DATABASE music_streaming_app;

USE music_streaming_app;


-- QUESTION 2
-- Create playlists table

CREATE TABLE playlists (
    playlist_id INT PRIMARY KEY,
    name VARCHAR(100),
    created_by VARCHAR(100)
);


-- QUESTION 3
-- Insert three sample playlists

INSERT INTO playlists (playlist_id, name, created_by)
VALUES
(1, 'Bollywood Hits', 'Amit'),
(2, 'Chill Vibes', 'Riya'),
(3, 'Workout Mix', 'Rahul');


-- QUESTION 4
-- Display all playlists created by Amit

SELECT *
FROM playlists
WHERE created_by = 'Amit';


-- QUESTION 5
-- Table, Row and Column example using a food delivery app

-- Table:
-- A table stores related data in rows and columns.
-- Example: A Zomato orders table can store order information.

-- Row:
-- A row represents one complete record.
-- Example: One row can contain one customer's order.

-- Column:
-- A column represents one type of information.
-- Example: order_id, customer_name, restaurant_name and order_value
-- can be columns in the orders table.


-- Display all playlists

SELECT * FROM playlists;