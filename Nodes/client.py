"""
By: Joe Meyer
"""
import ctypes, sys, socket, subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# finds the IP and get the
def findIP():
    print(socket.gethostname())
    #print(socket.gethostbyaddr())
    input("Press enter to continue")

if is_admin():
    findIP()
    for ping in range(1,256): 
        address = "192.168.4." + str(ping) 
        res = subprocess.call(['ping', '-c', '3', address]) 
        if res == 0: 
            print( "ping to", address, "OK") 
            print(socket.gethostbyaddr(address))
        elif res == 2: 
            print("no response from", address) 
        else: 
            print("ping to", address, "failed!")

    input("Press enter and exit")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)