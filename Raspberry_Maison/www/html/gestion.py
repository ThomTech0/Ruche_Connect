"""
@author: thomaslesaulnier
"""
from fonction import graphique

class HTML:
    def insertion(adresse_IP,date_avant):
        import time
        from time import strftime
        fichier_transfert=open("transfert_data/fichier_recu.txt",'r')
        data_recu=fichier_transfert.readlines()
        fichier_transfert.close()
        data_recu=data_recu[0].split('/')

        #ESPACE LORAWAN & RECUPERATION DES DONNEES
        #Espace data stockage des données dans les variables.
        nom_ruche=str(data_recu[0])
        INF01=str(data_recu[1])
        INF02=str(data_recu[2])
        INF03=str(data_recu[3])
        balise_temperature_interieur=str(data_recu[4])
        balise_temperature_exterieur=str(data_recu[5])
        balise_humidite_interieur=str(data_recu[6])
        balise_humidite_exterieur=str(data_recu[7])
        balise_masse=str(data_recu[8])
        base_chant_royal_texte=str(data_recu[9])
        base_chant_royal_logo=str(data_recu[10])
        balise_heure=str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


        #Création d'une chaîne data
        web_data=["Ruche : "+nom_ruche,"#"+INF01,"#"+INF02,"#"+INF03,balise_temperature_interieur,balise_temperature_exterieur,balise_humidite_interieur,balise_humidite_exterieur,balise_masse,base_chant_royal_texte,base_chant_royal_logo,adresse_IP,balise_heure]

        #Créaction Graphique
        date=str(time.strftime('%Y-%m-%d', time.localtime()))
        if(date != date_avant):
            date_avant=date
            graphique.ajoute_masse(balise_masse)
        graphique.masse()


        #ESPACE WEB, INTERFACES HOMMES-MACHINES
        #Web_Ruche_Connecter

        #(1) Récupération de la page par défaut
        fichier=open("data_defaults/ruche_connecter.html",'r')
        web_default=fichier.readlines()
        fichier.close()

        #(2) Transfert des données sur la nouvelle page
        web=""
        for ligne in web_default:
            web=web+" \n "+str(ligne)

        web_default_list=["nom_ruche","#INF01","#INF02","#INF03","balise_temperature_interieur","balise_temperature_exterieur","balise_humidite_interieur","balise_humidite_exterieur","balise_masse","base_chant_royal_texte","base_chant_royal_logo","base_web_ip","balise_heure"]
        for i in range(0,len(web_data)):
                web=web.replace(web_default_list[i],web_data[i])
                
        #(3) Enregistrement de la nouvelle page
        fichier=open("interface_homme_machine/ruche_connecter.html",'w')
        fichier.write(web)
        fichier.close()
        return(date_avant)

