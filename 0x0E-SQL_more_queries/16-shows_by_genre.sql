-- list all shows and all genres linked to that show
-- display tv_shows.title - tv_genres.name
-- order by tv_shows.tile and tv_show_genres.name (ascending)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;
