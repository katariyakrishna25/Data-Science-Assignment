
-- SESSION 12 - CTE (WITH Clause)
-- QUESTION 1
-- Find all products with a rating above 4.5 using a CTE.

USE foodie_app;

CREATE TABLE Products (
    id INT PRIMARY KEY,
    product_name VARCHAR(100),
    rating DECIMAL(2,1)
);

INSERT INTO Products (id, product_name, rating)
VALUES
(1, 'Smartphone', 4.8),
(2, 'Laptop', 4.6),
(3, 'Headphones', 4.2),
(4, 'Smart Watch', 4.9),
(5, 'Keyboard', 4.4);

WITH TopRatedProducts AS (
    SELECT *
    FROM Products
    WHERE rating > 4.5
)
SELECT *
FROM TopRatedProducts;


-- QUESTION 2
-- Find Ahmedabad restaurants with delivery charges under 50.
-- First, use a subquery.

CREATE TABLE Restaurant (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    delivery_charge DECIMAL(6,2)
);

INSERT INTO Restaurant (id, name, city, delivery_charge)
VALUES
(1, 'Spice Garden', 'Ahmedabad', 30),
(2, 'Food Corner', 'Ahmedabad', 60),
(3, 'Pizza House', 'Surat', 25),
(4, 'Tasty Bites', 'Ahmedabad', 40);

-- Subquery version

SELECT *
FROM (
    SELECT *
    FROM Restaurant
    WHERE city = 'Ahmedabad'
) AS AhmedabadRestaurants
WHERE delivery_charge < 50;


-- CTE version

WITH AhmedabadRestaurants AS (
    SELECT *
    FROM Restaurant
    WHERE city = 'Ahmedabad'
)
SELECT *
FROM AhmedabadRestaurants
WHERE delivery_charge < 50;

-- The CTE version is easier to read because
-- the temporary result has a clear name.


-- QUESTION 3
-- Use two CTEs to find the top 3 most-followed users
-- and the top 3 most-liked posts in one result set.

CREATE TABLE Users (
    id INT PRIMARY KEY,
    username VARCHAR(100),
    followers INT
);

CREATE TABLE Posts (
    id INT PRIMARY KEY,
    user_id INT,
    post_name VARCHAR(100),
    likes INT
);

INSERT INTO Users (id, username, followers)
VALUES
(1, 'Krishna', 5000),
(2, 'Rahul', 3200),
(3, 'Priya', 7000),
(4, 'Amit', 2100),
(5, 'Neha', 4500);

INSERT INTO Posts (id, user_id, post_name, likes)
VALUES
(1, 1, 'Travel Photo', 500),
(2, 2, 'Food Reel', 900),
(3, 3, 'Dance Video', 1200),
(4, 4, 'Nature Photo', 300),
(5, 5, 'Fashion Reel', 1000);

WITH TopUsers AS (
    SELECT username, followers
    FROM Users
    ORDER BY followers DESC
    LIMIT 3
),
TopPosts AS (
    SELECT post_name, likes
    FROM Posts
    ORDER BY likes DESC
    LIMIT 3
)
SELECT
    'Top Users' AS list_type,
    username AS item_name,
    followers AS count_value
FROM TopUsers

UNION ALL

SELECT
    'Top Posts' AS list_type,
    post_name AS item_name,
    likes AS count_value
FROM TopPosts;


-- QUESTION 4
-- Generate dates for the next 7 days, including today.

WITH RECURSIVE DateList AS (
    SELECT CURDATE() AS booking_date

    UNION ALL

    SELECT DATE_ADD(booking_date, INTERVAL 1 DAY)
    FROM DateList
    WHERE booking_date < DATE_ADD(CURDATE(), INTERVAL 6 DAY)
)
SELECT booking_date
FROM DateList;


-- QUESTION 5
-- Refactor the query for users with more than
-- 1000 followers using a CTE.

-- Original query

SELECT *
FROM Users
WHERE followers > 1000;


-- CTE version

WITH PopularUsers AS (
    SELECT *
    FROM Users
    WHERE followers > 1000
)
SELECT *
FROM PopularUsers;
