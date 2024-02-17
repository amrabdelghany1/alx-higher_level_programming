-- Import the database dump from hbtn_0d_tvshows to your MySQL server.

SELECT tv_shows.title, tv_show_genres
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.title = tv_show_genres.genre_id
ORDER BY tv_show.title AND tv_show_genre.genre_id;