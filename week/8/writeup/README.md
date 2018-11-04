Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Andrew Chalfant
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chalfant

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Traceroute on 142.93.118.186, cornerstoneairlines

2. laz0rh4x and c0uchpot4doz

3. laz0rh4x: 104.248.224.85 - North Bergen, NJ
   c0uchpot4doz: 206.189.113.189 - London, United Kingdom

4. Ports: 2749

5. Plans are readable with a parser through the linked file. Happening tomorrow at 1500

6. Sent a Google Doc link to the update.fpff file: 
https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view

7. They plan to see each other tomorrow at 1500

### Part 2 (55 Pts)

1. 20:40:07 on October 24th, 2018

2. laz0rh4x is the author

3. Says 9 sections, 11 section in file

4. Output:
------- HEADER -------
MAGIC: 0xdeadbeefL
VERSION: 1
TIMESTAMP: 2018-10-24 20:40:07
AUTHOR: laz0rh4x
SECTIONS: 9
-------  BODY  -------

====

Section 1 of size: 51
TYPE: Ascii found: Call this number to get your flag: (422) 537 - 7946

====
Section 2 of size: 60
TYPE: Words found: 
(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9)

====
Section 3 of size: 16
TYPE: Coordinates found: 38.99161,-77.02754

====
Section 4 of size: 4
TYPE: Reference found: 1

====
Section 5 of size: 60
TYPE: Ascii found: The imfamous security pr0s at CMSC389R will never find this!

====
Section 6 of size: 991
TYPE: Ascii found: The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

====
Section 7 of size: 16
TYPE: Coordinates found: 38.9910941,-76.9328019

====
Section 8 of size: 245614
TYPE: Png found: 1.png

====
Section 9 of size: 22
TYPE: Ascii found: AF(saSAdf1AD)Snz**asd1

====
Section 10 of size: 45
TYPE: Ascii found: Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9


====
Section 11 of size: 48
TYPE: Words found: 
(4, 8, 15, 16, 23, 42)


5. Flags:
CMSC389R- {PlaIN_dIfF_FLAG} from section 6, difference from actual text on Wikipedia

CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}, base64 decoder
