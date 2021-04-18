### Goal
Goal is to prepare for data engineering interviews at top tech companies. For DE, the most common data structures are going to be strings, arrays, and hash tables.

I will be going through the following list of array problems:
- [Leetcode Curated list](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/)
- [Yangshun](https://yangshun.github.io/tech-interview-handbook/algorithms/array/)

#### Template
For each question, I will provide the following:

1. Logic
	- df
2. Experience
	- df
3. Takeaways
	- df

#### Cracking the code interview
I want to follow the following routine for each problem, taken from Cracking the Code
1. Listen - pay very close attention to the description
2. Try (draw) an example
	1. make sure it's not too small, and not an edge case
3. Implement Brute force
4. Optimize using BUD
	1. bottleneck
	2. unnecessary work
	3. duplicated work
5. walk through the optimal solution in detail before coding
6. Implement
7. Test
	1. conceptual test
	2. unusual or non-standard code
	3. hot spots 
			1. arithmetic
			2. null
	4. small test cases
	5. special cases

####  26: remove duplicates
1. Logic
	- If the current number == prev number, delete the current number
2. Experience
	- So LC is able to check not enough your return value, but also the internal list value to make sure you modified it in place
3. Takeaways
	- When deleting from an array:
		- you need to use a while loop or else your indexes get messed up.
		- don't increment when you delete

### buy and sell stock #1
1. Logic
	- keep track of the min price, and at each number check what your profit would be if buying at min price
2. Experience
	- df
3. Takeaways
	- df

### buy and sell stock #2
1. Logic
	- buy if price < next_price
	- once we buy, sell if sell_price > next_sell_price
2. Experience
	- I got tripped up on how to know when we bought already before we can call sell
3. Takeaways
	- The key is to realize we must always buy before we can sell, and we only buy if the very next number is bigger
	- Once we buy, we know the next number is our min sell price, but we want to check if there are better sell prices after the next sell price, so we need to keep checking sell prices until we reach a number that is no longer increasing


### rotate array
1. Logic
	- Brute force solution is to shift each element to the right k times
	- To shift an element to the right, you need to to keep 2 temp variables, prev and temp, this logic is very similiar to linkedlist problem
	- Another solution that is O(n) is to create a new array and store the values offset by k 
2. Experience
	- The brute force solution took me forever, I thought of using two temp variables, but for some reason I was thinking it couldn't be correct
3. Takeaways
	- Even if the solution (two temp variables) seems strange or too hard to implement, you should still try if there's no way to use one temp var


### Single number
1. Logic
	- For an O(n\*2) solution, I used a dictionary, two pass, first pass is to populate the dictionary k, v number: count, and the second pass is to return a number with a count of 1 
2. Experience
	- df
3. Takeaways
	- To get O(n) solution one pass solution, you need to use a set, append all numbers, and then remove from set when that number appears the 2nd time.
	- Also, I didn't realize that all numbers either occured once or twice, I thought duplicates could appear more than once, I need to be careful about these little details because the set solution requires duplicates only appearing twice
