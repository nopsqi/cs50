SELECT
    d.name,
    SUM(e.pupils)
FROM
    districts d
    INNER JOIN expenditures e ON e.district_id = d.id
GROUP BY
    d.name
