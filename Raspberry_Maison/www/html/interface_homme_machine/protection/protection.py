#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:58:32 2021

@author: thomaslesaulnier
"""

import time

class class_protection:
    def protection():

        from flask import Flask
        from flask import render_template
        from flask import request, url_for
        import socket
        import time

        Etat_Fermeture=0
        Etat_Ouverture=1

        serveur_web = Flask(__name__)

        #definir le texte à afficher selon le chemn de l'URL
        @serveur_web.route('/')    #page racine
        def principal ():
            return render_template('protection.html')

        @serveur_web.route('/',methods = ['POST'])
        def change():
            if request.method == 'POST' :
                if request.form['switch'] == 'FERMETURE':
                    fichier=open("fichier_protection.txt",'w')
                    fichier.write(str(Etat_Fermeture)+"/")
                    fichier.close()
                    print(Etat_Fermeture)
                
                if request.form['switch'] == 'OUVERTURE':
                    fichier=open("fichier_protection.txt",'w')
                    fichier.write(str(Etat_Ouverture)+"/")
                    fichier.close()
                    print(Etat_Ouverture)


            return render_template('protection.html')


        #programme principal
        serveur_web.debug = False
        serveur_web.run(host="0.0.0.0")
        
time.sleep(30)
class_protection.protection()
