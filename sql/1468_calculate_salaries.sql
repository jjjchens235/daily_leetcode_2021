/*
 Find the salary after applying taxes, the taxes are based on how the salary is, ie. over 10k pays 49%
 */
SELECT
  company_id,
  employee_id,
  employee_name,
  round(salary - taxes, 0) salary
FROM
  (
    SELECT
      *,
      CASE
        WHEN salary < 1000 THEN 0 * salary
        WHEN salary <= 10000 THEN 0.24 * salary
        ELSE 0.49 * salary
      END AS taxes
    FROM
      Salaries
  ) tmp

