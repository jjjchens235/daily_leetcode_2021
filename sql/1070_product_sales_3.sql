/*
 */
SELECT
  product_id,
  YEAR first_year,
  quantity,
  price
FROM
  (
    SELECT
      *,
      rank() OVER (
        PARTITION BY product_id
        ORDER BY
          YEAR
      ) ranked
    FROM
      Sales
  ) base
WHERE
  ranked = 1

