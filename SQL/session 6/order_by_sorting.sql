-- SESSION 6 - ORDER BY + Sorting
use music_streaming_app;

-- QUESTION 1
-- Display all products sorted by price
-- from lowest to highest

SELECT *
FROM products
ORDER BY price ASC;


-- QUESTION 2
-- Display the top 5 most expensive products

SELECT *
FROM products
ORDER BY price DESC
LIMIT 5;


-- QUESTION 3
-- Sort movies by latest release year first
-- and then by highest rating

SELECT title, release_year, rating
FROM movies
ORDER BY release_year DESC, rating DESC;


-- QUESTION 4
-- Display the first 10 restaurants
-- sorted alphabetically by name

SELECT *
FROM restaurants
ORDER BY name ASC
LIMIT 10;


-- QUESTION 5
-- Display the top 3 trending songs.
-- If play_count is the same, the recently added
-- song should come first.

SELECT *
FROM songs
ORDER BY play_count DESC, added_date DESC
LIMIT 3;