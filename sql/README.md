
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
