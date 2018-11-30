#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

time= struct.unpack("<L", data[8:12])[0]
auth= struct.unpack("<8s",data[12:20])[0]
sec= struct.unpack("<L", data[20:24])[0]

print("TIMESTAMP: %s" % datetime.datetime.fromtimestamp(time))
print("AUTHOR: " + auth)
print("SECTIONS: %s" % sec)

print("-------  BODY  -------")

index= 24
for a in range(11):
    sec= struct.unpack("<L", data[index:index+4])[0]
    index+= 4
    size= struct.unpack("<L", data[index:index+4])[0]
    index+= 4
    print("====")
    print("Section " + str(a+1) + " of size: " + str(size))

    if sec==1:
        png= struct.unpack("<%ds" % size, data[index:index+size])[0]
        f= open("found.png","w")
        f.write(png)
        f.close()
        print("TYPE: Png found: " + str(sec) + ".png")

    elif sec==2:
        temp= size/8
        words= struct.unpack("<%dq" % temp, data[index:index+size])
        print("TYPE: Words found: ")
        print(words)

    elif sec==3:
        temp= struct.unpack("<%ds"%size, data[index:index+size])[0]
        print("TYPE: UTF found: " +utf_text.encode('utf-8'))
                
    elif sec==4:
        for a in range(0, size, 8):
            temp= struct.unpack("<d", data[index+a:index+a+8])[0]
            print("TYPE: Doubles found: " + temp)

    elif sec==5:
        s= size/4
        temp= struct.unpack("<%dL"%s, data[index:index+size])
        print("TYPE: Words found: ")
        print(temp)

    elif sec==6:
        x= struct.unpack("<d", data[index:index+8])[0]
        y= struct.unpack("<d", data[index+8:index+16])[0]
        print("TYPE: Coordinates found: " + str(x) + "," + str(y))

    elif sec==7:
        temp= struct.unpack("<L", data[index:index+size])[0]
        print("TYPE: Reference found: " + str(temp))

    elif sec== 9:
        temp= struct.unpack("<%ds" % size, data[index:index+size])[0]
        strd= ""
        for a in temp:
            strd.join(a)
        print("TYPE: Ascii found: " + temp.encode('ascii'))

    ##########
    index+= size
    
