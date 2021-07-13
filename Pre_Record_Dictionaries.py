# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:44:20 2020

@author: dfial
"""
import pickle  ## Gestion d'enregistrement de la mémoire
import os
Lieu = os.getcwd()
############################################""
def Sauvegarde_Memoire(donn):
    Localisation=Lieu+"/Dico_memoire.pickle"
    pickle_out=open(Localisation,"wb+")
    pickle.dump(donn,pickle_out)
    pickle_out.close()
############################################""
############################################""
def Sauvegarde_Discussion(donn):
    Localisation=Lieu+"/Dico_discussion.pickle"
    pickle_out=open(Localisation,"wb+")
    pickle.dump(donn,pickle_out)
    pickle_out.close()
############################################""
Dico_memoire = {"##": {'coord': '**', 'bonjour':1},"bonjour":{"coord":"A1", "hello":1},"hello":{"coord":"B1","ça va bien":1},"ça va bien":{"coord":"C1","très bien merci":1},"très bien merci":{"coord":"D1","je suis le roi du monde":1},"je suis le roi du monde":{"coord":"E1","non pas du tout":1},"non pas du tout":{"coord":"F1","j'ai rendez-vous avec elle":1},"j'ai rendez-vous avec elle":{"coord":"G1","c'est amusant moi aussi":1},"c'est amusant moi aussi":{"coord":"H1","au revoir ordinateur":1},"au revoir ordinateur":{"coord":"I1","au revoir monsieur turingue":1},"au revoir monsieur turingue":{"coord":"J1","au revoir":1}}
Dico_discussion = {"**A1":{"B1":1},"A1B1":{"C1":1},"B1C1":{"D1":1},"C1D1":{"E1":1},"D1E1":{"F1":1},"E1F1":{"G1":1},"F1G1":{"H1":1},"G1H1":{"I1":1},"H1I1":{"J1":1}} 
Sauvegarde_Discussion(Dico_discussion)
Sauvegarde_Memoire(Dico_memoire)
