Writeup 3 - Pentesting I
======

Name: Andrew Chalfant 
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant 

## Assignment 4 Writeup

### Part 1 (45 pts)
Flag for this homework: p1ng_as_a_serv1c3
Input I used: cornerstoneairlines.co; ls -a; cd home; ls -a; cat flag.txt;

To find the flag in this project I took advantage of Fred's usage of the ping utility by chaining together multiple Linux commands to access the Cornerstone Airlines file system. Fred is just passing the standard input directly into the ping utility. By not escaping user input, Fred is opening his server up to attacks from anyone who knows the port and IP combination. This project is similar to the cybersecurity project from 330, so I found this part fairly straight forward. I originally tried to pipe in a file with bash could that would search for a flag, but I ended up finding it quickly using trial and error (looking in the home directory, only seeing one file). If the flag were hidden among a whole directory of dummy flags like the previous project, piping in a file would probably have been necessary. Once a user gains access to a server and file system (despite if the account has sudo/admin access) like this, it's extremely easy to cause a massive amount of damage. Stolen private information could lose Fred a lot of business and could even get him sued.  

Fred could pretty easily secure his server from XSS attacks by escaping the user input he receives. Blocking semi-colons or spaces would help ensure that only valid input is being used. Alternatively, Fred could makes sure his users are required to input some type of password to connect to the uptime utility. If Fred really wanted to make the up-time application secure, he could develop a regular expression that checks if the user-input is either a valid IP address or a valid domain name. To be extra cautious, Fred could also track the IP addresses of those who input malicious data and could individually blacklist them from his different domains.

### Part 2 (55 pts)
I approached this problem by connecting the access to Fred's server I achieved through part 1 with the Python script we wrote for last weeks homework assignment. I was not sure if it was possible to establish a persistent connection through our method of access, instead I decided to establish a new connection every time the user input a command (after they had requested access with the 'shell' command). In cases of directory changes, I stored the previously entered information to give the illusion of a fully functional and persistent shell.

I found that the 'help' and exit commands were straight forward as I simply had to print out the given information and break the command loop respectively. However, figuring out how to pull files to my local machine was challenging. I first attempted to pull the files using SCP or FTP but decided since we don't know the admin password, it would be more straight forward just to 'cat' the relevant files and store the output as a local file. This approach could become inefficient when handling large files (where it might be easier to use tar), but for our use case of simple text files, a more complicated approach isn't necessary. I did have some difficulties with storing the file in a root directory, but this could just be an issue of inexperience with the Kali VM.  
