SELECT
  e.name,
  b.bonus
FROM
  Employee e
  LEFT JOIN Bonus b ON e.empID = b.empId
WHERE
  COALESCE(b.bonus, 0) < 1000
ORDER BY
  e.empId

