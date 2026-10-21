
-- SESSION 13 - Window Functions - Part 1
-- QUESTION 1
-- Create Playlists table and insert at least 8 sample rows.
USE foodie_app;

CREATE TABLE Playlists (
    id INT PRIMARY KEY,
    user_id INT,
    playlist_name VARCHAR(100),
    total_likes INT
);

INSERT INTO Playlists (id, user_id, playlist_name, total_likes)
VALUES
(1, 101, 'Bollywood Hits', 500),
(2, 101, 'Romantic Songs', 700),
(3, 101, 'Workout Music', 300),
(4, 102, 'Party Songs', 900),
(5, 102, 'Chill Vibes', 600),
(6, 103, 'Gujarati Hits', 400),
(7, 103, 'Trending Songs', 800),
(8, 104, 'Old Classics', 500);


-- QUESTION 2
-- Assign a unique row number to each playlist,
-- ordered by total_likes in descending order.

SELECT
    playlist_name,
    user_id,
    total_likes,
    ROW_NUMBER() OVER (
        ORDER BY total_likes DESC, id
    ) AS row_num
FROM Playlists;


-- QUESTION 3
-- Rank all playlists by total_likes.

SELECT
    playlist_name,
    user_id,
    total_likes,
    RANK() OVER (
        ORDER BY total_likes DESC
    ) AS playlist_rank
FROM Playlists;


-- QUESTION 4
-- Rank each user's playlists using DENSE_RANK().


SELECT
    playlist_name,
    user_id,
    total_likes,
    DENSE_RANK() OVER (
        PARTITION BY user_id
        ORDER BY total_likes DESC
    ) AS playlist_rank
FROM Playlists;


-- QUESTION 5
-- Show the top 2 playlists for each user.

WITH RankedPlaylists AS (
    SELECT
        playlist_name,
        user_id,
        total_likes,
        ROW_NUMBER() OVER (
            PARTITION BY user_id
            ORDER BY total_likes DESC, id
        ) AS playlist_position
    FROM Playlists
)
SELECT
    playlist_name,
    user_id,
    total_likes,
    playlist_position
FROM RankedPlaylists
WHERE playlist_position <= 2
ORDER BY user_id, playlist_position;
