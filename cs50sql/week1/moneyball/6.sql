SELECT
    t.name,
    SUM(pm.H) AS "total hits"
FROM
    teams t
    INNER JOIN performances pm ON pm.team_id = t.id
WHERE
    pm.year = 2001
GROUP BY
    t.id
ORDER BY
    SUM(pm.H) DESC
LIMIT
    5
