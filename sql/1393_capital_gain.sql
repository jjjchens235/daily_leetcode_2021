/*
 For all buy stocks, make the price negative
 union with
 sell stocks
 
 group by the stock_name, sum(price)
 */
WITH unioned AS (
  SELECT
    stock_name,
    price * -1 price
  FROM
    Stocks
  WHERE
    operation = 'Buy'
  UNION ALL
  SELECT
    stock_name,
    price
  FROM
    Stocks
  WHERE
    operation = 'Sell'
)
SELECT
  stock_name,
  sum(price) capital_gain_loss
FROM
  unioned
GROUP BY
  1
ORDER BY
	2 DESC
