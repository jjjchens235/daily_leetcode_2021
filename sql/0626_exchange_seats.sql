/*
 if last one and odd, don't do anything
 if odd, make id + 1
 if even, make id - 1
 order by id
 */
SELECT
	CASE
		-- last number, and odd
		WHEN id = (
			SELECT
				count(*)
			FROM
				seat
		)
		AND mod(id, 2) != 0 THEN id
		-- even
		WHEN mod(id, 2) = 0 THEN  id - 1
		-- odd
		ELSE id + 1 
	END as id,
	student
FROM
	seat
order by id
