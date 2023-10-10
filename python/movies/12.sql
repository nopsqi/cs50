SELECT *
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
LIMIT 20;