
-- SESSION 10 - JOINS - Part 2

-- QUESTION 1
-- Create Influencers and Collaborations tables.
-- Display all influencers and their collaboration partners,
-- including influencers with no collaborations.

USE foodie_app;

CREATE TABLE Influencers (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE Collaborations (
    id INT PRIMARY KEY,
    influencer1_id INT,
    influencer2_id INT,
    collab_date DATE
);

INSERT INTO Influencers (id, name)
VALUES
(1, 'Krishna'),
(2, 'Rahul'),
(3, 'Priya'),
(4, 'Amit');

INSERT INTO Collaborations
(id, influencer1_id, influencer2_id, collab_date)
VALUES
(1, 1, 2, '2026-01-10'),
(2, 2, 3, '2026-02-15');

SELECT
    i1.name AS influencer_name,
    i2.name AS partner_name,
    c.collab_date
FROM Influencers i1
LEFT JOIN Collaborations c
    ON i1.id = c.influencer1_id
LEFT JOIN Influencers i2
    ON c.influencer2_id = i2.id

UNION

SELECT
    i1.name AS influencer_name,
    i2.name AS partner_name,
    c.collab_date
FROM Influencers i1
RIGHT JOIN Collaborations c
    ON i1.id = c.influencer1_id
LEFT JOIN Influencers i2
    ON c.influencer2_id = i2.id;


-- QUESTION 2
-- SELF JOIN: Display each playlist with its parent playlist name.

CREATE TABLE Playlists (
    id INT PRIMARY KEY,
    user_id INT,
    playlist_name VARCHAR(100),
    parent_playlist_id INT
);

INSERT INTO Playlists
(id, user_id, playlist_name, parent_playlist_id)
VALUES
(1, 101, 'My Music', NULL),
(2, 101, 'Workout Songs', 1),
(3, 102, 'Relaxing Music', 1),
(4, 103, 'Favorites', NULL);

SELECT
    child.playlist_name AS playlist_name,
    parent.playlist_name AS parent_playlist_name
FROM Playlists child
LEFT JOIN Playlists parent
    ON child.parent_playlist_id = parent.id;


-- QUESTION 3
-- Multiple JOINs: Show all users, even if they have
-- no orders or payments.

CREATE TABLE Users (
    id INT PRIMARY KEY,
    username VARCHAR(100)
);

CREATE TABLE Orders (
    id INT PRIMARY KEY,
    user_id INT,
    order_date DATE
);

CREATE TABLE Payments (
    id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10,2)
);

INSERT INTO Users (id, username)
VALUES
(1, 'krishna'),
(2, 'rahul'),
(3, 'priya');

INSERT INTO Orders (id, user_id, order_date)
VALUES
(101, 1, '2026-03-01'),
(102, 2, '2026-03-02');

INSERT INTO Payments (id, order_id, amount)
VALUES
(201, 101, 450.00);

SELECT
    Users.username,
    Orders.order_date,
    Payments.amount AS payment_amount
FROM Users
LEFT JOIN Orders
    ON Users.id = Orders.user_id
LEFT JOIN Payments
    ON Orders.id = Payments.order_id;


-- QUESTION 4
-- Remove duplicate restaurant rows from a JOIN query.

-- Example tables: Restaurants and Reviews.
-- DISTINCT removes repeated result rows.

SELECT DISTINCT
    Restaurants.id,
    Restaurants.name,
    Restaurants.city
FROM Restaurants
INNER JOIN Reviews
    ON Restaurants.id = Reviews.restaurant_id;


-- QUESTION 5
-- List all products with their category names
-- using two different JOIN conditions.

CREATE TABLE Categories (
    id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE Products (
    id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT
);

INSERT INTO Categories (id, category_name)
VALUES
(1, 'Mobiles'),
(2, 'Laptops'),
(3, 'Headphones');

INSERT INTO Products (id, product_name, category_id)
VALUES
(101, 'Smartphone', 1),
(102, 'Gaming Laptop', 2),
(103, 'Wireless Headphones', 3);

-- JOIN Query 1: Using category IDs.

SELECT
    Products.product_name,
    Categories.category_name
FROM Products
INNER JOIN Categories
    ON Products.category_id = Categories.id;


-- JOIN Query 2: Using category names.
-- This requires a category_name column in Products.
-- Add it for this demonstration.

ALTER TABLE Products
ADD COLUMN category_name VARCHAR(100);

UPDATE Products
SET category_name = 'Mobiles'
WHERE id = 101;

UPDATE Products
SET category_name = 'Laptops'
WHERE id = 102;

UPDATE Products
SET category_name = 'Headphones'
WHERE id = 103;

SELECT
    Products.product_name,
    Categories.category_name
FROM Products
INNER JOIN Categories
    ON Products.category_name = Categories.category_name;
