-- ZOMATO BANGALORE RESTAURANT CASE STUDY
-- MySQL 8+

-- QUESTION 1
-- Find top 5 highest-rated North Indian restaurants in Koramangala.

SELECT
    name,
    location,
    cuisines,
    rate AS rating,
    votes
FROM zomato
WHERE location = 'Koramangala'
  AND cuisines LIKE '%North Indian%'
  AND rate IS NOT NULL
ORDER BY rate DESC, votes DESC
LIMIT 5;


-- QUESTION 2 
-- Find the 3 most expensive cuisines based on average cost for two.
-- Assumes cost_for_two is numeric.

SELECT
    cuisines,
    ROUND(AVG(cost_for_two), 2) AS average_cost_for_two
FROM zomato
WHERE cost_for_two IS NOT NULL
GROUP BY cuisines
ORDER BY average_cost_for_two DESC
LIMIT 3;


-- QUESTION 3
-- Find online-delivery restaurants with rating below 3.0.

SELECT
    name,
    location,
    cuisines,
    rate AS rating,
    cost_for_two,
    votes
FROM zomato
WHERE online_order = 'Yes'
  AND rate < 3.0
ORDER BY rate ASC, votes DESC;

-- Marketing recommendation:
-- 1. Investigate low-rated restaurants by location and cuisine.
-- 2. Check review volume and recurring customer complaints.
-- 3. Help restaurants improve food quality, packaging and delivery time.
-- 4. Offer targeted promotions only after service quality improves.


-- QUESTION 4
-- Segment restaurants by average cost for two.

SELECT
    CASE
        WHEN cost_for_two < 400 THEN 'Budget'
        WHEN cost_for_two <= 800 THEN 'Mid-range'
        ELSE 'Premium'
    END AS market_segment,
    COUNT(*) AS total_restaurants
FROM zomato
WHERE cost_for_two IS NOT NULL
GROUP BY
    CASE
        WHEN cost_for_two < 400 THEN 'Budget'
        WHEN cost_for_two <= 800 THEN 'Mid-range'
        ELSE 'Premium'
    END
ORDER BY total_restaurants DESC;


-- QUESTION 5
-- Find the top 10 restaurant chains by number of outlets.
-- Group identical restaurant names together.

SELECT
    name AS restaurant_chain,
    COUNT(*) AS total_outlets
FROM zomato
WHERE name IS NOT NULL
GROUP BY name
ORDER BY total_outlets DESC, name ASC
LIMIT 10;
