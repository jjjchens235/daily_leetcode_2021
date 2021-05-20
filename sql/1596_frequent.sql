WITH counted AS (
  SELECT
    customer_id,
    product_id,
    count(*) counted
  FROM
    Orders
  GROUP BY
    1,
    2
),
maxed AS (
  SELECT
    customer_id,
    max(counted) maxed
  FROM
    counted
  GROUP BY
    1
)
SELECT
  counted.customer_id,
  counted.product_id,
  Products.product_name
FROM
  counted
  JOIN maxed ON counted.customer_id = maxed.customer_id
  AND counted.counted = maxed.maxed
  JOIN Products ON counted.product_id = Products.product_id
order by 1, 2
