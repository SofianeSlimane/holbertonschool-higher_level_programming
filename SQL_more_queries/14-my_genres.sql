-- List genre base on both matching show id and genre id
SELECT name
FROM tv_genres, tv_show_genres
WHERE tv_show_genres.show_id = 8 AND tv_show_genres.genre_id = tv_genres.id
