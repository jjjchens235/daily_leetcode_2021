/*
 https://stackoverflow.com/questions/17046204/how-to-find-the-boundaries-of-groups-of-contiguous-sequential-numbers

The windows function groups all continous numbers in the same group.
From there, you do a groupby on each group, the miniumum of the group is the start, and the max of that group is the end
 */
WITH cte AS (
  SELECT
    log_id,
    row_number() OVER (
      ORDER BY
        log_id
    ) row_ct,
    log_id - row_number() OVER (
      ORDER BY
        log_id
    ) AS grp
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

