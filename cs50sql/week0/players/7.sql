SELECT
    COUNT(*)
FROM
    players
WHERE
    bats != throws AND bats IN ('R', 'L') AND throws IN ('R', 'L');
