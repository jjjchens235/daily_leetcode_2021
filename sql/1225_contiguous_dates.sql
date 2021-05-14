/*
 
 */
SELECT
  *
FROM
  (
    SELECT
      'succeeded' AS period_state,
      min(success_date) start_date,
      max(success_date) end_date
    FROM
      (
        SELECT
          *,
          date_add(
            success_date,
            INTERVAL - row_number() OVER (
              ORDER BY
                success_date
            ) DAY
          ) diff
        FROM
          Succeeded
        WHERE
          success_date >= '2019-01-01'
      ) tmp
    GROUP BY
      diff
    UNION
    SELECT
      'failed' AS period_state,
      min(fail_date) start_date,
      max(fail_date) end_date
    FROM
      (
        SELECT
          *,
          date_add(
            fail_date,
            INTERVAL - row_number() OVER (
              ORDER BY
                fail_date
            ) DAY
          ) diff
        FROM
          Failed
        WHERE
          fail_date >= '2019-01-01'
      ) tmp
    GROUP BY
      diff
  ) combined
ORDER BY
  start_date

