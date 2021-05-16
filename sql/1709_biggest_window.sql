SELECT
  user_id,
  max(datediff(next_visit_date, visit_date)) biggest_window
FROM
  (
    SELECT
      *,
      ifnull(
        lead(visit_date, 1) OVER (
          PARTITION BY user_id
          ORDER BY
            visit_date
        ),
        date('2021-01-01')
      ) next_visit_date
    FROM
      UserVisits
  ) base
GROUP BY
  1
ORDER BY
  1

