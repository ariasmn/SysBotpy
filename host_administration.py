import platform
import getpass
import socket
import process_administration

class Host:

    def __init__(self, os, hostname, user_logged, ip_addr):
        self.os = os
        self.hostname = hostname
        self.user_logged = user_logged
        self.ip_addr = ip_addr

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def sendSystemInfo():
    if platform.system() == 'Linux':
        info = Host(platform.linux_distribution(), socket.gethostname(), getpass.getuser(), getIP())
        info.os = " ".join(info.so) #formatting. linux_distribution() returns a list of string, join them with an space between them. 
    elif platform.system() == 'Windows':
        print ("????")
    else:
        print ("????")
    return info
