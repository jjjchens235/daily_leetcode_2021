DELETE FROM
  Person
WHERE
  id NOT IN (
    SELECT
      min(id) id
    FROM
      Person
    GROUP BY
      email
  )

