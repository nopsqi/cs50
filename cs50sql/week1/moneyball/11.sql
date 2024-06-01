SELECT
    p.first_name,
    p.last_name,
    s.salary / pm.H AS "dollars per hit"
FROM
    players p
    INNER JOIN (
        SELECT
            player_id,
            SUM(salary) AS salary
        FROM
            salaries
        WHERE
            YEAR = 2001
        GROUP BY
            player_id
    ) s ON s.player_id = p.id
    INNER JOIN (
        SELECT
            player_id,
            SUM(H) AS H
        FROM
            performances
        WHERE
            YEAR = 2001
        GROUP BY
            player_id
    ) pm ON pm.player_id = p.id
WHERE
    pm.H > 0
ORDER BY
    s.salary / Pm.H ASC,
    first_name ASC,
    last_name ASC
LIMIT
    10
