Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 2 writeup

### Part 1 (45 pts)

1. Real name: Fred Krueger

2. Personal Info: https://twitter.com/kruegster1990 - From Silver Spring, MD Born 1990 - Found through IntelTechniques and then CheckUsernames app. 
https://stwity.com/kruegster1990/ - 3rd result on a Google search for username (think this just scrapes Twitter). 
https://www.reddit.com/user/kruegster1990 - Second result on a Google search for username.
https://www.instagram.com/kruegster1990 - Instagram specific search for username. 
		
3. http://www.cornerstoneairlines.co - Found through his Twitter bio. IP Addresses: 142.93.118.186 by using the Ping utility on the hostname.

4. Hidden directory: http://www.cornerstoneairlines.co/secret/  Flag: fly_th3_sk1es_w1th_u5. Found by looking in robots.txt

5. 142.93.117.193 from Discover Linux utlity (also visible as the url of the admin page).

6. Digital Ocean, 10th floor of a building in NYC? - whois on second admin IP

7. Server OS: Apache/2.4.18 Ubuntu - Just a whois on the IP

8. h1dden_fl4g_in_s0urce.

Not a flag, but turns out Fred Krueger is actually Sean Maday. https://www.linkedin.com/in/seanmaday/ - https://twitter.com/seanmaday

### Part 2 (55 pts)
Flag: c0rn3rstone-air-27670

I first used npm to search for available ports on both the IPs. I saw that port 22 was open so I tried using that in the Python stub with a bunch of different changes and wasn't getting anywhere. Then I played around with nc and decided I had the wrong port, redid the npm scan with some extra flags and found port 1337 open. I then used the stub with the username "kruegster" as that's the email he listed. Edited the script to iterate over all the passwords in the rockyou.txt and made adjustments to break the loop once the password was found.

Took forever to figure out 'less' and 'grep' weren't gonna work for the server, eventually looked for more social media accounts and found the Instagram page. Used 'cat' to find the flag.

