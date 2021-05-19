-- todo this problem isn't fully correct, it is missing this last row: 
-- 2019-07-02 | both     | 0            | 0           |

WITH gb AS (
  SELECT
    user_id,
    spend_date,
    CASE
      WHEN ct = 2 THEN 'both'
      ELSE 'ignore'
    END val
  FROM
    (
      SELECT
        user_id,
        spend_date,
        count(*) ct
      FROM
        Spending
      GROUP BY
        user_id,
        spend_date
    ) gb
),
cte AS (
  SELECT
    s.*,
    CASE
      WHEN gb.val = 'both' THEN 'both'
      ELSE platform
    END final
  FROM
    Spending s
    JOIN gb ON s.user_id = gb.user_id
    AND s.spend_date = gb.spend_date
),
cte2 AS (
  SELECT
    spend_date,
    final,
    user_id,
    sum(amount) total_amount
  FROM
    cte
  GROUP BY
    1,
    2,
    3
)
SELECT
  spend_date,
  final platform,
  sum(total_amount) total_amount,
  count(user_id) total_users
FROM
  cte2
GROUP BY
  1,
  2

