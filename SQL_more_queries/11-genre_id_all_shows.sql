-- Returns all records that exist in two tables
-- that match the ON condition but also the records that
-- don't match the ON condition in the left table
SELECT tv_shows.title ,tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
