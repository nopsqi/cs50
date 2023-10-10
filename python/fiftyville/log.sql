-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema

SELECT
    i.year, i.month, i.day, b.hour, b.minute
    , c.description
    , i.transcript
    , b.minute
    , b.activity
    , b.license_plate
    , p.name
    , pc.caller
    , pc.receiver
    , p1.name
    , p1.passport_number
    , a.city origin
    , a1.city destination
FROM crime_scene_reports c
JOIN interviews i, bakery_security_logs b
JOIN people p ON p.license_plate = b.license_plate
JOIN phone_calls pc ON pc.caller = p.phone_number AND pc.day = c.day
JOIN people p1 ON p1.phone_number = pc.receiver
JOIN passengers pas ON pas.passport_number = p1.passport_number
JOIN flights f ON f.id = pas.flight_id
JOIN airports a ON a.id = f.origin_airport_id
JOIN airports a1 ON a1.id = f.destination_airport_id
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.street = 'Humphrey Street'
AND c.description LIKE '%theft%'
AND i.transcript LIKE '%theft%'
AND b.hour = 10
AND b.minute = 25;