CREATE TABLE
    chipers (
        sentence_id INTEGER,
        START INTEGER NOT NULL,
        length INTEGER NOT NULL,
        FOREIGN KEY (sentence_id) REFERENCES sentences (id)
    );

INSERT INTO
    chipers (sentence_id, START, length)
VALUES
    (14, 98, 4),
    (114, 3, 5),
    (618, 72, 9),
    (630, 7, 3),
    (932, 12, 5),
    (2230, 50, 7),
    (2346, 44, 10),
    (3041, 14, 5);

CREATE VIEW
    message AS
SELECT
    SUBSTR (s.sentence, c.start, c.length) AS phrase
FROM
    chipers c
    INNER JOIN sentences s ON s.id = c.sentence_id;
