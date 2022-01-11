"""
@author: thomaslesaulnier
"""
from gestion import HTML
from fonction import adresse_IP
from fonction import urgence

import time
print("lancement de chef orcherstre")
adresse_IP=adresse_IP.IP_capture()
date_avant=0

while True:
    try:
        date_avant=HTML.insertion(adresse_IP,date_avant)
        print("Cycle terminé")
        time.sleep(5)
    except :
        urgence.mail()
        break