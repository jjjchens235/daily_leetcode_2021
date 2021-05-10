-- return each p name with:
-- total amount due, paid, cancelled, refunded
-- order by product name
SELECT
  p.name,
  sum(rest) rest,
  sum(paid) paid,
  sum(canceled) canceled,
  sum(refunded) refunded
FROM
  Product p
  JOIN Invoice i ON p.product_id = i.product_id
GROUP BY
  p.name
ORDER BY
  p.name

