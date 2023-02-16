-- list all shows without the genre Comedy
-- display tv_shows.title
-- order by tv_shows.title (ascending)
SELECT title
FROM tv_shows
WHERE title NOT IN
	(SELECT tv_shows.title
	 FROM tv_shows
	 INNER JOIN tv_show_genres
	 ON tv_shows.id = tv_show_genres.show_id
	 INNER JOIN tv_genres
	 ON tv_genres.id = tv_show_genres.genre_id
	 WHERE tv_genres.name = 'Comedy')
ORDER BY title ASC;
