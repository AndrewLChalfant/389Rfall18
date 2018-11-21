Writeup 10 - Crypto II
=====

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 10 Writeup

### Part 1 (70 Pts)
I started by trying to manually connecting to the server and just trying random options to see what the formatting was like. I somehow managed to get the flag by accident (I guess just luck), early on in the project before I began to write my script.

Upon starting the script I first made sure my connection was setup correctly so I could pass in my sample message and receive a legit message from the server. Once I completed that, I created payloads with custom padding to try and crack the system. A lot of this was trial and error until I finally got the output I was looking for. 

I configured my output to only show once I hadn't seen the "Hmm" message which appeared for unsuccesful input. 


### Part 2 (30 Pts)
1.	To generate a key: 	gpg --gen-key
2.	To import a key: 	gpg --import pgassignment.key
3.	To encode a key:	gpg --output message.private encrypt and then enter information from listing output of step 2 (gpg --list-keys)

