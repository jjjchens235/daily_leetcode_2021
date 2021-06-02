/*
 The contacts count and trust_contacts_count need to be precomputed earlier
 contacts_ct is simply the user_id, count(*) table grouped by user_id
 trust_contacts_count is the same as above but there is a WHERE CLAUSE that checks to see if this email existed
 */
-- Solution 1: Using group by twice
WITH contacts_ct AS (
  SELECT
    user_id,
    count(*) ct
  FROM
    Contacts
  GROUP BY
    1
),
trusted_contacts_ct AS (
  SELECT
    user_id,
    count(*) ct
  FROM
    Contacts
  WHERE
    contact_email IN (
      SELECT
        email
      FROM
        Customers
    )
  GROUP BY
    1
),
Result AS (
  SELECT
    Invoices.invoice_id,
    Customers.customer_name,
    Invoices.price,
    COALESCE(contacts_ct.ct, 0) contacts_cnt,
    COALESCE(trusted_contacts_ct.ct, 0) trusted_contacts_cnt
  FROM
    Invoices
    JOIN Customers ON Invoices.user_id = Customers.customer_id
    LEFT JOIN contacts_ct ON Invoices.user_id = contacts_ct.user_id
    LEFT JOIN trusted_contacts_ct ON Invoices.user_id = trusted_contacts_ct.user_id
  ORDER BY
    1
)
SELECT
  *
FROM
  Result;

-- Solution #2, using groupby only once
SELECT
  Invoices.invoice_id,
  Customers.customer_name,
  Invoices.price,
  COALESCE(contacts_cnt, 0) contacts_cnt,
  COALESCE(trusted_contacts_cnt, 0) trusted_contacts_cnt
FROM
  Invoices
  LEFT JOIN (
    SELECT
      user_id,
      count(Contacts.user_id) contacts_cnt,
      count(Customers.customer_id) trusted_contacts_cnt
    FROM
      Contacts
      LEFT JOIN Customers ON Contacts.contact_email = Customers.email
    GROUP BY
      user_id
  ) gb ON Invoices.user_id = gb.user_id
  JOIN Customers ON Invoices.user_id = Customers.customer_id
ORDER BY
  1;

