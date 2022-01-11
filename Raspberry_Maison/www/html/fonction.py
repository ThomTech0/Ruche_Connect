
"""
@author: thomaslesaulnier
"""

class graphique:
    def masse():
        #Graphique Masse
        import numpy as np
        import matplotlib.pyplot as plt
        fichier_poids=open("interface_homme_machine/graphique/poids.txt",'r')
        texte=fichier_poids.readlines()
        fichier_poids.close()
            
        
        texte_poids=texte[0].split('/')
        
        data_poids=[]
        data_date=[]
        
        if (len(texte_poids)>=30):
            i=len(texte_poids)-30
        else:
            i=0
            
        while(i<len(texte_poids)-1):
            data_poids.append(float(texte_poids[i]))
            i=i+1
            data_date.append(str(texte_poids[i]))
            i=i+1
        

        x = np.array(data_date)
        y = np.array(data_poids)
        plt.plot(x, y,'white',marker='o',linewidth=2)
        plt.axis('off')
        
     
        plt.xlabel('Date')
        plt.ylabel('Poids')
        plt.savefig("interface_homme_machine/graphique/poids.png",dpi=300,transparent=True)
        
        #Graphe précis
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)

        x = np.array(data_date)
        y = np.array(data_poids)
        plt.plot(x, y,'white',marker='o',linewidth=2)
        
        plt.xlabel('Date')
        plt.ylabel('Poids')
        plt.savefig("interface_homme_machine/graphique/poids_precision.png",dpi=300,transparent=True)
    
        
    def ajoute_masse(balise_masse):
        import time
        now = time.localtime(time.time())
        date=time.strftime("%d-%m", now)
        fichier_poids=open("interface_homme_machine/graphique/poids.txt",'r')
        texte=fichier_poids.readlines()
        fichier_poids.close()
        fichier=open("interface_homme_machine/graphique/poids.txt",'w')
        fichier.write(str(texte[0])+"/"+balise_masse+"/"+date)
        fichier.close()

class urgence:
    def mail():
        import smtplib
        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login("ruche3.0.1@gmail.com", "ezfbwwbsnhaekbyp")
        message = "Nous vous informons qu'un dysfonctionnement a eu lieu. Ainsi l'application ne peut actualiser les informations. Merci de contacter le SAV."
        serveur.sendmail("ruche3.0.1@gmail.com", "thomasdollet.tl@gmail.com", message)
        serveur.quit()
        
class adresse_IP:
    def IP_capture():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IP=s.getsockname()[0]
        s.close()
        return(IP)
    
    def fixe_IP():
        page_modif_IP=["ruche_hors_ligne.html","activites.html","conseil.html","index.html","protection/templates/protection.html"]
        
        IP=adresse_IP.IP_capture()
        
        for page in page_modif_IP:
            #(1) Récupération de la page par défaut
            fichier=open("data_defaults/"+page,'r')
            web_default=fichier.readlines()
            fichier.close()

            #(2) Transfert des données sur la nouvelle page
            web=""
            for ligne in web_default:
                web=web+" \n "+str(ligne)
                
            web=web.replace("base_web_ip",IP)
                    
            #(3) Enregistrement de la nouvelle page
            fichier=open("interface_homme_machine/"+page,'w')
            fichier.write(web)
            fichier.close()