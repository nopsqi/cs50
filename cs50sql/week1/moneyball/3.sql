SELECT
    YEAR,
    HR
FROM
    performances
WHERE
    player_id = (
        SELECT
            id
        FROM
            players
        WHERE
            first_name = 'Ken'
            AND last_name = 'Griffey'
    )
ORDER BY
    year DESC
