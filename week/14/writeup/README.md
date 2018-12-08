Writeup 14 - Web II
=====

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 10 Writeup

### Part 1 (40 Pts)
After viewing the different possible products listed on the site, I noticed the url was using sql syntax to retrieve data based on a specific user id. I played around with a couple different options such as trying to escape the input for the item and execute another SQL expression. In the end I found that simply bruteforcing different possible IDs work, and I eventually guessed an item ID of 1337 to get the flag CMSC38R-{y0U-are_the-5ql-n1nja}

After stumbling upon the flag I played with the input to recreate the flag by using 'or '1'='1, not sure why a capital OR wouldn't work.

### Part 2 (60 Pts)
1. Input "<script>alert();</script>" into search bar
	
	Since this was the first level, I assumed there wouldn't be any code escaping potentially malicious input. Added some basic Javascript to pull the alert up.

2. Input <button onclick=alert();>Hello</button> into blog post
	
	At first I tried the same method from level 1, but this didn't work. I guessed that script tags were being escaped by the site but HTML was still being rendered correctly. Inserted an alert popup into a HTML button and bingo.

3. Input /frame#3' onclick='alert()''; into URL
	
	Based on the provided source code looks like the image is being rendered directly from the URL parameter. I messed around with a few potential input syntaxs and eventually embedded another popup in the page.

4. Input ');alert();(' into input
	
	This was one of the trickier ones for me to solve. Look at the source code again to see the URL parameter was being passed directly into the controller. Figuring out that the last closing parentheses was needed took some trial and error.

5. Input ?next=javascript:alert(); into URL
	
	I tried the same approach from part 1 and part 2 before seeing that the email field wasn't being used after input. That left
only URL manipulation. After looking through the source code I saw that next is reached through href. Again, I wasn't sure about the correct syntax but after doing some research saw that 'javascript:' could be used to add JS to a href.

6. Input frame#hTtps://pastebin.com/raw/A2RXb4GF
	My initial thought is to replace the given JS file with a malicious one. I host my file on pastebin and try linking it, only to see that https is escaped by the regex, however, the regex isn't case sensitive so I was able to bypass it with some inner capitalization. 
