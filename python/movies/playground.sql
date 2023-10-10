SELECT *
FROM people p1
JOIN stars s1 ON s1.movie_id = p1.id
LIMIT 20;