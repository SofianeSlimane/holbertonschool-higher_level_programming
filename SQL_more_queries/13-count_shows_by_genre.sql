-- The select statement first retrieves one column with genre name
-- , it then computes how many shows are linked to a genre, thanks to COUNT
-- , the GROUP BY clause split every genre rows and applies the count function to
-- to each row, with a condition specified by WHERE
SELECT tv_genres.name AS genre , COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres, tv_show_genres
WHERE tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
