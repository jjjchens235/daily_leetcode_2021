SELECT
  base2.id,
  Accounts.name
FROM
  (
		-- group by to check if contigious dates 5 or more in a row
    SELECT
      id
    FROM
      (
				-- get contiguious dates, distinct removes same day dups for a user
        SELECT
          DISTINCT id,
          login_date,
          date_add(
            login_date,
            INTERVAL (
              - dense_rank() OVER (
                PARTITION BY id
                ORDER BY
                  login_date
              )
            ) DAY
          ) ranked
        FROM
          Logins
      ) base
    GROUP BY
      id,
      ranked
    HAVING
      count(*) >= 5
  ) base2
  JOIN Accounts ON Accounts.id = base2.id

