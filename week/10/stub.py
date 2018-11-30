#!/usr/bin/env python2
# from the git repo
import md5py
import socket 

#####################################
### STEP 1: Calculate forged hash ###
#####################################

host= '142.93.118.186' #connect to server
port= 1234
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

message = 'hi'    # original message here

s.recv(2048)
s.send('1\n')
s.recv(1024)

s.send(message + '\n')
data= s.recv(1024)

legit= data[36:].strip() #parse servers hash
print("REAL HASH: " + legit)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'broken'
# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print("FAKE HASH: " + fake_hash)
s.recv(1024)

#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

for x in range(6,17):
	start= '\x80'
	middle= '\x00' * (64 - (x + 11)) #64 - lengths of messages
	end= chr(8*(2+x)) + '\x00'*7
	padding = start + middle + end

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
	
	payload = message + padding + malicious
	s.send('2\n')
	s.recv(4096)

	s.send(fake_hash + '\n')
	s.recv(4096)

	s.send(payload + '\n')
	s.recv(2048)

	data= s.recv(1024)
	if "Hmm" not in data:
		print("\nFLAG FOUND\n")
		print(data)
		break

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
