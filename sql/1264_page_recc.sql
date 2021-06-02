-- working on it, stuck on last part, how do we exclude pages that userid1 already liked?
SELECT
  DISTINCT Likes.page_id
FROM
  (
    SELECT
      user2_id user_id
    FROM
      Friendship
    WHERE
      user1_id = 1
    UNION
    SELECT
      user1_id user_id
    FROM
      Friendship
    WHERE
      user2_id = 1
  ) user1_friends
  JOIN Likes ON user1_friends.user_id = Likes.user_id

