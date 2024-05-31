SELECT
    english_title,
    artist,
    entropy
FROM
    views
WHERE
    english_title LIKE '%Sagami%'
ORDER BY
    entropy DESC;
