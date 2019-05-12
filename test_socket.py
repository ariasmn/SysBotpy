import socket
import host_administration as hostadmin

SERVER_ADDR = "192.168.1.60"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", 1337))
server_socket.listen(15)

print ("Testing para proyecto\n")

sc, addr = server_socket.accept()

if addr[0] != SERVER_ADDR:
    sc.close()
    exit()

while True:
     
    received = (sc.recv(48000)).decode('utf8')

    if received.strip() == "info":
        info = hostadmin.sendSystemInfo()
        print (info.os)
    elif received.strip() == "apaga":
        hostadmin.shutdownHost()
    elif received.strip() == "reinicia":
        hostadmin.restartHost()
    else:
        print("No se reconoce el comando")