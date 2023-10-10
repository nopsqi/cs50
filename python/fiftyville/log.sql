-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema

SELECT
    i.year, i.month, i.day, b.hour, b.minute
    -- , i.name, c.description, i.transcript
    -- , b.activity, b.license_plate
    -- , p.id, p.name, p.phone_number, p.passport_number
    -- , pc.caller, pc.receiver
    -- , p1.name, p1.phone_number, p1.passport_number
FROM crime_scene_reports c
JOIN interviews i, bakery_security_logs b
JOIN people p ON p.license_plate = b.license_plate
JOIN phone_calls pc ON pc.caller = p.phone_number AND pc.day = c.day
JOIN people p1 ON p1.phone_number = pc.receiver
JOIN passengers pas ON pas.passport_number = p1.passport_number
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.street = 'Humphrey Street'
AND c.description LIKE '%theft%'
AND i.transcript LIKE '%theft%'
AND b.hour = 10
AND b.minute = 25;