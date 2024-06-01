SELECT
    p.first_name,
    p.last_name,
    s.salary,
    pm.HR,
    pm.year
FROM
    players p
    INNER JOIN salaries s ON s.player_id = p.id
    INNER JOIN performances pm ON pm.player_id = p.id
WHERE
    s.year = pm.year
ORDER BY
    p.id ASC, pm.year DESC, pm.HR DESC, s.salary DESC
