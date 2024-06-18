-- List genre base on both matching show id and genre id
SELECT name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_show_genres.show_id = tv_shows.id AND tv_show_genres.genre_id = tv_genres.id AND tv_shows.title = 'Dexter'
ORDER BY name ASC;
