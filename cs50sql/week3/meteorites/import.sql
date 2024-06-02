.import --csv meteorites.csv temp
CREATE TABLE
    meteorites (
        id INTEGER PRIMARY KEY,
        name TEXT,
        class TEXT,
        mass NUMERIC,
        discovery TEXT,
        year NUMERIC,
        lat NUMERIC,
        long NUMERIC
    );

UPDATE temp
SET
    mass = NULL
WHERE
    mass = '';

UPDATE temp
SET
    year = NULL
WHERE
    year = '';

UPDATE temp
SET
    lat = NULL
WHERE
    lat = '';

UPDATE temp
SET
    long = NULL
WHERE
    long = '';

INSERT INTO
    meteorites (
        name,
        class,
        mass,
        discovery,
        year,
        lat,
        long
    )
SELECT
    name,
    class,
    ROUND(mass, 2),
    discovery,
    year,
    ROUND(lat, 2),
    ROUND(long, 2)
FROM
    temp
WHERE
    nametype != 'Relict'
ORDER BY
    year ASC,
    name ASC;

DROP TABLE temp;
