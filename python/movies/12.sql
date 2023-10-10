SELECT movies.title FROM movies
JOIN people, stars ON people.id = stars.person_id
WHERE people.id =
(
    SELECT people.id FROM people
    WHERE people.name = 'Bradley Cooper'
)
OR people.id =
(
    SELECT people.id FROM people
    WHERE people.name = 'Jennifer Lawrence'
);