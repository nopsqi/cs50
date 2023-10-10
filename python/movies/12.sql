SELECT movies.title FROM movies
JOIN stars ON movies.id = stars.movie_id
WHERE stars.person_id =
(
    SELECT people.id FROM people
    WHERE people.name = 'Bradley Cooper'
)
AND stars.person_id =
(
    SELECT people.id FROM people
    WHERE people.name = 'Jennifer Lawrence'
)
GROUP BY movies.title;