-- Import the database dump of hbtn_0d_tvshows to your MySQL server.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
Join show_genres
LEFT JOIN tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC AND tv_show_genre.genre_id ASC;
