
### Template
For each challenging question, I will provide the following:

1. Logic
	- df
2. Experience
	- df
3. Takeaways
	- df

### Challenging problems
1. 1285: Find the Start and End Number of Continuous Ranges
	- Logic: There are 2 parts to this problem:
		1. Group all continious ranges together
		2. Get the min and max of each continious range
	- Step 1 is definitely the harder one, one method of doing this is to realize that log_id - row_number() will always have the same difference for numbers in the same continuous range 
	- Experience: I ended up stackoverflowing this problem and found a pretty nice row_number() windows function that I adopted

2. 615: average salary
	- Logic- there's a lot of moving parts here. The key is figuring out the order in which to join things.
		1. you want to join salary with employees. Then do a group by on this combined table. This is your avg amount by month/dept
		2. Create another table that is the avg amount by just dept. Join this table with the table from step 1
		3. Thirdly, you compare the avg amount by month/dept vs by month company-wide
	- Experience: I was able to do this, but it took me a little bit of time to get it right

3. 618: Geography pivot
	1. Logic
		- Create 3 new columns for each continent (Asia, America, Europe) using case statement, where it should return the student name or NULL
		- The issue with just adding 3 case statements is that you have a bunch of null values, so next, you have an inner query that shows the row number partitioned by the continent, then you group by by the row number, this removes null values
	2. Experience
		- df
	3. Takeaways
		- What you group by does not need to be in the select clause
		- If you have to do a transpose/pivot, you most likely need some sort of case when clause 

4. 1142 Average Sessions Per User
	1. Logic: A user can have multiple sessions, and each session can have multiple activities. Notice the grain is activities, but we care only about average sessions per user, so we need to find the number of distinct sessions and the number of distinct users, that's the average
	2. Takeaways: 
		- I made this problem harder than it needs to be, all we need is distinct command for sessions and users
		- I used dateadd() function, which ends up needing an extra condition, better is to use datediff()

5. 1225: Contiguous Date Ranges
	1. Logic: This question is very similar to 1285 above- the two main differences are
		- In 1285, they want you to find contigious log id's (integer), here we need to find contigious dates. For both, the logic is to be able to group the log_id/ date together, by subtracting by row number 
		- In this question, you have to do an additional union between the fail and success tables, not a big deal 
	2. Takeaways
		- For contigious problems, use row_number() windows function to be able to group contiguous ranges together, in this case you would do something like diff = date_add(success_date, - row_number())

6. 
