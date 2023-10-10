-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema

SELECT i.day, i.month, i.year, i.name, i.transcript
FROM crime_scene_reports c
JOIN interviews i
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.street = 'Humphrey Street'
AND c.description LIKE '%theft%'
AND i.transcript LIKE '%theft%';

SELECT *
FROM bakery_security_logs
LIMIT 10;