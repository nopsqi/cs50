SELECT
    first_name,
    last_name
FROM
    players
WHERE
    height > (
        SELECT
            AVG(height)
        FROM
            players
    )
ORDER BY
    first_name ASC, last_name ASC;
