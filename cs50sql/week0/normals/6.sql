SELECT
    "50m",
    latitude,
    longitude
FROM
    normals
WHERE
    latitude BETWEEN 0.1 AND 19.9 AND longitude BETWEEN 55.1 AND 74.9;
