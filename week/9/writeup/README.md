Writeup 9 - Crypto I
=====

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 9 Writeup

### Part 1 (60 Pts)
In order to brute force password combinations, I started by first iterating over the hashes given to us, then I iterated again over all the possible pre-pended salt options and while combinining them with the passwords found in the text file. I next used the hashlib() function to create a hash of the prepended letter + password to give the output hash. Finally, I compared those hashes with the ones provided to see which combinations were correct.

Initially I ran into some issues with checking the equality of the given and generates hashes.To solve this, I stripped the new line from the hash I was reading in and as well as stripped the password from the given file. After those adjustments, my script was able to print out the matching passwords. 
![Image of Yaktocat](https://i.gyazo.com/71a480cbf846373c79fd668fb39f8b0d.png)


### Part 2 (40 Pts)
To solve the trivial puzzle, I first directly connected to the supplied IP and port through the command line, just to see what the potential input and output were. By doing this is, I figured out the various different hashing methods needed.

I then used the script from hw4 as an outline for the connection functionality. By printing out the output data, I was able to parse the output for a hashing method and requested string to hash. I then used those parameters to create an output hash which I passed back to the connection.

I surrounded that code in a loop that would iterate forever until I saw the flag in the output. Lastly, I added a statement to cut off the loop once "win" was seen in the output text. 

Flag: CMSC389R-{H4sh-5l!ngInG-h@sH3r}

![Image of Yaktocat](https://i.gyazo.com/b723e232c3383a643d798a243faea0b9.png)
![Image of Yaktocat](https://gyazo.com/5466db784749de099032051dabd0c312)

