/*
 First step is to bring in dept id to salary table.
 Then we bring in average salary per month overall using windows function
 
 Then we do a pivot by pay_month, dept_id, avg(dept), avg(overall)
 */
SELECT
  s.pay_month,
  s.department_id,
  CASE
    WHEN s.amount > avg_salary.avg_amount THEN 'higher'
    WHEN s.amount = avg_salary.avg_amount THEN 'same'
    ELSE 'lower'
  END comparison
FROM
  (
    SELECT
      date_format(pay_date, '%Y-%m') pay_month,
      department_id,
      avg(amount) amount
    FROM
      salary s
      JOIN employee e ON s.employee_id = e.employee_id
    GROUP BY
      1,
      2
  ) s
  JOIN (
    SELECT
      date_format(pay_date, '%Y-%m') pay_month,
      avg(amount) AS avg_amount
    FROM
      salary
    GROUP BY
      1
  ) avg_salary ON s.pay_month = avg_salary.pay_month

