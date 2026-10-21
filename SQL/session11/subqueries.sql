
-- SESSION 11 - SUBQUERIES


-- QUESTION 1
-- Find restaurants whose average rating is higher
-- than the average rating of all restaurants in the same city.
USE foodie_app;

CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    average_rating DECIMAL(3,2)
);

INSERT INTO Restaurants (id, name, city, average_rating)
VALUES
(1, 'Spice Garden', 'Surat', 4.50),
(2, 'Food Corner', 'Surat', 3.80),
(3, 'Pizza House', 'Mumbai', 4.60),
(4, 'Tasty Bites', 'Mumbai', 4.10),
(5, 'Royal Meals', 'Surat', 4.20);

SELECT *
FROM Restaurants r
WHERE r.average_rating > (
    SELECT AVG(r2.average_rating)
    FROM Restaurants r2
    WHERE r2.city = r.city
);


-- QUESTION 2
-- Display each user's name and total number of orders
-- using a subquery in the SELECT statement.

CREATE TABLE Users (
    id INT PRIMARY KEY,
    username VARCHAR(100)
);

CREATE TABLE Orders (
    id INT PRIMARY KEY,
    user_id INT,
    order_date DATE
);

INSERT INTO Users (id, username)
VALUES
(1, 'Krishna'),
(2, 'Rahul'),
(3, 'Priya');

INSERT INTO Orders (id, user_id, order_date)
VALUES
(101, 1, '2026-01-10'),
(102, 1, '2026-01-15'),
(103, 2, '2026-02-05'),
(104, 1, '2026-02-20');

SELECT
    u.username,
    (
        SELECT COUNT(*)
        FROM Orders o
        WHERE o.user_id = u.id
    ) AS total_orders
FROM Users u;


-- QUESTION 3
-- Use IN with a subquery to find movies
-- that have at least one 5-star review.

CREATE TABLE Movies (
    id INT PRIMARY KEY,
    movie_name VARCHAR(100)
);

CREATE TABLE Reviews (
    id INT PRIMARY KEY,
    movie_id INT,
    rating INT
);

INSERT INTO Movies (id, movie_name)
VALUES
(1, 'Movie A'),
(2, 'Movie B'),
(3, 'Movie C'),
(4, 'Movie D');

INSERT INTO Reviews (id, movie_id, rating)
VALUES
(1, 1, 5),
(2, 1, 4),
(3, 2, 3),
(4, 3, 5),
(5, 4, 4);

SELECT *
FROM Movies
WHERE id IN (
    SELECT movie_id
    FROM Reviews
    WHERE rating = 5
);


-- QUESTION 4
-- Find sellers who have sold products in every category.
-- Nested subqueries compare each seller with all categories.

CREATE TABLE Categories (
    id INT PRIMARY KEY,
    category_name VARCHAR(100)
);

CREATE TABLE Sellers (
    id INT PRIMARY KEY,
    seller_name VARCHAR(100)
);

CREATE TABLE Products (
    id INT PRIMARY KEY,
    seller_id INT,
    category_id INT,
    product_name VARCHAR(100)
);

INSERT INTO Categories (id, category_name)
VALUES
(1, 'Mobiles'),
(2, 'Laptops'),
(3, 'Headphones');

INSERT INTO Sellers (id, seller_name)
VALUES
(1, 'Seller A'),
(2, 'Seller B'),
(3, 'Seller C');

INSERT INTO Products (id, seller_id, category_id, product_name)
VALUES
(1, 1, 1, 'Smartphone'),
(2, 1, 2, 'Laptop'),
(3, 1, 3, 'Headphones'),
(4, 2, 1, 'Mobile Phone'),
(5, 2, 2, 'Office Laptop'),
(6, 3, 1, 'Budget Phone');

SELECT s.seller_name
FROM Sellers s
WHERE NOT EXISTS (
    SELECT *
    FROM Categories c
    WHERE NOT EXISTS (
        SELECT *
        FROM Products p
        WHERE p.seller_id = s.id
          AND p.category_id = c.id
    )
);
