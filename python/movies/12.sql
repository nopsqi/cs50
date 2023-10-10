SELECT * FROM movies
JOIN stars ON movies.id = stars.movie_id
WHERE stars.movies_id =
(
    SELECT stars.movie_id FROM stars
    WHERE stars.person_id =
);
-- AND stars.person_id =
-- (
--     SELECT people.id FROM people
--     where people.name = 'jennifer lawrence'
-- )