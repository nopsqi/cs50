SELECT title
FROM movies
WHERE movies.id in (
    SELECT movie_id
    FROM stars
    WHERE person_id = (
        SELECT id
        FROM people
        WHERE name = 'Bradley Cooper'
    )
)
AND movies.id in (
    SELECT movie_id
    FROM stars
    WHERE person_id = (
        SELECT id
        FROM people
        WHERE name = 'Jennifer Lawrence'
    )
)
LIMIT 20;