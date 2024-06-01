SELECT
    YEAR,
    ROUND(AVG(salary), 2)
FROM
    salaries
GROUP BY
    year
ORDER BY
    year DESC
