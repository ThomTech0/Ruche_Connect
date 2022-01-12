#----- A simple TCP client program in Python using send() function -----

import socket
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Sortie_Protection= 21
Sortie_Protection_Etat=False
GPIO.setup(Sortie_Protection,GPIO.OUT)




while True:
    # Create a client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    
    # Connect to the server
    clientSocket.connect(("10.3.141.1",9090));
    
    # Send data to server
    fichier_transfert=open("/media/pi/2821-0000/fichier_transfert.txt",'r')
    data=fichier_transfert.readlines()
    fichier_transfert.close()
    
    clientSocket.send(str(data[0]).encode());
    
    # Receive data from server
    dataFromServer = clientSocket.recv(1024);
    if(str(dataFromServer.decode())=="0"):
        Sortie_Protection_Etat= False
        
    else:
        Sortie_Protection_Etat= True
    GPIO.output(Sortie_Protection,Sortie_Protection_Etat)
    
    # Print to the console
    print(dataFromServer.decode());
    time.sleep(5)