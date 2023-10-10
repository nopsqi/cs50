-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema

SELECT
    i.year, i.month, i.day
    -- , c.description
    -- , i.name
    -- , i.transcript
    , atm.account_number
    -- , atm.atm_location
    -- , atm.transaction_type
    -- , atm.amount
    , p.name
    , p.phone_number
    , b.hour
    , b.minute
    , b.activity
    , b.license_plate
    , pc.caller
    , pc.receiver
    , pc.duration
    -- , p1.name
    -- , p1.passport_number
    -- , a.city origin
    -- , a1.city destination
FROM crime_scene_reports c
JOIN interviews i ON i.year >= c.year AND i.month >= c.month
JOIN atm_transactions atm ON atm.year = c.year AND atm.month = c.month AND atm.day = c.day
JOIN bank_accounts ba ON ba.account_number = atm.account_number
JOIN bakery_security_logs b ON b.year = c.year AND b.month = c.month AND b.day = c.day
JOIN people p ON p.id = ba.person_id AND p.license_plate = b.license_plate
JOIN phone_calls pc ON (pc.year = c.year AND pc.month = c.month AND pc.day = c.day) AND (pc.caller = p.phone_number OR pc.receiver = p.phone_number)
-- JOIN people p1 ON p1.phone_number = pc.receiver
-- JOIN passengers pas ON pas.passport_number = p1.passport_number
-- JOIN flights f ON f.id = pas.flight_id
-- JOIN airports a ON a.id = f.origin_airport_id
-- JOIN airports a1 ON a.id = f.destination_airport_id
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.street = 'Humphrey Street'
AND c.description LIKE '%theft%'
AND i.transcript LIKE '%bakery%'
AND atm.transaction_type = 'withdraw'
AND atm.atm_location = 'Leggett Street'
AND b.hour >= 10
AND b.minute >= 15
AND b.activity = 'exit'
AND pc.duration < 60
-- GROUP BY i.transcript
;