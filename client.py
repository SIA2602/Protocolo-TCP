#!/usr/bin/env python3

import socket
import struct
from pathlib import Path
import sys

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

print("Sou o Cliente")

with open('arquivosTest/teste.txt', 'rb') as f: 
    dado = f.read() 
    
#for i in range(len(dado)):    
#    print(dado[i])

mesageOut = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    for i in range(len(dado)):          
        s.sendall(chr(dado[i]).encode('utf-8'))           
        data = s.recv(1024)        
        mesageOut.append(data)        

print('Received: ', repr(mesageOut))