SELECT
    u.username
FROM
    users u
    INNER JOIN messages m ON m.to_user_id = u.id
GROUP BY
    u.id
ORDER BY
    COUNT(m.to_user_id) DESC,
    u.username ASC
LIMIT
    1
