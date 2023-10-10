SELECT people.name FROM people
JOIN movies, stars ON movies.id = stars.movie_id AND people.id = stars.person_id
WHERE movies.year = 2004
GROUP BY people.name
ORDER BY people.birth;