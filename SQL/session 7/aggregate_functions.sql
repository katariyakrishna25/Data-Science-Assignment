-- SESSION 7 - Aggregate Functions
use music_streaming_app;

-- QUESTION 1
-- Create Orders table and insert 5 sample records.
-- One order has NULL total_amount.

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    total_amount DECIMAL(10,2),
    order_date DATE
);

INSERT INTO Orders (order_id, user_name, total_amount, order_date)
VALUES
(1, 'Amit', 500.00, '2026-08-01'),
(2, 'Riya', 750.00, '2026-08-02'),
(3, 'Amit', NULL, '2026-08-03'),
(4, 'Rahul', 1200.00, '2026-08-04'),
(5, 'Riya', 450.00, '2026-08-05');


-- QUESTION 2
-- Count how many orders were placed by each user.

SELECT user_name,
       COUNT(*) AS order_count
FROM Orders
GROUP BY user_name;


-- QUESTION 3
-- Calculate the average order amount.
-- AVG() automatically ignores NULL values.

SELECT AVG(total_amount) AS average_order_amount
FROM Orders;


-- QUESTION 4
-- Find the highest and lowest order amounts
-- in a single result row.

SELECT MAX(total_amount) AS highest_order_amount,
       MIN(total_amount) AS lowest_order_amount
FROM Orders;


-- QUESTION 5
-- Calculate total sales.
-- Only orders having a non-NULL amount are included.

SELECT SUM(total_amount) AS total_sales
FROM Orders
WHERE total_amount IS NOT NULL;