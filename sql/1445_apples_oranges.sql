SELECT
  sale_date,
  apples - oranges AS diff
FROM
  (
    SELECT
      sale_date,
      sum(apples) apples,
      sum(oranges) oranges
    FROM
      (
        SELECT
          sale_date,
          CASE
            WHEN fruit = 'apples' THEN sold_num
            ELSE 0
          END apples,
          CASE
            WHEN fruit = 'oranges' THEN sold_num
            ELSE 0
          END oranges
        FROM
          Sales
      ) base
    GROUP BY
      sale_date
  ) gb

