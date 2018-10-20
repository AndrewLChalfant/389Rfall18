Writeup 7 - Forensics I
======

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 7 writeup

### Part 1 (40 pts)

1. File is a JPEG 

2. 875 N Michigan Ave, Chicago, IL, 60611 USA. John Hancock Center

3. 2018:08:22 11:33:24:801 - August 22nd, 2018

4. iPhone 8 Back Camera

5. 539.5 m Above Sea Level

6. Flag: "look_I_f0und_a_str1ng, with Strings + GREP on image file.
   Flag: "abr@cadabra" - binwalk

### Part 2 (55 pts)

I started by running 'file' on the supplied binary to see what we were working with. After finding that binary was an ELF. I decided to go ahead and run it, which didn't seem to do much. I then looked for any hidden by flags by using strings, "strings binary | grep flag" and "strings binary | grep cmsc" and found nothing useful besides the output "Where is your flag?", which was a good but unhelpful question (Still not sure if this led to a flag). 

I then switched to using objdump to try and see if the assembly backbone had any clues. After trying a couple different command flags, I settled for "objdump -d binary" and noticed a large section with many move commands and coordinating hex values. (0x2f, 0x74,0x6d,0x70,0x2f,0x2e,0x73,0x73,0x65,0x67,0x6f,0x0), which after being put through a hex to ascii converter game me "/temp/.stego"

After navigating to the related folder I found the .stego file but running "file" didn't give me any useful results. I then ran exiftools and saw that the file was likely a JPEG and showed message about an unknown header. I then used Strings on .stego which showed that the file was indeed a JFIF. 

After doing some Googling it looked like the file had a faulty magic bytes section due to two leading zeros. I removed the zeroes from the file and was able to generate the full JPEG image of a friendly dinosaur.

I then used steghide to guess passwords like hunter2, pokemon, password, as well as some common passwords from rockyou.txt, eventually I used stegosaurus and found the associated flag.

Flag: "dropping_files_is_fun"
