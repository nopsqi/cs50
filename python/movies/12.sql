SELECT movies.title FROM movies
JOIN stars ON movies.id = stars.movie_id
WHERE stars.person_id =
(
    SELECT people.id FROM people
    WHERE people.name = 'Bradley Cooper'
)
OR stars.person_id =
(
    SELECT people.id FROM people
    WHERE people.name = 'Jennifer Lawrence'
)
GROUP BY movies.title;