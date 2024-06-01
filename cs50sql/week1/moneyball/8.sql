SELECT
    salary
FROM
    salaries
WHERE
    YEAR = 2001
    AND player_id IN (
        -- find player ids whose HR is the highet in 2001
        SELECT
            player_id
        FROM
            performances
        WHERE
            YEAR = 2001
        GROUP BY
            player_id
        HAVING
            SUM(HR) = (
                -- find the highest HR number by players in 2001
                SELECT
                    MAX(HR)
                FROM
                    (
                        -- calculate total HR for each player IN 2001
                        SELECT
                            SUM(HR) AS HR
                        FROM
                            performances
                        WHERE
                            YEAR = 2001
                        GROUP BY
                            player_id
                    )
            )
    )
