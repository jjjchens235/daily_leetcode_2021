/*
https://stackoverflow.com/questions/17046204/how-to-find-the-boundaries-of-groups-of-contiguous-sequential-numbers
*/

WITH cte AS (
  SELECT
    log_id - row_number() OVER (
      ORDER BY
        log_id
    ) AS grp,
    log_id
  FROM
    Logs
)
SELECT
  min(log_id) AS from_,
  max(log_id) AS to_
FROM
  cte
GROUP BY
  grp
ORDER BY
  min(log_id)

