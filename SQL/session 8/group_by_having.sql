-- SESSION 8 - GROUP BY + HAVING


-- QUESTION 1
-- Create Orders table and insert 8 sample records.

CREATE TABLE Orders1 (
    order_id INT PRIMARY KEY,
    user_id INT,
    payment_method VARCHAR(20),
    amount DECIMAL(10,2)
);

INSERT INTO Orders1 (order_id, user_id, payment_method, amount)
VALUES
(1, 101, 'UPI', 250.00),
(2, 102, 'Card', 500.00),
(3, 101, 'Wallet', 350.00),
(4, 103, 'UPI', 450.00),
(5, 104, 'COD', 200.00),
(6, 102, 'Card', 700.00),
(7, 105, 'UPI', 600.00),
(8, 103, 'Wallet', 300.00);


-- QUESTION 2
-- Count how many orders were placed
-- using each payment method.

SELECT payment_method,
       COUNT(*) AS order_count
FROM Orders1
GROUP BY payment_method;


-- QUESTION 3
-- Find the total amount spent by each user.

SELECT user_id,
       SUM(amount) AS total_spend
FROM Orders1
GROUP BY user_id;


-- QUESTION 4
-- Show only payment methods where
-- average order amount is greater than 300.

SELECT payment_method,
       AVG(amount) AS average_order_amount
FROM Orders1
GROUP BY payment_method
HAVING AVG(amount) > 300;


-- QUESTION 5
-- Difference between WHERE and HAVING.
--
-- WHERE filters individual rows before GROUP BY.
-- HAVING filters groups after GROUP BY.


-- WHERE example:
-- Show orders where amount is greater than 300.

SELECT *
FROM Orders1
WHERE amount > 300;


-- HAVING example:
-- Show users whose total spending is greater than 500.

SELECT user_id,
       SUM(amount) AS total_spend
FROM Orders1
GROUP BY user_id
HAVING SUM(amount) > 500;