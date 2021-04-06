#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

par = True #se true eh par se false eh impar
invert = ""

print("Sou o Servidor")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    #mesageOut = ""
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)                  
            #print(data.decode('oem'))
            if(int.from_bytes(data, byteorder='big') > 0 and int.from_bytes(data, byteorder='big') < 255):                 
                if(par == True):
                    #print('{:08b}'.format(int.from_bytes(data, byteorder='big')))
                    invert = '{:08b}'.format(int.from_bytes(data, byteorder='big'))                    
                    if(invert[-1] == "0"):
                        lst = list(invert)
                        lst[-1] = "1"
                        invert = ''.join(lst)                         
                    else:
                        lst = list(invert)
                        lst[-1] = "0"
                        invert = ''.join(lst)                                    
                
                else:
                    #print('{:08b}'.format(int.from_bytes(data, byteorder='big')))
                    invert = '{:08b}'.format(int.from_bytes(data, byteorder='big'))                    
                    if(invert[0] == "0"):
                        lst = list(invert)
                        lst[0] = "1"
                        invert = ''.join(lst)                        
                    else:
                        lst = list(invert)
                        lst[0] = "0"
                        invert = ''.join(lst)                   

                if(int(invert, 2)%2 == 0):
                    par = True
                else:
                    par =  False                               

                #print(chr(int(invert, 2)), end="") 
                invert = chr(int(invert, 2))                                

            if not data:
             break                        

            if(int.from_bytes(data, byteorder='big') == 0 or int.from_bytes(data, byteorder='big') == 255):                               
                conn.sendall(data)
            else:
                conn.sendall(bytes(invert, encoding='utf8'))