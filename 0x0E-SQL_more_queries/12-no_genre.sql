-- Import the database dump from hbtn_0d_tvshows to your MySQL server.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
RIGHT JOIN tv_show_genre
ON tv_shows.id = tv_show_genre
ORDER BY tv_shows_title ASC, tv_shows_genre.genre_id ASC;
