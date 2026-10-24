-- SESSION 17 - SQL Project - HR Analysis

USE foodie_app;

-- QUESTION 1
-- Create Restaurant table and insert 5 sample restaurants.

CREATE TABLE IF NOT EXISTS Restaurant (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine VARCHAR(50),
    location VARCHAR(100),
    average_rating DECIMAL(2,1)
);

INSERT INTO Restaurant (id, name, cuisine, location, average_rating)
VALUES
(1, 'La Pinoz Pizza', 'Italian', 'Ahmedabad', 4.3),
(2, 'Dominos', 'Italian', 'Surat', 4.1),
(3, 'Honest', 'Indian', 'Ahmedabad', 4.2),
(4, 'Punjabi Tadka', 'North Indian', 'Surat', 4.0),
(5, 'TGB - The Grand Bhagwati', 'Multi Cuisine', 'Ahmedabad', 4.5);

-- QUESTION 2
-- Count restaurants for each cuisine type.
 
SELECT 
    cuisine,
    COUNT(*) AS total_restaurants
FROM Restaurant
GROUP BY cuisine
ORDER BY total_restaurants DESC;

-- QUESTION 3
-- Create Review table and insert 10 sample reviews.

CREATE TABLE IF NOT EXISTS Review (
    id INT PRIMARY KEY,
    restaurant_id INT,
    user_name VARCHAR(100),
    rating DECIMAL(2,1),
    review_date DATE,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id)
);

INSERT INTO Review (id, restaurant_id, user_name, rating, review_date)
VALUES
(1, 1, 'Krishna', 4.5, '2026-01-01'),
(2, 1, 'Rahul', 4.0, '2026-01-02'),
(3, 2, 'Priya', 4.2, '2026-01-03'),
(4, 2, 'Amit', 3.8, '2026-01-04'),
(5, 3, 'Neha', 4.5, '2026-01-05'),
(6, 3, 'Rohan', 4.0, '2026-01-06'),
(7, 4, 'Kiran', 3.5, '2026-01-07'),
(8, 4, 'Meera', 4.0, '2026-01-08'),
(9, 5, 'Arjun', 4.8, '2026-01-09'),
(10, 5, 'Pooja', 4.6, '2026-01-10');

-- QUESTION 4
-- Show each restaurant's name, cuisine, and average review rating.

SELECT
    r.name AS restaurant_name,
    r.cuisine,
    ROUND(AVG(rv.rating), 2) AS avg_review_rating
FROM Restaurant r
JOIN Review rv
    ON r.id = rv.restaurant_id
GROUP BY r.id, r.name, r.cuisine
ORDER BY avg_review_rating DESC;

-- QUESTION 5
-- Rank restaurants by average review rating within each cuisine.

SELECT
    restaurant_name,
    cuisine,
    avg_review_rating,
    RANK() OVER (
        PARTITION BY cuisine
        ORDER BY avg_review_rating DESC
    ) AS restaurant_rank
FROM (
    SELECT
        r.id,
        r.name AS restaurant_name,
        r.cuisine,
        AVG(rv.rating) AS avg_review_rating
    FROM Restaurant r
    JOIN Review rv
        ON r.id = rv.restaurant_id
    GROUP BY r.id, r.name, r.cuisine
) AS restaurant_ratings
ORDER BY cuisine, restaurant_rank;
