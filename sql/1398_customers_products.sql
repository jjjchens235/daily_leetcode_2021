/*
 This question 's solution is not immediately obvious to me
 */
SELECT
  a.customer_name
FROM
  (
    SELECT
      o.*,
      c.customer_name
    FROM
      Orders o
      JOIN Customers c ON o.customer_id = c.customer_id
    WHERE
      product_name = 'A'
  ) a
  JOIN (
    SELECT
      o.*,
      c.customer_name
    FROM
      Orders o
      JOIN Customers c ON o.customer_id = c.customer_id
    WHERE
      product_name = 'B'
  ) b ON a.customer_name = b.customer_name
WHERE
  a.customer_id NOT IN (
    SELECT
      customer_id
    FROM
      Orders
    WHERE
      product_name = 'C'
  )

