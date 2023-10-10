SELECT people.name FROM people
JOIN movies, directors, ratings
ON movies.id = directors.movie_id AND people.id = directors.person_id AND movies.id = ratings.movie_id
WHERE ratings.rating >= 9.0
GROUP BY people.name;
