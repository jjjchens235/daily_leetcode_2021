
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

6. 1709 - biggest window
	1. Logic: Immediately knew this was a lag/lead question, with a group by and max() logic, but the hard part was including the 2021-01-01 logic
	2. Takeaways:
		- I could not for the life of me figure out how to add the 2021-01-01 while using lag, the trick is to use lead() combined with coalesce()

7. 1633 - percentage of users attended a contest
	1. Takeaway: You can create a derived column using a subquery, i.e 
``` sql
select main.\*, (select new_field from tmp) derived_field
```

8. 596: Median Salary
	1. Logic:
		-  You need to rank the rows on salary partitioned by company
		- You also need the count partitioned by company. The trick here is to divide the count by 2, if odd, you will get a number like 4.5, if even you will get a round number like 5.
		- So lets say count_div = count / 2. The median is always equal to all numbers between (count_div , count_div + 1)
		- [circle coder source](https://circlecoder.com/median-employee-salary/)
	2. Experience: I had most of the intuition right and after playing around with this in sql fiddle I was able to solve it without help, however, not in the first straight shot. The above logic uses a `where between clause`, whereas I used a `where case when clause`, which was definitely not as clean
	3.  Takeaways:
		- Need to better think out the whole problem before coding it, i.e I wasn't fully sure how I was going to get the median once I had salaries ranked and had the count. My intution told me that's all that was needed but I wasn't fully sure and I didn't flesh it out.
		- Median properties:
			- If odd, the median is always count / 2 , rounded up, i.e if there are 9 numbers, then it's 4.5 rounded  up, i.e the 5th number
			- If even, the median is always count / 2 AND count /2 + 1
		- Between clause, I have never used this before - it's quite nice
9. 1454: active users
	1. Logic
		- This problem is tough! I feel like it should be classified as hard. I ended up using logic similiar to 'contiguious dates' problem
		- First, using dense_rank() group contigious dates by users together, make sure to use distinct to remove duplicate same day logins 
		- Group by user/ contigious dates, check if any are above a count of 4
		- Join with employee table to get the name
	2. Experience: was stuck for a pretty long time on this, wasn't sure if I wanted to commit time to solving it contiguous style, ended up committing to it.
10. 534: Game Play Analysis #3
	1. Takeaways: For running totals, use sum() windows function, don't forget to add an argument to sum(), like sum(games_played)

11. 1484: Group products
	1. Takeaways: This problem is very easy if you know about the sql built in method group_concat() . This is the name of the function in mysql, in postgres it's called something else.

12. 570: Managers with more than 5 employees
	1. Takeaways: Still not the strongest with self joins. One question to ask ourselves is what do we want to lookup? In this case, we want to know who the manager is, so use e.managerid to lookup the manager

13. 1795: Rearrange Products table
	1. Experience: I was not able to devise a solution for this problem, didn't occur to me to use union, I was really stuck on the idea of 'unpivoting' which I think would work as well, but I sensed that there had to be an easier way especially given the fact that there were only 3 stores

14. 1511: Customer Order frequency
	1. Experience: Despite this being an easy problem, I wasn't originally sure how to proceed with separating June and July
	2. Takeaways: Need to separate the two months  into separate fields using case statement, afterwards, can do a group by, and having(sum > 100)

15. 1127: User Purchase
	1. Experience: This problem is pretty rough, wasn't able to solve it fully in the end and I don't think it's worth more time to invest in it. I'm basically missing a final row where no one bought from that category (the 'both' category)

16. 1355: activity participants
	1. Experience: I was stumped for a little trying to figure out how to tie everything together, eventually I went with a chain CTE solution that I thought was pretty clean.
	2. Logic: The github solution does things slightly differently using a `having not in ( select max union select min )`

17. 1194 Tournament
	1. Experience: I implemented a clean CTE solution, but this problem is a good one, worth doing again

18. 1596: The Most Frequently Ordered Products for Each Customer
	1. Experience: This one took me a little longer than I would like, I didn't recognize the pattern immediately, which is you need to group by customer/product/ count as product_count, then a second group by like customer, max(product_count) all chained together as CTE

19. 574: Winning Canididate
	1. Easier than 1194, but simpler.

20. 1555: Bank Balance
	1. Experience: Not bad, but good practice
	2. Logic: Located inside the sql problem 1555_

21. 1393: Capital Gain /Loss
	1. Experience: Very similar to 1555
	2. Logic: Located inside the sql problem 1555_
22. 1412: queit student
	1. Experience: tough problem, requires some thinking, worth doing again
	2. Logic: Located inside the sql problem 1412
