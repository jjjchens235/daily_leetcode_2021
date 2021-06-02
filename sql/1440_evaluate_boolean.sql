SELECT
  CASE
    WHEN OPERATOR = '>' THEN v_left.value > v_right.value
    WHEN OPERATOR = '<' THEN v_left.value < v_right.value
    ELSE v_left.value = v_right.value
  END
FROM
  Expressions
  JOIN Variables v_left ON Expressions.left_operand = v_left.name
  JOIN Variables v_right ON Expressions.right_operand = v_right.name

