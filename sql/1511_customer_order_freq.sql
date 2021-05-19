SELECT
  customer_id,
  NAME
FROM
  (
    SELECT
      c.customer_id,
      c.name,
      CASE
        WHEN date_format(order_date, '%Y-%m') = '2020-06' THEN price * quantity
        ELSE 0
      END AS june,
      CASE
        WHEN date_format(order_date, '%Y-%m') = '2020-07' THEN price * quantity
        ELSE 0
      END AS july
    FROM
      Customers c
      JOIN Orders o ON o.customer_id = c.customer_id
      JOIN Product p ON o.product_id = p.product_id
  ) base
GROUP BY
  customer_id,
  NAME
HAVING
  sum(june) >= 100
  AND sum(july) >= 100

