import socket
import os
import time
address_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
address = address_info[0][-1]
sock = socket.socket()
sock.connect(address)
while True:
    data = sock.recv(500)
    print(str(data, 'utf8'), end='')
