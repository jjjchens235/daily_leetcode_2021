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

#### reverse intenger
1. Logic
	- start, keep track if is_negative
	- main logic: to get the last digit of a number mod by 10
	- add that digit to a string
	- Then remove that digit by // 10
	- end: check if is_negative, if true, add a negative sign to the string
2. Experience
	- This one sucked, I got the main logic after talking with Shing about this problem, but I had some issues with dealing with negative numbers
3. Takeaways
	- Don't forget your solution when actually coding it out, I knew what I had to do with negative numbers but lost sight of it
	- % 10 returns the last digit of any number

#### valid anagram
1. Logic: 
	- I converted each string to a Counter, then compared the counter agianst each other.
	- If Counter is not allowed, then have one for loop and within the same loop, using seperate dicts for each string add the respective character to the respective dictionary, then compare the dictionaries against each other

#### valid palindrome
1. Logic
	- clean the string using regex, and lower case it
	- Compared cleaned string reversed [::-1] vs itself
2. Takeaways
	- \^[a-z] means match all strings that start with a-z, whereas I needed to exclude a-z, so I would use [^a-zA-Z\d], note that I cannot use [^\w\d] because that includes _


#### 28: needle in the haystack (implement strstr)
1. Logic
	- Keep two pointers (actually only need 1, but it's easier to conceptualize as two), called start and end, where start and end capture the full substring length. For each haystack[start: end+1] substring compare it to needle
2. Takeaways
 	- I had to think about this problem quite a bit with regards to indexing and the correct conditions. After I decided to make start the beginning of the substring, and end the last index of the substring, it became much easier to conceptualize, because that meant end < len(needle), and for slicing it was always haystack[start: end + 1]

#### 38: Count and Say
1. Logic
	- Check if current character is the last repeating character. If not, continue incrementing count. If it is the last character, need to update the result string with (count) + (digit), and thenreset counter to 1.
	- To make things easier, add a placeholder char to the end
2. Experience
	- This one took a lot of time, and it was hard to solve, I wasn't sure if I should compare current against prev character or next characters
	- Wasn't fully sure on the conditional statements either
3. Takeaways
	- This problem is worth doing again, there's something about it that I find very tricky, even though it's not a complex problem

#### 14: Longest Common Prefix
1. Logic
	- Get the shortest str in the list
	- Compare the shortest str in the list against every item in the list starting at position 0
	- If shortest doesn't match a certain character of another string, remove that character and all subsequent characters from shortest
2. Experience
	- My first solution was pretty convolted, I used a dictionary of the first string in the list, and compared all values against this dictionary, and kept a minimum count of matched words
3. Takeaways
	- Shouldn't always default to dictionaries, when comparing strings against each other, oftentimes using list notation is good enough

### group anagram
1. logic: An str is an anagram of another str if after sorting each of the strings, they equal each other. To create a list of anagrams, we can sort each str in strs, and place it in a dictionary where k: v is sorted(str): [anagrams].
2. experience: pretty easy problem

### longest substring without repeats
1. logic: Two pointer, keep track of left and right. Left signifies the start of the window, right signifies the current end of the window.
	- for each right, add it to a dictionary, where k: v is char: index.
	- If s[right] already exists in the dictionary, then we need to move left to right + 1
2. Experience: my instincts were good that this was a sliding window problem and that we needed to keep track of the position of each string. It might be worth doing again though bc this problem is quite tricky

### Palindromic Substrings
1. Logic: 
	- For every char, treat it as the 'center' and compare its left and right elements with each other. If matching, continue, else break since no longer palindrome
	- Make sure to check for both even and odd length palindrome using the same 'center'
2. Experience: I looked at a hint, where I found out we wouldn't have to duplicate work by using a 'center'
3. Takeaways: 
	- To find a palindrome, often times it's a center problem. Each character is the 'center', and we bubble left and right from the center and compare those left and right characters against each other.
	- Palindromes can be both even and odd lengthed, meaning at each 'center', there are two conditons you need to check

### Num unique emails
1. Logic
	- For each email, apply the following rules:
		- remove periods from the first half of string
    - remove all words on and after the +
    - Push the updated word into a set
    - Return the length of the set
2. Experience
	- smooth except one mess-up, I didn't include the '@' back into the split string when concatting, I had to use a print statement to debug this, wasn't able to figure this out by walking through the code
3. Takeaways
	- Don't forgot about the word you split on if you need to re-concat string, in this case the '@'
	- If you need to find the index of the first occurrence of a char in a string/list, you can use index(), be aware that it returns a ValueError() if no element found, so better to check if exists in str/list

