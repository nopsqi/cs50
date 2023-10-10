-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema

SELECT
    i.day, i.month, i.year, b.hour, b.minute
    -- , i.name, c.description, i.transcript
    , b.activity, b.license_plate
FROM crime_scene_reports c
JOIN interviews i, bakery_security_logs b
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.street = 'Humphrey Street'
AND c.description LIKE '%theft%'
AND i.transcript LIKE '%theft%'
AND b.hour = 10;