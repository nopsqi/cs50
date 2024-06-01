SELECT
    first_name,
    last_name
FROM
    players
WHERE
    id IN (
        SELECT
            s.player_id
        FROM
            salaries s
            INNER JOIN performances pm ON pm.player_id = s.player_id
        WHERE
            s.year = 2001
            AND pm.year = 2001
            AND pm.RBI > 0
        GROUP BY
            s.player_id
        ORDER BY
            SUM(s.salary) / SUM(pm.RBI) ASC
        LIMIT
            10
    )
INTERSECT
SELECT
    first_name,
    last_name
FROM
    players
WHERE
    id IN (
        SELECT
            s.player_id
        FROM
            salaries s
            INNER JOIN performances pm ON pm.player_id = s.player_id
        WHERE
            s.year = 2001
            AND pm.year = 2001
            AND pm.H > 0
        GROUP BY
            s.player_id
        ORDER BY
            SUM(s.salary) / SUM(pm.H) ASC
        LIMIT
            10
    )
ORDER BY
    last_name
