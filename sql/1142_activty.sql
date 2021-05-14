SELECT
  avg(ct)
FROM
  (
    SELECT
      user_id,
      count(user_id) ct
    FROM
      (
        SELECT
          user_id,
          session_id session_count
        FROM
          Activity
        WHERE
          activity_date > date_add('2019-07-27', INTERVAL -30 DAY)
          AND activity_date <= '2019-07-27'
        GROUP BY
          1,
          2
      ) tmp
    GROUP BY
      1
  ) tmp2;

/*
 Alternatively, we can just count the distinct number of sessions and divide it by the number of distinct users
 */
SELECT
  round(
    count(DISTINCT(session_id)) / count(DISTINCT(user_id)),
    2
  ) average_sessions_per_user
FROM
  Activity
WHERE
  datediff('2019-07-27', activity_date) < 30

