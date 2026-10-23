-- SESSION 16 - SQL Project - Sales Analysis

USE foodie_app;

SELECT * FROM FoodOrders;

-- QUESTION 1
-- Create FoodOrders table to store food delivery orders.
-- CSV data can be imported into this table using MySQL Workbench.

CREATE TABLE IF NOT EXISTS FoodOrders (
    order_id INT PRIMARY KEY,
    restaurant_name VARCHAR(100),
    customer_name VARCHAR(100),
    order_amount DECIMAL(10,2),
    order_date DATE
);
USE FoodOrdersDB;

INSERT INTO FoodOrders
(order_id, restaurant_name, customer_name, order_amount, order_date)
VALUES
(1, 'La Pinoz', 'Krishna', 450, '2026-01-01'),
(2, 'Honest', 'Rahul', 320, '2026-01-02'),
(3, 'Dominos', 'Priya', 550, '2026-01-03'),
(4, 'La Pinoz', 'Rahul', 250, '2026-01-04'),
(5, 'Honest', 'Krishna', 400, '2026-01-05'),
(6, 'Dominos', 'Amit', 600, '2026-01-06'),
(7, 'La Pinoz', 'Priya', 350, '2026-01-07'),
(8, 'Honest', 'Rahul', 500, '2026-01-08'),
(9, 'Dominos', 'Krishna', 300, '2026-01-09'),
(10, 'La Pinoz', 'Amit', 700, '2026-01-10');

SELECT * FROM FoodOrders;

-- QUESTION 2
-- Create TopSongs table and insert 5 sample popular tracks.

CREATE TABLE IF NOT EXISTS TopSongs (
    song_id INT PRIMARY KEY,
    song_title VARCHAR(150),
    artist VARCHAR(100),
    streams BIGINT,
    release_date DATE
);

INSERT INTO TopSongs (song_id, song_title, artist, streams, release_date)
VALUES
(1, 'Blinding Lights', 'The Weeknd', 4000000000, '2019-11-29'),
(2, 'Shape of You', 'Ed Sheeran', 3800000000, '2017-01-06'),
(3, 'Someone You Loved', 'Lewis Capaldi', 3000000000, '2018-11-08'),
(4, 'Starboy', 'The Weeknd', 3000000000, '2016-09-22'),
(5, 'As It Was', 'Harry Styles', 2500000000, '2022-04-01');

-- QUESTION 3
-- Find the top 3 customers based on total order amount.

SELECT
    customer_name,
    SUM(order_amount) AS total_spent
FROM FoodOrders
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 3;

-- QUESTION 4
-- Generate restaurant performance report.

SELECT
    restaurant_name,
    COUNT(order_id) AS number_of_orders,
    SUM(order_amount) AS total_order_amount
FROM FoodOrders
GROUP BY restaurant_name
ORDER BY total_order_amount DESC;

-- QUESTION 5
-- Calculate average order amount and unique customer count
-- in dashboard-friendly KPI format.

SELECT
    'Average Order Amount' AS kpi_name,
    ROUND(AVG(order_amount), 2) AS kpi_value
FROM FoodOrders

UNION ALL

SELECT
    'Unique Customers' AS kpi_name,
    COUNT(DISTINCT customer_name) AS kpi_value
FROM FoodOrders;
