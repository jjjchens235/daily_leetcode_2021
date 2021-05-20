/*
1. union matches first_player with second_player
2. join the union table with Players

3. do a group by group_id/ player_id , sum(score)

4.  do a windows function rank() over (partition by group_id order by score, player_id)
 
5. return only rank 1 
 
 */
WITH unioned AS (
  SELECT
    first_player player_id,
    first_score score
  FROM
    Matches
  UNION ALL
  SELECT
    second_player player_id,
    second_score score
  FROM
    Matches
),
joined AS (
  SELECT
    unioned.*,
    Players.group_id
  FROM
    unioned
    JOIN Players ON unioned.player_id = Players.player_id
),
gb AS (
  SELECT
    group_id,
    player_id,
    sum(score) score
  FROM
    joined
  GROUP BY
    group_id,
    player_id
),
windowed AS (
  SELECT
    *,
    rank() OVER (
      PARTITION BY group_id
      ORDER BY
        score DESC,
        player_id
    ) ranked
  FROM
    gb
)
SELECT
  group_id,
  player_id
FROM
  windowed
WHERE
  ranked = 1

