SELECT
  a.student_name,
  b.student_name,
  c.student_name
FROM
  SchoolA a
  JOIN SchoolB b ON a.student_id != b.student_id
  AND a.student_name != b.student_name
  JOIN SchoolC c on c.student_id != b.student_id
  AND c.student_name != b.student_name
  and c.student_id != a.student_id
  AND c.student_name != a.student_name

