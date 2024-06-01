SELECT
    d.name,
    SUM(e.per_pupil_expenditure)
FROM
    districts d
    INNER JOIN expenditures e ON e.district_id = d.id
WHERE
    d.type = 'Public School District'
GROUP BY
    d.id
ORDER BY
    SUM(e.per_pupil_expenditure) DESC
LIMIT
    10
