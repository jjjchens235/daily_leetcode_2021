/*
 Ask ourselves, what are we trying to look up here, we want to look-up manager name, so we join using e.managerid
 */
SELECT
  m.name
FROM
  Employee e
  JOIN Employee m ON e.managerid = m.id
GROUP BY
  1
HAVING
  count(*) >= 5

