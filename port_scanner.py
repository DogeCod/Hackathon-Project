import socket 
from queue import Queue
import threading
target = input("IP address (Thats on your network) -> ")
q = Queue()
for x in range(1,10001):
    q.put(x)
def portscan(port):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        conn = s.connect((target,port))  
        return True  
    except:
        return False
def worker():
    while True:
        port = q.get(x)
        if portscan(port):
            print(f'Port {port} is open')
for x in range(20000):
    t = threading.Thread(target=worker)            
    t.start()