WITH gb AS (
  SELECT
    CandidateId,
    count(id) ct
  FROM
    Vote
  GROUP BY
    1
),
most_votes AS (
  SELECT
    max(ct) maxed
  FROM
    gb
)
SELECT
  c.Name
FROM
  most_votes
  JOIN gb ON most_votes.maxed = gb.ct
  JOIN Candidate c ON gb.CandidateId = c.id

