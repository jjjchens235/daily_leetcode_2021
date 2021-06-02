/*
 get running total using sum windows function
 remove all weights above 1000
 return the person name with the max weight
 */
SELECT
  person_name
FROM
  (
    SELECT
      Queue.*,
      sum(weight) OVER (
        ORDER BY
          turn
      ) running_weight
    FROM
      Queue
  ) windowed
WHERE
  running_weight <= 1000
ORDER BY
  running_weight DESC
LIMIT
  1

