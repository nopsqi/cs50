CREATE VIEW
    frequently_reviewed AS
SELECT
    l.id,
    l.property_type,
    l.host_name,
    COUNT(r.id) AS reviews
FROM
    listings l
    INNER JOIN reviews r ON r.listing_id = l.id
GROUP BY
    l.id
ORDER BY
    COUNT(r.id) DESC,
    property_type ASC,
    host_name ASC
LIMIT
    100;
