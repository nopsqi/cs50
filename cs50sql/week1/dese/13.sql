SELECT
    s.name,
    g.excluded
FROM
    schools s
    INNER JOIN graduation_rates g ON g.school_id = s.id
ORDER BY
    g.excluded DESC
