### Goal
Goal is to prepare for data engineering interviews at top tech companies. For DE, the most common data structures are going to be strings, arrays, and hash tables.

I will be going through the following list of string problems:
- [Leetcode Curated list](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/)
- [Yangshun](https://yangshun.github.io/tech-interview-handbook/algorithms/string/)

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

#### 334 Reverse String
1. Logic
	- Not using any native methods, I did a swap
2. Experience
	- Came up with the swap solution pretty quickly, I tried testing with pure strings, and I got an string immutable error. 
3. Takeaways
	- Need to read the problem more carefully (first step of CtC), didn't realize the argument was a list of chars and not a string
	- Inadvertedly, I re-discovered that you can't swap characters in a string due to immutability

#### 387 First Unique Char in a string
1. Logic
	- Two loops non-nested. First loop gets the count of occurences of each char as a counter object/dict. 
	- Second loop checks each char against the Counter, if the occurence is 1, then return the char's index
2. Experience
	- It took me around 5 minutes to figure out how to do this, I initially thought of using a counter, but assumed it would end up being n^2
3. Takeaways
	- 

#### reverse intenger
1. Logic
	- #start, keep track if is_negative
  - main logic: to get the last digit of a number mod by 10
  - add that digit to a string
  - Then remove that digit by // 10
  - end: check if is_negative, if true, add a negative sign to the string
2. Experience
	- This one sucked, I got the main logic after talking with Shing about this problem, but I had some issues with dealing with negative numbers
3. Takeaways
 - Don't forget your solution when actually coding it out, I knew what I had to do with negative numbers but lost sight of it
 - % 10 returns the last digit of any number
