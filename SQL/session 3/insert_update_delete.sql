-- SESSION 3 - INSERT, UPDATE & DELETE

use music_streaming_app;
-- QUESTION 1
-- Create Playlist table and insert one favorite song.

CREATE TABLE Playlist (
    id INT PRIMARY KEY,
    song_name VARCHAR(100),
    artist VARCHAR(100),
    duration INT
);

INSERT INTO Playlist (id, song_name, artist, duration)
VALUES
(1, 'With You', 'AP Dhillon', 180);


-- QUESTION 2
-- Insert 3 more rows into Playlist.

INSERT INTO Playlist (id, song_name, artist, duration)
VALUES
(2, 'Brown Munde', 'AP Dhillon', 189),
(3, 'Heeriye', 'Arjit Singh', 195),
(4, 'Kesariya', 'Arijit Singh', 268);


-- QUESTION 3
-- Fix the artist name typo.

UPDATE Playlist
SET artist = 'Arijit Singh'
WHERE artist = 'Arjit Singh';

SELECT * FROM Playlist;


-- QUESTION 4
-- Delete songs where duration is less than 120 seconds.

DELETE FROM Playlist
WHERE duration < 120;


-- QUESTION 5
-- Add '(Remix)' to AP Dhillon songs
-- having duration greater than 180 seconds.

UPDATE Playlist
SET song_name = CONCAT(song_name, ' (Remix)')
WHERE artist = 'AP Dhillon'
  AND duration > 180;


-- Check final Playlist table.

SELECT * FROM Playlist;