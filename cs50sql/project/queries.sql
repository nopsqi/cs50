-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

-- query notebooks that have CPU manufactured by Intel with frequency > 3.5Ghz and order it by the cheapest
SELECT
	notebook_name,
	notebook_model,
	notebook_manufacturer,
	frequency,
  notebook_price
FROM
	list_all
WHERE
	notebook_id IN (
		SELECT
			notebook_id
		FROM
			list_all
		WHERE
			component_type = 'cpu'
			AND frequency > 3.5
		EXCEPT
		SELECT
			notebook_id
		FROM
			list_all
		WHERE
			component_type = 'cpu'
			AND component_manufacturer != 'Manufacturer A'
	)
	AND frequency IS NOT NULL
GROUP BY
	notebook_id,
	notebook_name,
	notebook_model,
	notebook_manufacturer,
	frequency,
  notebook_price
ORDER BY
  notebook_price ASC

-- query notebooks that have RAM size > 30GB
SELECT
	notebook_name,
	notebook_model,
	notebook_manufacturer,
	SUM(memory_size) AS total_memory_size
FROM
	list_all
GROUP BY
	notebook_name,
	notebook_model,
	notebook_manufacturer
HAVING
	SUM(memory_size) > 30;

-- query notebooks that only have SSD as storage with the total size > 500GB
SELECT
	notebook_name,
	notebook_model,
	notebook_manufacturer,
	SUM(storage_size) AS total_storage_type
FROM
	list_all
WHERE
	notebook_id NOT IN (
		SELECT
			notebook_id
		FROM
			list_all
		WHERE
			component_type = 'storage' AND storage_type != 'ssd'
	)
GROUP BY
	notebook_name,
	notebook_model,
	notebook_manufacturer
HAVING
	SUM(storage_size) > 500;
