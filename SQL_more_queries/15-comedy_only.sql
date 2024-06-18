-- Retrieves rows in based on the genre name and ids of genre and show
SELECT title
FROM tv_shows, tv_show_genres, tv_genres
WHERE tv_genres.name = 'Comedy'
AND tv_show_genres.show_id = tv_shows.id
AND tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC;
