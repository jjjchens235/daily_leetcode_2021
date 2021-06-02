WITH cte AS (
  SELECT
    Boxes.*,
    COALESCE(Chests.apple_count, 0) chest_apple_count,
    COALESCE(Chests.orange_count, 0) chest_orange_count
  FROM
    Boxes
    LEFT JOIN Chests ON Boxes.chest_id = Chests.chest_id
)
select 
	sum(apple_count) apple_count,
	sum(orange_count) orange_count 
	FROM (
SELECT
  apple_count,
  orange_count
FROM
  cte
UNION ALL
SELECT
  chest_apple_count,
  chest_orange_count
FROM
  cte) unioned


