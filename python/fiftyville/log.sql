-- Keep a log of any SQL queries you execute as you solve the mystery.

.table

SELECT i
FROM crime_scene_reports c
JOIN interviews i
WHERE c.year = 2021 AND c.month = 7 AND c.day = 28 AND c.street = 'Humphrey Street' AND c.description LIKE '%theft%';

