-- trivial problem
SELECT
  CLASS
FROM
  courses
GROUP BY
  CLASS
HAVING
  count(*) > 5

