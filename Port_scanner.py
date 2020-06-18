#!/bin/python3
import sys
import socket
import subprocess
from datetime import datetime as dt
t1=dt.now()
if sys.platform == "win32":
    subprocess.call("cls",shell=True)
if ((sys.platform) == "linux1" or (sys.platform) == "linux2"):
   subprocess.call("clear",shell=True) 
try:
    if (len(sys.argv))==4:
        target=socket.gethostbyname(sys.argv[1])
    else:
        print("invalid input parameters")
        print("Syntax: python3 ps.py <ip> <start_port> <end_port>")
    p1=abs(int(sys.argv[2]))
    p2=abs(int(sys.argv[3]))
    if p1>65534 or p2>65535:
        print("Ports numbers cannot exceed 0-65535")
        sys.exit()
    if p1>p2:
        p1,p2=p2,p1

    print("_"*32)
    print("Target ip : "+ target)
    print(f"Start_port:{p1}\tEnd_port:{p2}")
    print("Start Time : "+str(dt.now()  ))
    print("_"*32)
    

    for port in range(p1,p2+1):
        soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        result=soc.connect_ex((target,port))
        if result == 0:
            print("Port: {} is open".format(port))
        soc.close()

except KeyboardInterrupt:
    print("\nExiting the program")
    sys.exit()
except socket.gaierror:
    print("\nCould not resolve the host name")
    sys.exit()  
except socket.error:
    print("\nCheck your internet connection")
    sys.exit()
except IndexError:
    print("\nSyntaxError\nsyntax:python3 ps.py <ip> <start_port> <end_port>")
except NameError:
    print("please input all arguments\nsyntax:python3 ps.py <ip> <start_port> <end_port>")
    sys.exit()
t2=dt.now()
t=t2-t1
print("Time Lasted: "+str(t))   