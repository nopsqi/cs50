SELECT movies.title FROM movies
JOIN stars, ratings, people ON movies.id = stars.movie_id AND people.id = stars.person_id
WHERE stars.person_id = (
    SELECT people.id FROM people
    WHERE people.name = 'Chadwick Boseman'
)
GROUP BY movies.title
ORDER BY ratings.rating DESC
LIMIT 5;