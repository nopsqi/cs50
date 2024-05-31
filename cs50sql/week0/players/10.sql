SELECT
    first_name,
    last_name,
    ROUND((weight / height) * (703.0 / height), 2) AS "BMI"
FROM
    players
WHERE
    BMI BETWEEN 18.5 AND 24.9
ORDER BY
    BMI ASC, first_name ASC, last_name ASC
