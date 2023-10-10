SELECT m.title, p2.name
FROM people p1
INNER JOIN stars s1 ON s1.person_id = p1.id
INNER JOIN movies m ON m.id = s1.movie_id
INNER JOIN stars s2 ON s2.movie_id = m.id
INNER JOIN people p2 ON p2.id = s2.person_id
WHERE p2.name == 'Kevin Bacon'
LIMIT 20;