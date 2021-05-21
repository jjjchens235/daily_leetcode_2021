/*
 union the following
 1. the current credit
 2. with paid by (negative)
 3. paid_to 
 
 Do a group by on the credit
 
 join back with Users to get user_name field
 
 add a case statement for credit limit breached
 */
WITH unioned AS (
  SELECT
    user_id,
    credit
  FROM
    Users
  UNION ALL
  SELECT
    paid_by user_id,
    amount * -1 AS credit
  FROM
    Transaction
  UNION ALL
  SELECT
    paid_to user_id,
    amount AS credit
  FROM
    Transaction
),
gb AS (
  SELECT
    user_id,
    sum(credit) credit
  FROM
    unioned
  GROUP BY
    1
)
SELECT
	gb.user_id,
	Users.user_name,
	gb.credit,
	CASE
		WHEN gb.credit < 0 THEN 'Yes'
		ELSE 'No'
	END credit_limit_breached
FROM
	gb
	JOIN Users ON gb.user_id = Users.user_id

