SELECT
  round(
    (
      SELECT
        count(DISTINCT player_id)
      FROM
        (
          SELECT
            *,
            lag(event_date, 1) OVER (
              PARTITION BY player_id
              ORDER BY
                event_date
            ) lagged
          FROM
            Activity
        ) windowed
      WHERE
        datediff(event_date, lagged) = 1
    ) / (
      SELECT
        count(DISTINCT player_id)
      FROM
        Activity
    ),
    2
  ) AS fraction;

-- Kamyu solution, the right join is the trickiest part here, you're actually taking your 3 distinct players from the group by, and checking whcih ones join successfully on the main Activity table, I would not have thought of this tbh
-- The other tricky part is realizing you can join by the date - 1, instead of using lag windows function
SELECT
  round(count(Activity.player_id) / count(*), 2)
FROM
  Activity
  RIGHT JOIN (
    SELECT
      player_id,
      min(event_date) min_event_date
    FROM
      Activity
    GROUP BY
      1
  ) gb ON Activity.player_id = gb.player_id
  AND date_add(Activity.event_date, INTERVAL -1 DAY) = gb.min_event_date;

