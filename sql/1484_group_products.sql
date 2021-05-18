SELECT
  ct.*, p.products
FROM
  (select
    sell_date,
    group_concat(
      DISTINCT product
      ORDER BY product 
				separator ', '
    ) products
    FROM
      Activities
    GROUP BY
      1
  ) p
  JOIN (
    SELECT
      sell_date,
      count(*) num_sold
    FROM
      Activities
    GROUP BY
      1
  ) ct ON p.sell_date = ct.sell_date

