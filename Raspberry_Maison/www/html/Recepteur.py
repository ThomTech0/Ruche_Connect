
#----- A simple TCP based server program in Python using send() function -----

import socket


# Create a stream based socket(i.e, a TCP socket)
# operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

 

# Bind and listen
serverSocket.bind(("10.3.141.1",9090));
serverSocket.listen();

 

# Accept connections
while(True):
    try:
        (clientConnected, clientAddress) = serverSocket.accept();
        print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));


        dataFromClient = clientConnected.recv(1024)
        print(dataFromClient.decode());
        fichier=open("transfert_data/fichier_recu.txt",'w')
        fichier.write(dataFromClient.decode())
        fichier.close()


        # Send some data back to the client
        fichier_transfert=open("interface_homme_machine/protection/fichier_protection.txt",'r')
        data_recu=fichier_transfert.readlines()
        fichier_transfert.close()
        data_recu=data_recu[0].split('/')
        clientConnected.send(str(data_recu[0]).encode());
        
    except KeyboardInterrupt:
        import smtplib
        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login("ruche3.0.1@gmail.com", "ezfbwwbsnhaekbyp")
        message = "Erreur de Communication"
        serveur.sendmail("ruche3.0.1@gmail.com", "thomasdollet.tl@gmail.com", message)
        serveur.quit()
        break
        
