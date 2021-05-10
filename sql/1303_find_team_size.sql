/* 
 - for each employee, find how big their team is
 - result can be in any order
 
 - Get the count for each team_id, then rejoin with the employee table
 */
SELECT
  e.employee_id, gb.team_size
FROM
  Employee e
  JOIN (
    SELECT
      team_id,
      count(*) team_size
    FROM
      Employee
    GROUP BY
      1
  ) gb ON e.team_id = gb.team_id

