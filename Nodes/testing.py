import socket
from datetime import datetime
net = input("Enter the IP address: ")
net1 = net.split('.')
a = '.'

net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Enter the Starting Number: "))
en1 = int(input("Enter the Last Number: "))
en1 = en1 + 1
t1 = datetime.now()

def scan(addr, port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    result = s.connect_ex((addr, port))

    if result == 0:
        return 1
    else :
        return 0

def run1():
    # these are a mix of Linux, Mac, and Windows Ports to search through
    port = [20, 21, 22, 23, 25, 80, 111, 443, 631, 993, 995, 135, 137, 138, 139, 445, 548]

    for ip in range(st1,en1):
        addr = net2 + str(ip)
        for i in port:
            if (scan(addr, i)):
                print (str(addr) , "is live at " + str(i))
            else:
                print (str(addr) , "is not alive and very much dead at " + str(i))
         
run1()
t2 = datetime.now()
total = t2 - t1
print ("Scanning completed in: " , total)