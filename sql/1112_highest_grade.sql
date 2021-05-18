SELECT
  student_id,
  course_id,
  grade
FROM
  (
    SELECT
      *,
      rank() OVER (
        PARTITION BY student_id
        ORDER BY
          grade DESC,
          course_id
      ) ranked
    FROM
      Enrollments
  ) base
WHERE
  ranked = 1
