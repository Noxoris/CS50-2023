SELECT movies.title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN ratings ON stars.movie_id = ratings.movie_id
JOIN people ON person_id = people.id
WHERE people.name LIKE 'Chadwick Boseman' ORDER BY ratings.rating DESC LIMIT 5;
