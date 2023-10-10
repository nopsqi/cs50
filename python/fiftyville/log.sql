-- Keep a log of any SQL queries you execute as you solve the mystery.

.schema


SELECT c.description
FROM crime_scene_reports c
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.description LIKE '%theft%'
;

SELECT i.year || ', ' || i.month || ' ' || i.day as interview_date, i.name, i.transcript
FROM interviews i
WHERE i.year >= 2021
AND i.month >= 7
AND i.day >= 28
AND i.transcript LIKE '%bakery%'
ORDER BY i.name
;

SELECT
    c.year || ', ' ||  c.month || ' ' || c.day AS crime_date
    -- , atm.year
    -- , atm.month
    -- , atm.day
    -- , atm.account_number
    -- , atm.atm_location
    -- , atm.transaction_type
    -- , atm.amount
    , p.name as thief
    , p.phone_number
    -- , p.passport_number
    , pc.caller
    , pc.receiver
    -- , pc.duration
    , p1.name as accomplice
    , p1.passport_number accom_passport
    , f.year || ', ' ||  f.month || ' ' || f.day AS flight_date
    , f.hour || ':' ||  f.minute AS flight_time
    , a1.city origin
    , a.city destination
    -- , b.hour || ':' || b.minute as time
    -- , b.activity
    -- , b.license_plate
    -- , p1.name
FROM crime_scene_reports c
JOIN atm_transactions atm ON atm.year = c.year AND atm.month = c.month AND atm.day = c.day AND atm.atm_location = 'Leggett Street' AND atm.transaction_type = 'withdraw'
JOIN bank_accounts ba ON ba.account_number = atm.account_number
JOIN people p ON p.id = ba.person_id AND p.license_plate = b.license_plate
JOIN phone_calls pc ON pc.year = c.year AND pc.month = c.month AND pc.day = c.day AND pc.duration < 60 AND (pc.caller = p.phone_number OR pc.receiver = p.phone_number)
JOIN people p1 ON (p1.phone_number = pc.receiver OR p1.phone_number = pc.caller) AND p1.name != p.name
JOIN passengers pas ON pas.passport_number = p.passport_number OR pas.passport_number = p1.passport_number
JOIN flights f ON f.id = pas.flight_id AND f.year >= c.year AND f.month >= c.month AND f.day = c.day + 1
JOIN airports a ON a.id = f.destination_airport_id
JOIN airports a1 ON a1.id = f.origin_airport_id
JOIN bakery_security_logs b ON b.year = c.year AND b.month = c.month AND b.day = c.day AND b.hour >= 10 AND b.minute >= 15 AND b.activity = 'exit'
WHERE c.year = 2021
AND c.month = 7
AND c.day = 28
AND c.street = 'Humphrey Street'
AND c.description LIKE '%theft%'
-- GROUP BY i.transcript
;