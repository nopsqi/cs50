-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema


SELECT c.description
FROM crime_scene_reports c
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.description LIKE '%theft%'
;

SELECT i.name, i.transcript
FROM interviews i
WHERE i.year = 2021
AND i.month = 7
AND i.day = 28
AND i.transcript LIKE '%bakery%'
ORDER BY i.name
;

SELECT
    c.year, c.month, c.day
    , atm.account_number
    -- , atm.atm_location
    -- , atm.transaction_type
    -- , atm.amount
    , p.name
    , p.phone_number
    , p.passport_number
    , b.hour
    , b.minute
    , b.activity
    , b.license_plate
    , pc.caller
    , pc.receiver
    , pc.duration
    , a.city destination
    , p1.name
FROM crime_scene_reports c
JOIN atm_transactions atm ON atm.year = c.year AND atm.month = c.month AND atm.day = c.day AND atm.atm_location = 'Leggett Street' AND atm.transaction_type = 'withdraw'
JOIN bank_accounts ba ON ba.account_number = atm.account_number
JOIN bakery_security_logs b ON b.year = c.year AND b.month = c.month AND b.day = c.day AND b.hour >= 10 AND b.minute >= 15 AND b.activity = 'exit'
JOIN people p ON p.id = ba.person_id AND p.license_plate = b.license_plate
JOIN phone_calls pc ON (pc.year = c.year AND pc.month = c.month AND pc.day = c.day) AND (pc.caller = p.phone_number OR pc.receiver = p.phone_number) AND pc.duration < 60
JOIN passengers pas ON pas.passport_number = p.passport_number
JOIN flights f ON f.id = pas.flight_id AND f.year >= c.year AND f.month >= c.month AND f.day >= c.day AND f.hour >= b.hour AND f.minute >= b.minute
JOIN airports a ON a.id = f.destination_airport_id and a.city = 'Fiftyville'
JOIN people p1 ON p1.phone_number = pc.receiver
-- JOIN people p1 ON p1.phone_number = pc.receiver
-- JOIN airports a ON a.id = f.origin_airport_id
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.street = 'Humphrey Street'
AND c.description LIKE '%theft%'
-- GROUP BY i.transcript
;