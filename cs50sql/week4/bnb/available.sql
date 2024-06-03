CREATE VIEW
    available AS
SELECT
    l.id,
    l.property_type,
    l.host_name,
    a.date
FROM
    listings l
    INNER JOIN availabilities a ON a.listing_id = l.id
WHERE
    a.available = 'TRUE';
