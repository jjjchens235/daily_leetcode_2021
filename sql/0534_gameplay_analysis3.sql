/*
 windows function, partition by player_id, order by event_date
 do a sum total
 */
 SELECT
	 player_id,
	 event_date,
	 sum(games_played) OVER (
		 PARTITION BY player_id
		 ORDER BY
			 event_date
	 ) games_played_so_far
 FROM
	 Activity

