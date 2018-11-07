#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')
hashes= open("../hashes",'r')
# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase
x= 0

for hashy in hashes:
    wordlist= open("../probable-v2-top1575.txt",'r')
    x= x + 1
    hashy= hashy.rstrip() #remove new line charcter

    for word in wordlist:
        word= word.strip()
        for salt in salts:
            salted= hashlib.sha512(salt+word).hexdigest()
            if (salted == hashy):
                print("Found Password: " +  word + " was salted with letter: " + salt + " in: " + hashy + "\n")
                break
