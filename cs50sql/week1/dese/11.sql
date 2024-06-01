SELECT
	s.name,
	e.per_pupil_expenditure,
	g.graduated
FROM
	schools s
	INNER JOIN (
		SELECT
			district_id,
			SUM(per_pupil_expenditure) AS per_pupil_expenditure
		FROM
			expenditures
		GROUP BY
			district_id
	) e ON e.district_id = s.district_id
	INNER JOIN graduation_rates g ON g.school_id = s.id
ORDER BY
	e.per_pupil_expenditure DESC,
	s.name ASC
