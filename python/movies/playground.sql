-- SELECT DISTINCT p.name
SELECT *
FROM stars s1
JOIN stars s2 ON s1.movie_id = s2.movie_id
JOIN people p ON s2.person_id = p.id
-- WHERE s1.person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958)
--   AND p.name != 'Kevin Bacon';
LIMIT 20;