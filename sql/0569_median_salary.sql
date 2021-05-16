/*
 get the row number partitioned by company ordered by salary
 
 get the count of each company

The median for odd numbers is the ranked_row_number that = floor(count / 2) + 1
And for even numbers,it is ranked_row_number IN (count /2 , floor(count /2) + 1)
 */
SELECT
  e.Id,
  e.Company,
  e.Salary
FROM
  (
    SELECT
      *,
      row_number() OVER (
        PARTITION BY Company
        ORDER BY
          Salary
      ) ranked
    FROM
      Employee
  ) e
  JOIN (
    SELECT
      Company,
      count(*) ct
    FROM
      Employee
    GROUP BY
      1
  ) gb ON e.Company = gb.Company
WHERE
  CASE
    WHEN mod(gb.ct, 2) = 0 THEN e.ranked IN (gb.ct div 2, (gb.ct div 2) + 1)
    ELSE e.ranked = (gb.ct div 2) + 1
  END
ORDER BY
  Company,
  Salary

