SELECT movies.title FROM movies
JOIN stars, ratings ON movies.id = stars.movie_id AND movies.id = ratings.movie_id
WHERE stars.person_id = (
    SELECT people.id FROM people
    WHERE people.name = 'Chadwick Boseman'
)
ORDER BY ratings.rating DESC
LIMIT 5;