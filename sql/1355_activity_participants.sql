WITH gb AS (
  SELECT
    activity,
    count(*) participants
  FROM
    Friends
  GROUP BY
    activity
),
min_max AS (
  SELECT
    min(participants) min_,
    max(participants) max_
  FROM
    gb
)
SELECT
  activity
FROM
  gb
  JOIN min_max ON gb.participants != min_max.min_
  AND gb.participants != min_max.max_

