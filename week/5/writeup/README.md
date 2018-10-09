Writeup 5 - Binaries I
======

Name: Andrew Chalfant 
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 5 Writeup

The last time I used Assembly was in 216, so going into this project I was pretty rusty. Low level languages have never really been a strength of mine so it was somewhat frustrating to have to leave Python to write x86. I tried to look at some of my 216 work but settled for watching a YouTube tutorial instead. 

To get started I looked over the example code posted which reminded me of the basic looping structure I needed to implement. From there I tried to use Godbolt to port the C code to Assembly, but found the implementation long and somewhat unwieldy. I then reverted back to just looking over the example code and wrote the two loops myself. Both functions had to perform similar tasks, so I was able to reuse the same logic for iterating over the character array.

The only real difference I saw in my implementation was my_memset a character was able to be directly put into the array location in memory, while my_strncpy required the storage of the relevant character in a temporary register. I accomplished this change by just using bl to store the 1 byte character. If I were to rewrite this program now, I would trace out each step of the intended functionality before starting to code, to get a feel for how the data will be moved around. 

One somewhat frustrating note: I was not able to run the makefile given per Josh's answer to a Piazza question (architecture incompatible with i386). I'd rather not install and setup a whole other VM for one homework assignment, so I'm just crossing my fingers that my output is correct. I've looked over the code and everthing seems like it should work alright, but who knows.  

