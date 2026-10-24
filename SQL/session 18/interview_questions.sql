-- SESSION 18 - Interview Questions + Final Revision

-- QUESTION 1
-- Count songs uploaded by each artist.
-- Show only artists who have uploaded more than 3 songs.
use foodie_app ;

SELECT
    artist_name,
    COUNT(song_id) AS total_songs
FROM songs
GROUP BY artist_name
HAVING COUNT(song_id) > 3;


-- QUESTION 2
-- Display each username with their total order amount.

SELECT
    u.username,
    SUM(o.amount) AS total_order_amount
FROM users u
JOIN orders o
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.username;


-- QUESTION 3
-- Find restaurants with ratings higher than the average rating.

SELECT
    name,
    rating
FROM restaurants
WHERE rating > (
    SELECT AVG(rating)
    FROM restaurants
);


-- QUESTION 4
-- Display each user's transaction amount and running total.

SELECT
    id,
    user_id,
    amount,
    transaction_date,
    SUM(amount) OVER (
        PARTITION BY user_id
        ORDER BY transaction_date, id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM transactions
ORDER BY user_id, transaction_date, id;


-- QUESTION 5
-- Two optimizations for filtering Flipkart products by category and price.

-- Optimization 1: Create a composite index.
CREATE INDEX idx_category_price
ON FlipkartProducts (category, price);

-- Optimization 2: Select only the required columns and filter
-- directly using WHERE conditions instead of SELECT *.

SELECT product_name, category, price
FROM FlipkartProducts
WHERE category = 'Electronics'
  AND price BETWEEN 1000 AND 50000;
