-- *** The Lost Letter ***
SELECT
    *
FROM
    addresses
WHERE
    id = (
        SELECT
            address_id
        FROM
            scans
        WHERE
            package_id = (
                SELECT
                    id
                FROM
                    packages
                WHERE
                    from_address_id = (
                        SELECT
                            id
                        FROM
                            addresses
                        WHERE
                            address = '900 Somerville Avenue'
                    )
                    AND contents LIKE '%congratulatory%'
            )
            AND action = 'Drop'
    );

-- *** The Devious Delivery ***
SELECT
    *
FROM
    addresses
WHERE
    id = (
        SELECT
            address_id
        FROM
            scans
        WHERE
            package_id = (
                SELECT
                    id
                FROM
                    packages
                WHERE
                    from_address_id IS NULL
            )
            AND action = 'Drop'
    );

SELECT
    *
FROM
    packages
WHERE
    from_address_id IS NULL;

-- *** The Forgotten Gift ***
SELECT
    *
FROM
    packages
WHERE
    from_address_id = (
        SELECT
            id
        FROM
            addresses
        WHERE
            address = '109 Tileston Street'
    );

SELECT
    *
FROM
    drivers
WHERE
    id = (
        SELECT
            driver_id
        FROM
            scans
        WHERE
            package_id = (
                SELECT
                    id
                FROM
                    packages
                WHERE
                    from_address_id = (
                        SELECT
                            id
                        FROM
                            addresses
                        WHERE
                            address = '109 Tileston Street'
                    )
            )
            AND action = 'Pick'
        ORDER BY
            timestamp DESC
        LIMIT
            1
    );
