SELECT
  DISTINCT t.id,
  CASE
    WHEN t.p_id IS NULL THEN 'Root'
    WHEN child.id IS NULL THEN 'Leaf'
    WHEN child.id IS NOT NULL THEN 'Inner'
  END TYPE
FROM
  tree t
  LEFT JOIN tree child ON t.id = child.p_id

