SELECT
  contest_id,
  contest_count / total_count percentage
FROM
  (
    SELECT
      contest_id,
      count(contest_id) contest_count,
      (
        SELECT
          count(*)
        FROM
          Users
      ) AS total_count
    FROM
      Register
    GROUP BY
      contest_id
  ) base
ORDER BY
  percentage DESC,
  contest_id

