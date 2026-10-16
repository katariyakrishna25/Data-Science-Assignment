
-- SESSION 8 - GROUP BY + HAVING


-- QUESTION 1
-- Create Orders table and insert at least 8 sample records.
USE foodie_app;

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    payment_method VARCHAR(20),
    amount DECIMAL(10,2)
);

INSERT INTO Orders (order_id, user_id, payment_method, amount)
VALUES
(1, 101, 'UPI', 250),
(2, 102, 'Card', 450),
(3, 101, 'Wallet', 180),
(4, 103, 'COD', 350),
(5, 102, 'UPI', 500),
(6, 104, 'Card', 200),
(7, 103, 'UPI', 400),
(8, 101, 'Card', 600);


-- QUESTION 2
-- Count orders placed using each payment method.

SELECT
    payment_method,
    COUNT(*) AS total_orders
FROM Orders
GROUP BY payment_method;


-- QUESTION 3
-- Find total amount spent by each user.

SELECT
    user_id,
    SUM(amount) AS total_spend
FROM Orders
GROUP BY user_id;


-- QUESTION 4
-- Show payment methods where average order amount
-- is greater than 300.

SELECT
    payment_method,
    AVG(amount) AS average_amount
FROM Orders
GROUP BY payment_method
HAVING AVG(amount) > 300;


-- QUESTION 5
-- Difference between WHERE and HAVING.

-- Example of WHERE:
-- Shows only orders where amount is greater than 300.
-- Filters individual rows before grouping.

SELECT *
FROM Orders
WHERE amount > 300;


-- Example of HAVING:
-- Shows users whose total spending is greater than 500.
-- Filters groups after GROUP BY.

SELECT
    user_id,
    SUM(amount) AS total_spend
FROM Orders
GROUP BY user_id
HAVING SUM(amount) > 500;
