
-- SESSION 14 - Window Functions - Part 2


-- QUESTION 1
-- Create Orders table and insert at least 7 sample rows.

USE foodie_app;

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2)
);

INSERT INTO Orders (order_id, user_id, order_date, total_amount)
VALUES
(1, 101, '2026-01-01', 250),
(2, 101, '2026-01-05', 400),
(3, 101, '2026-01-10', 300),
(4, 102, '2026-01-02', 500),
(5, 102, '2026-01-08', 350),
(6, 103, '2026-01-03', 200),
(7, 103, '2026-01-12', 450);


-- QUESTION 2
-- Use LAG() to show the previous order amount
-- for each user.

SELECT
    order_id,
    user_id,
    order_date,
    total_amount,
    LAG(total_amount) OVER (
        PARTITION BY user_id
        ORDER BY order_date
    ) AS previous_amount
FROM Orders
ORDER BY user_id, order_date;


-- QUESTION 3
-- Use LEAD() to show the next order amount
-- for the same user.

SELECT
    order_id,
    user_id,
    order_date,
    total_amount,
    LEAD(total_amount) OVER (
        PARTITION BY user_id
        ORDER BY order_date
    ) AS next_amount
FROM Orders
ORDER BY user_id, order_date;


-- QUESTION 4
-- Calculate the running total for each user.

SELECT
    order_id,
    user_id,
    order_date,
    total_amount,
    SUM(total_amount) OVER (
        PARTITION BY user_id
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM Orders
ORDER BY user_id, order_date;


-- QUESTION 5
-- Calculate a 3-order moving average for each user.
-- Use SUM() OVER() with the previous 2 rows and current row.

SELECT
    order_id,
    user_id,
    order_date,
    total_amount,
    SUM(total_amount) OVER (
        PARTITION BY user_id
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) /
    COUNT(*) OVER (
        PARTITION BY user_id
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg
FROM Orders
ORDER BY user_id, order_date;
