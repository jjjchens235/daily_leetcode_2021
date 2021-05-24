/*
 let's do a group by  on exam_id, and get the min and max
 
 
 join back on Exam on student_id and score
 */
WITH gb AS (
  SELECT
    exam_id,
    min(score) min_,
    max(score) max_
  FROM
    Exam
  GROUP BY
    1
),
main AS (
  SELECT
    DISTINCT student_id
  FROM
    Exam
    JOIN gb ON Exam.exam_id = gb.exam_id
    AND (
      Exam.score = gb.min_
      OR Exam.score = gb.max_
    )
)
SELECT
  student_name
FROM
  Student
  LEFT JOIN main ON Student.student_id = main.student_id
WHERE
  student_name IS NOT NULL;

/*
 A quiet student is one who took at least one exam but didn't score neither the high or low score for all exams
 
 -- for each exam, get the min and max score via groupby
 
 -- from exam table, join on the groupby table on exam and min and max and get the distinct members that match
 
 - for members not matching from exam table look up to student table
 */
WITH not_quiet AS (
  SELECT
    DISTINCT Exam.student_id
  FROM
    (
      SELECT
        exam_id,
        min(score) min_score,
        max(score) max_score
      FROM
        Exam
      GROUP BY
        1
    ) gb
    JOIN Exam ON gb.exam_id = Exam.exam_id
    AND (
      gb.min_score = Exam.score
      OR gb.max_score = Exam.score
    )
)
SELECT
  Student.student_name
FROM
  Exam
  JOIN Student ON Exam.student_id = Student.student_id
WHERE
  Exam.student_id NOT IN (
    SELECT
      student_id
    FROM
      not_quiet
  );
