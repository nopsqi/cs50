SELECT
    title
FROM
    episodes
WHERE
    STRFTIME('%m', air_date) = '12' AND STRFTIME('%d', air_date) = '31';
