SELECT
    t.name,
    ROUND(AVG(s.salary), 2) AS "average salary"
FROM
    teams t
    INNER JOIN salaries s ON s.team_id = t.id
WHERE
     s.year = 2001
GROUP BY
    t.id
ORDER BY
    AVG(s.salary) ASC
LIMIT
    5
