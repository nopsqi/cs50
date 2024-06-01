SELECT
    s.name
FROM
    schools s
    INNER JOIN graduation_rates g ON g.school_id = s.id
WHERE
    g.graduated = 100;
