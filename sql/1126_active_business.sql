/*
 find all active businesses
 
 An active business has at least two event types that exceed the avg
 */
SELECT
  business_id
FROM
  (
    SELECT
      e.*,
      a.avg_occur
    FROM
      Events e
      JOIN (
        SELECT
          event_type,
          avg(occurences) avg_occur
        FROM
          Events
        GROUP BY
          event_type
      ) a ON e.event_type = a.event_type
  ) base
WHERE
  occurences > avg_occur
GROUP BY
  1
HAVING
  count(*) > 1

