-- SELECT *
-- FROM people p1
-- INNER JOIN stars s1 ON s1.person_id = p1.id
-- INNER JOIN movies m ON m.id = s1.movie_id
-- INNER JOIN stars s2 ON s2.movie_id = s1.movie_id
-- INNER JOIN people p2 ON p2.id = s2.person_id
-- WHERE p1.name == 'Kevin Bacon'
-- LIMIT 20;
SELECT *
FROM movies m1
INNER JOIN stars s1 ON s1.movie_id = m1.id
INNER JOIN people p1 ON p1.id = s1.person_id
INNER JOIN stars s2 ON s2.movie_id = m1.id
INNER JOIN people p2 ON p2.id = s2.person_id
WHERE p1.name = 'Bradley Cooper' AND p2.name = 'Jennifer Lawrence'
LIMIT 20;