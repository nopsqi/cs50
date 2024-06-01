SELECT
    s.name
FROM
    districts d
    INNER JOIN schools s ON s.district_id = d.id
WHERE
    d.name = 'Cambridge';
