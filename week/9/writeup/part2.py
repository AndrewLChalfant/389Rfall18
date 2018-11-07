#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data= s.recv(1024)

while(True):
    # use these to connect to the service

    # receive some data
    #print(data)
    if "win" in data:
        break
    method=""
    to_hash= ""
    hashed= ""
    x= 0
    data= data.split()

    for word in data:
        if (word == "the"):
            method= data[x+1]
        if (word == "of"):
            to_hash= data[x+1]
        x= x+1

    print(to_hash + " is requiring " + method)
    if (method == "sha512"):
        hashed= hashlib.sha512(to_hash).hexdigest()
    elif (method == "sha256"):
        hashed= hashlib.sha256(to_hash).hexdigest()
    elif (method == "md5"):
        hashed= hashlib.md5(to_hash).hexdigest()
    elif (method == "sha384"):
        hashed= hashlib.sha384(to_hash).hexdigest()
    elif (method == "sha1"):
        hashed= hashlib.sha1(to_hash).hexdigest()
    elif (method == "sha224"):
        hashed= hashlib.sha224(to_hash).hexdigest()

    s.send(hashed+"\n")
    data= s.recv(1024)
    print(data)

# close the connection
s.close()
