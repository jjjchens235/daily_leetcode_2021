/*
 Create 3 new columns, 'America', 'Asia', 'Europe'
 For each column, return the name or null
 */
/*
 This isn't the proper solution because it co
 */
SELECT
  CASE
    WHEN continent = 'America' THEN NAME
  END America,
  CASE
    WHEN continent = 'Asia' THEN NAME
  END Asia,
  CASE
    WHEN continent = 'Europe' THEN NAME
  END Europe
FROM
  student;

/*
 Looking back at my old solution back from Jun 20...
 Not using parameter values
 */
SELECT
  min(am) America,
  min(asia) Asia,
  min(eu) Europe
FROM
  (
    SELECT
      row_number() OVER (PARTITION BY continent) row_num,
      (
        CASE
          WHEN continent = 'America' THEN NAME
        END
      ) am,
      (
        CASE
          WHEN continent = 'Asia' THEN NAME
        END
      ) asia,
      (
        CASE
          WHEN continent = 'Europe' THEN NAME
        END
      ) eu
    FROM
      student
  ) tmp
GROUP BY
  row_num;

