SELECT *
FROM people p1
JOIN stars s1 ON s1.person_id = p1.id
JOIN movies m ON m.id = s1.movie_id
LIMIT 20;