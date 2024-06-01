SELECT
    d.name
FROM
    districts d
    INNER JOIN expenditures e ON e.district_id = d.id
GROUP BY
    d.name
HAVING
    SUM(e.pupils) = (
        SELECT
            MIN(pupils_per_district)
        FROM
            (
                SELECT
                    SUM(pupils) AS pupils_per_district
                FROM
                    expenditures
                GROUP BY
                    district_id
            )
    )
