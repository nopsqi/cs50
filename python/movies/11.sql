SELECT movies.title, ratings.rating FROM movies
JOIN stars, ratings, people ON movies.id = stars.movie_id AND people.id = stars.person_id
WHERE stars.person_id = (
    SELECT people.id FROM people
    WHERE people.name = 'Chadwick Boseman'
)
ORDER BY ratings.rating DESC
LIMIT 5;