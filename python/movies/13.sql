-- SELECT people.name FROM people
-- JOIN stars ON people.id = stars.person_id
-- WHERE stars.movie_id IN
-- (
--     SELECT stars.movie_id FROM stars
--     WHERE stars.person_id =
--     (
--         SELECT people.id FROM people
--         WHERE people.name = 'Kevin Bacon' AND people.birth = 1958
--     )
-- )
-- AND people.name != 'Kevin Bacon';
SELECT DISTINCT p.name
FROM stars s1
JOIN stars s2 ON s1.movie_id = s2.movie_id
JOIN people p ON s2.person_id = p.id
WHERE s1.person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND birth = 1958)
  AND p.name != 'Kevin Bacon';