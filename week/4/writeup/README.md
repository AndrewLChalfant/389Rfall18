Writeup 3 - Pentesting I
======

Name: Andrew Chalfant 
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant 

## Assignment 4 Writeup

### Part 1 (45 pts)
Right flag: p1ng_as_a_serv1c3
Input: cornerstoneairlines.co; ls -a; cd home; ls -a; cat flag.txt

To find this flag I took advantage of Fred's usuage of the ping utility by chaining together multiple Linux commands. Fred is just passing the standard input into the ping utility and by not escaping user input, Fred is opening his server up to anyone who knows the port and IP combination. This project is similar to the cybersecurity project from 330. 

### Part 2 (55 pts)
I approached this problem by connecting the access to Fred's server I acheived through part 1 to the Python script stub we were given
