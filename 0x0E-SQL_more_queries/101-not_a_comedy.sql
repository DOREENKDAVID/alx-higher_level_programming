-- This script lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

-- Use of inner join, to join more than 2 tables

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
    SELECT tv_shows.title
    FROM tv_shows
    JOIN tv_show_genres
