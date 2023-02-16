-- list all genres in the database by their rating
-- display: tv_genres.name - rating sum
-- order by rating (descending)
SELECT tv_genres.name, SUM(tv_show_ratings.rate) as rating
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
