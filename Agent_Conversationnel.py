# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sqlite3
from time import gmtime, strftime
from Record_ext1 import *   ## Important car import la méthode extérieure rec()
import speech_recognition as sr  ## module de reconnaissance verbale API Google (internet branché)
import sounddevice as sd
from scipy.io.wavfile import write ## enregistrer des fichiers WAV à partir de données
import wavio as wv 
from Reconn2_ext import *
#from Reconnaitre3_self import * ## Module necessitant detre en exterieur
#from Reconn_Face import *
import socket
import pickle  ## Gestion d'enregistrement de la mémoire
import os  ## gestion de la localisation des fichiers
import random  ##  Gestion du hasard
import pyttsx3  ## pour parler
Lieu = os.getcwd()   ## repérage du lieu de travail
#####   Demmarage du moteur de paraole  ######
engine = pyttsx3.init()
# Set properties _before_ you add things to say
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
#########################################################""
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import sys
import time
from PIL import Image
import matplotlib
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import numpy
import statistics
from itertools import chain
import imageio
import webbrowser
###################################################
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QApplication 
from PyQt5.QtWidgets import QFrame 
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QVBoxLayout 
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QDial
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QAbstractScrollArea
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage 
from PyQt5.QtGui import QPainter 
from PyQt5.QtGui import QPen 
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import QTimer 
from PyQt5.QtCore import QPoint 
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QRect
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QMetaObject
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1359, 700)
        Form.setStyleSheet("background-color: rgb(173, 173, 173);")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(10, 100, 640, 480))
        self.image_label.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.image_label.setObjectName("image_label")
        self.Interaction = QtWidgets.QTextEdit(Form)
        self.Interaction.setGeometry(QtCore.QRect(10, 610, 641, 81))
        self.Interaction.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 127);\n"
"")
        self.Interaction.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Interaction.setReadOnly(True)
        self.Interaction.setObjectName("Interaction")
        self.Apprentissage = QtWidgets.QTextEdit(Form)
        self.Apprentissage.setGeometry(QtCore.QRect(790, 20, 541, 551))
        self.Apprentissage.setStyleSheet("border-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 255, 255);")
        self.Apprentissage.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Apprentissage.setReadOnly(True)
        self.Apprentissage.setObjectName("Apprentissage")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 501, 91))
        self.groupBox.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.Apprenti = QtWidgets.QRadioButton(self.groupBox)
        self.Apprenti.setGeometry(QtCore.QRect(160, 50, 101, 31))
        self.Apprenti.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.Apprenti.setObjectName("Apprenti")
        self.Interract = QtWidgets.QRadioButton(self.groupBox)
        self.Interract.setGeometry(QtCore.QRect(270, 50, 91, 31))
        self.Interract.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.Interract.setChecked(False)
        self.Interract.setObjectName("Interract")
        self.ReconnFac = QtWidgets.QRadioButton(self.groupBox)
        self.ReconnFac.setGeometry(QtCore.QRect(10, 50, 141, 31))
        self.ReconnFac.setStyleSheet("background-color: rgb(255, 79, 48);\n"
"border-color: rgb(85, 85, 0);")
        self.ReconnFac.setObjectName("ReconnFac")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.Dictio = QtWidgets.QRadioButton(self.groupBox)
        self.Dictio.setGeometry(QtCore.QRect(110, 10, 121, 31))
        self.Dictio.setStyleSheet("background-color: rgb(255, 185, 254);")
        self.Dictio.setObjectName("Dictio")
        self.Dictio_2 = QtWidgets.QRadioButton(self.groupBox)
        self.Dictio_2.setGeometry(QtCore.QRect(260, 10, 101, 31))
        self.Dictio_2.setStyleSheet("background-color: rgb(221, 0, 166);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.Dictio_2.setObjectName("Dictio_2")
        self.Ordis = QtWidgets.QRadioButton(self.groupBox)
        self.Ordis.setGeometry(QtCore.QRect(380, 20, 101, 61))
        self.Ordis.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 0);")
        self.Ordis.setObjectName("Ordis")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 0, 131, 91))
        self.groupBox_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.Vocal = QtWidgets.QRadioButton(self.groupBox_2)
        self.Vocal.setGeometry(QtCore.QRect(10, 20, 82, 31))
        self.Vocal.setObjectName("Vocal")
        self.Ecrit = QtWidgets.QRadioButton(self.groupBox_2)
        self.Ecrit.setGeometry(QtCore.QRect(10, 60, 61, 17))
        self.Ecrit.setChecked(True)
        self.Ecrit.setObjectName("Ecrit")
        self.Vocal_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.Vocal_2.setGeometry(QtCore.QRect(70, 30, 61, 41))
        self.Vocal_2.setObjectName("Vocal_2")
        self.Interaction_2 = QtWidgets.QTextEdit(Form)
        self.Interaction_2.setGeometry(QtCore.QRect(10, 581, 641, 31))
        self.Interaction_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 127);\n"
"")
        self.Interaction_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Interaction_2.setReadOnly(True)
        self.Interaction_2.setObjectName("Interaction_2")
        self.Miniature1 = QtWidgets.QLabel(Form)
        self.Miniature1.setGeometry(QtCore.QRect(790, 570, 131, 101))
        self.Miniature1.setStyleSheet("background-color: rgb(87, 87, 130);")
        self.Miniature1.setObjectName("Miniature1")
        self.Mintext1 = QtWidgets.QTextEdit(Form)
        self.Mintext1.setGeometry(QtCore.QRect(790, 670, 131, 31))
        self.Mintext1.setObjectName("Mintext1")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(680, 20, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "\" Agent Conversationnel : Libre Arbitre Pondere\" (David Fialaire _ Novembre 2020 _ Version 1.0)"))
        self.image_label.setText(_translate("Form", "TextLabel"))
        self.groupBox.setTitle(_translate("Form", "Modes"))
        self.Apprenti.setText(_translate("Form", "Apprentissage"))
        self.Interract.setText(_translate("Form", "Interraction"))
        self.ReconnFac.setText(_translate("Form", "Reconnaissance faciale"))
        self.radioButton.setText(_translate("Form", "Intro"))
        self.Dictio.setText(_translate("Form", "Gestion Dictionnaire"))
        self.Dictio_2.setText(_translate("Form", "Reset Dicos"))
        self.Ordis.setText(_translate("Form", "Entre 2 \n"
"ordinateurs"))
        self.groupBox_2.setTitle(_translate("Form", "Type d\'echanges :"))
        self.Vocal.setText(_translate("Form", "Vocaux\n"
"lents"))
        self.Ecrit.setText(_translate("Form", "Ecrits"))
        self.Vocal_2.setText(_translate("Form", "Vocaux \n"
"rapides"))
        self.Miniature1.setText(_translate("Form", " _Reconnaissance requise"))
        self.pushButton.setText(_translate("Form", "Re_init !"))
###################################################
class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.showFullScreen()
        self.showMaximized()
        ############################################
        self.Dico_Entree={}
        self.Dico_Sortie={}
        self.Dico_Sort={}
        ### Ne pas activer la ligne suivante quand on démarre de zéro 1 apprentissage ! ###
        self.Donnees=self.Lecture_Apprentissage()
        ##############################################################
        self.list_lettre=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        #def remplissage_tableau(dictio):
        self.dico_tab={}
        self.Dico_memoire={}
        self.Dico_discussion={}
        self.discut=[0,0,0,0]
        self.Entree=""
        self.Sortie=""
        self.coordo="-"
        self.entree_entree=0
        self.taille_discut=0
        self.dico_val={} 
        self.bonjour_dit=0
        self.Dico_coord_cle={}
        self.red=0
        ###        
        Localisation=Lieu+"/Dico_memoire.pickle"
        pickle_in=open(Localisation,"rb")
        self.Dico_memoire=pickle.load(pickle_in)
        pickle_in.close()
        ###
        self.List_Cle_Dico_memoire=list(self.Dico_memoire.keys())
        print("\nList_Cle_Dico_memoire = ",self.List_Cle_Dico_memoire)
        Long_List_Cle_Dico_memoire=len(self.List_Cle_Dico_memoire)
        for i in range(Long_List_Cle_Dico_memoire):
            sous_dico=self.Dico_memoire.get(self.List_Cle_Dico_memoire[i],"N0")
            coord=sous_dico.get("coord","N0")
            self.Dico_coord_cle[coord]=self.List_Cle_Dico_memoire[i]
        print("\nDico_coord_cle = ",self.Dico_coord_cle)
###########################################
        Localisation=Lieu+"/Dico_discussion.pickle"
        pickle_in=open(Localisation,"rb")
        self.Dico_discussion=pickle.load(pickle_in)
        pickle_in.close()
        print("\nself.Dico_discussion = ", self.Dico_discussion )
###########################################""
        self.Dico_Entree=self.Donnees 
        self.BoutEcrit=1
        self.tre=0
        self.fin=0
        self.visio=0
        self.qs=""
        self.init=1
        self.continu=1
        self.stop=0
        self.synonyme=0
        self.syno=0
        self.Raccord=0
        self.VocalLent=1
        self.twordis=0
        self.firstword=1
        self.initwordis=1
        self.exserveur=0
        #############################################9
        self.fond()
        self.ui.Interract.toggled.connect(self.interraction)
        self.ui.Dictio.toggled.connect(self.memoire)
        self.ui.Apprenti.toggled.connect(self.apprentissage)
        self.ui.ReconnFac.toggled.connect(self.ControlCam)
        self.ui.radioButton.toggled.connect(self.Intro)        
        self.ui.Ecrit.toggled.connect(self.FoncEcrit)
        self.ui.Vocal.toggled.connect(self.FoncVocalLent)
        self.ui.Vocal_2.toggled.connect(self.FoncVocalRapide)
        self.ui.Dictio_2.toggled.connect(self.Charge)
        self.ui.Ordis.toggled.connect(self.two_ordis)
        self.ui.pushButton.clicked.connect(self.reinit)
        
        
        ############################################
        ## Contrôle de temps pour la caméra ##
        self.timer = QTimer()
        self.cap=0        
        self.timer.timeout.connect(self.RecFace)
############################################
    def reinit(self):
        ############################################
        print("coucou, passage par réinit")
        self.Dico_Entree={}
        self.Dico_Sortie={}
        self.Dico_Sort={}
        ### Ne pas activer la ligne suivante quand on démarre de zéro 1 apprentissage ! ###
        self.Donnees=self.Lecture_Apprentissage()
        ##############################################################
        self.list_lettre=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        #def remplissage_tableau(dictio):
        self.dico_tab={}
        self.Dico_memoire={}
        self.Dico_discussion={}
        self.discut=[0,0,0,0]
        self.Entree=""
        self.Sortie=""
        self.coordo="-"
        self.entree_entree=0
        self.taille_discut=0
        self.dico_val={} 
        self.bonjour_dit=0
        self.Dico_coord_cle={}
        self.red=0
        ###        
        Localisation=Lieu+"/Dico_memoire.pickle"
        pickle_in=open(Localisation,"rb")
        self.Dico_memoire=pickle.load(pickle_in)
        pickle_in.close()
        ###
        self.List_Cle_Dico_memoire=list(self.Dico_memoire.keys())
        print("\nList_Cle_Dico_memoire = ",self.List_Cle_Dico_memoire)
        Long_List_Cle_Dico_memoire=len(self.List_Cle_Dico_memoire)
        for i in range(Long_List_Cle_Dico_memoire):
            sous_dico=self.Dico_memoire.get(self.List_Cle_Dico_memoire[i],"N0")
            coord=sous_dico.get("coord","N0")
            self.Dico_coord_cle[coord]=self.List_Cle_Dico_memoire[i]
        print("\nDico_coord_cle = ",self.Dico_coord_cle)
###########################################
        Localisation=Lieu+"/Dico_discussion.pickle"
        pickle_in=open(Localisation,"rb")
        self.Dico_discussion=pickle.load(pickle_in)
        pickle_in.close()
        print("\nself.Dico_discussion = ", self.Dico_discussion )
###########################################""
        self.Dico_Entree=self.Donnees 
        self.BoutEcrit=1
        self.tre=0
        self.fin=0
        self.visio=0
        self.qs=""
        self.init=1
        self.continu=1
        self.stop=0
        self.synonyme=0
        self.syno=0
        self.Raccord=0
        self.VocalLent=1
        self.twordis=0
        self.firstword=1
        self.initwordis=1
        self.exserveur=0
        self.Intro()
        #############################################
############################################
    def ServeurParle(self):
        print("\nOn est dans le serveur.. on passe à l'écoute")
        # Source : https://python.doctor/page-reseaux-sockets-python-port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', 15555))
        Alecoute=True        
        while Alecoute:
                sock.listen(5)
                serveur, address = sock.accept()
                print ("{} connected".format( address ))        
                reponse = serveur.recv(255)
                if reponse != "":
                        horloge=strftime("%Y-%m-%d %H:%M:%S")
                        print("horloge reçue réponse = ",horloge)
                        print("Reçue du client : ",reponse)
                        
                        if reponse==b"jecoute":
                            if self.firstword==1:
                                horloge=strftime("%Y-%m-%d %H:%M:%S")
                                print("horloge first world = ",horloge)
                                print("first word")
                                time.sleep(1)
                                phrase="bonjour"
                                engine.say(phrase)
                                engine.runAndWait()
                                self.firstword=0
                                Alecoute=True   
                            else:
                                Alecoute=True
                                horloge=strftime("%Y-%m-%d %H:%M:%S")
                                print("horloge serveur va parler = ",horloge)
                                print ("\nServeur va fermer.. peut parler Sortie")
                                #time.sleep(1)
                                phrase=self.Sortie
                                time.sleep(1)
                                engine.say(phrase)
                                engine.runAndWait()
                                serveur.close()
                                sock.close()
                                retour_serveur=2
                                return retour_serveur
                        if reponse==b"change":
                            self.firstword=0
                            horloge=strftime("%Y-%m-%d %H:%M:%S")
                            print("horloge Serveur changement = ",horloge)
                            print("\nchangement cote serveur")
                            print ("Passage en ordre 2")
                            Alecoute=False
                            serveur.close()
                            sock.close()
                            retour_serveur=2
                            self.ordre=2
                            return retour_serveur

############################################
    def Client(self,message):
        print("\n On est dans le client.. on va envoyer un message..")
        hote = str(self.ip_lui) # "192.168.1.33"
        port = 15555   
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((hote, port))
        print ("Connection on {}".format(port))
        if message=="jecoute":
            horloge=strftime("%Y-%m-%d %H:%M:%S")
            print("horloge Client Envoie jecoute = ",horloge)
            print("\n Client envoie jecoute...")
            sock.sendall(b"jecoute")
        elif message=="change":
            horloge=strftime("%Y-%m-%d %H:%M:%S")
            print("horloge Client Envoie change = ",horloge)
            print("\n Client envoie change et passe en ordre 1...")
            sock.sendall(b"change")
            self.ordre=1
            self.firstword=0
        print ("Close")
        sock.close()
        retour_client=2
        return retour_client
###########################
    def two_ordis(self):
        print("\n Passage par twordis ...")
        if self.fin==1:
#            self.stop=1
            print("6")
            self.ui.Ordis.setChecked(False)
            print("7")
            self.ui.radioButton.setChecked(True)
            print("8")
        else:
            if self.initwordis==1:
                self.Sortie="bonjour"
                self.initwordis=0
                self.BoutEcrit=0
                self.VocalLent=0
                self.twordis=1
                yep="<u><span style=\" color:#000000; \n font: 20pt \"MS Shell Dlg 2\";\n font-weight: bold;\" >"+"Interraction entre 2 ordinateurs. </span></u>"            
                self.ui.Apprentissage.setText(yep)
                self.ui.Apprentissage.append("\n")
                yep="<span style=\" color:#000000; \n font: 15pt \"MS Shell Dlg 2\";\n font-weight: bold;\" >"+"--> Définissez mon ordre de parole (1 ou 2 ) : </span>"            
                self.ui.Apprentissage.append(yep)
                self.ui.Apprentissage.append("\n")
                self.questi = QInputDialog()
                self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                text, ok = self.questi.getText(self,"2 Ordis : ", "Ordre de Paroles (1 ou 2) : ")
                self.ordre=int(text)

            
                if self.ordre<1 or self.ordre>2:
                    self.fin=1
                    print("1..")
                    self.ui.radioButton.setChecked(True)
        #            break
                else:
                    self.ip_moi=socket.gethostbyname(socket.gethostname())
                    yep="<span style=\" color:#000000; \n font: 15pt \"MS Shell Dlg 2\";\n font-weight: bold;\" >"+"Voici mon adresse IP : "+self.ip_moi+"</span>"            
                    self.ui.Apprentissage.append(yep)
                    self.ui.Apprentissage.append("\n")
                    yep="<span style=\" color:#000000; \n font: 15pt \"MS Shell Dlg 2\";\n font-weight: bold;\" >"+"Quelle est l'adresse IP de mon interlocuteur ? : Ex: 192.168.1.33 </span>"            
                    self.ui.Apprentissage.append(yep)
                    self.ui.Apprentissage.append("\n")
                    self.questi = QInputDialog()
                    self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                    self.ip_lui, ok = self.questi.getText(self,"Adresse IP... : ", "de l'autre Ordi : ")
                    if self.ip_lui=="m":
                        self.ip_lui="192.168.1.17" #33
                    elif self.ip_lui=="d":
                        self.ip_lui="192.168.1.22" #13
                    self.interraction()    
            else:
                self.interraction()    
################################
    def OuvreDialogOpen(self):
        # asksaveasfilename  # askopenfilename
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("pickle files","*.pickle"),("all files","*.*")))
        root.destroy()
        texte=root.filename
        return texte
##########################################
########################
    def Charge(self):
        if self.fin==1:
            self.ui.Dictio_2.setChecked(False)
            print("27")
            self.ui.radioButton.setChecked(True)
            print("28") 
        else:
            Openrootfilename=self.OuvreDialogOpen()
            position=1
            continu=True
            while continu:
                lettre=Openrootfilename[-position]
                if lettre=="/":
                    new_position=position
                    continu=False
                else:
                    Openrootfilename=Openrootfilename.rstrip(Openrootfilename[-1])
            ####
            mem=Openrootfilename
            Openrootfilename=mem+"Dico_discussion.pickle"
            pickle_in=open(Openrootfilename,"rb")
            After_Exist_List=pickle.load(pickle_in)
            pickle_in.close()
            self.Dico_discussion=After_Exist_List        
            Openrootfilename=mem+"Dico_memoire.pickle"
            pickle_in=open(Openrootfilename,"rb")
            After_Exist_List=pickle.load(pickle_in)
            pickle_in.close()
            self.Dico_memoire=After_Exist_List
            self.Sauvegarde_Memoire(self.Dico_memoire)
            self.Sauvegarde_Discussion(self.Dico_discussion)
            list_val_dico_tab=[]
            self.fin=1
            self.ui.Dictio_2.setChecked(False)
            print("27")
            self.ui.radioButton.setChecked(True)
            print("28")           
################################################
    def FoncSyno(self):
        self.synonyme=1
################################################
    def FoncNoSyno(self):
        self.synonyme=0
################################################
    def getProfile(self,id):
        conn=sqlite3.connect("FaceBase.db")
        cmd="SELECT * FROM People WHERE ID="+str(id)
        cursor=conn.execute(cmd)
        self.profile=None
        for row in cursor:
            self.profile=row
        conn.close()
        return self.profile
################################################""
    def ControlCam(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cam = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
        # if timer is started
        else:
            self.timer.stop()
            # release video capture
            self.cam.release()
################################################""
    def RecFace(self):
        if self.ui.ReconnFac.isChecked()==True:
            self.bonjour_dit=0
            self.visio=1
            faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
            rec=cv2.face.LBPHFaceRecognizer_create();
            rec.read("recognizer/trainningData.yml")
            path="dataSet"
            id=0
            font = cv2.FONT_HERSHEY_SIMPLEX
            while(True):
                ret,self.img=self.cam.read();
                gray=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
                faces=faceDetect.detectMultiScale(gray,1.3,5);
                for (x,y,w,h) in faces:
                    cv2.rectangle(self.img, (x,y), (x+w, y+h), (0, 255, 0), 2 )
                    id,conf=rec.predict(gray[y:y+h, x:x+w])                  
                    if conf>70:          # Plus la valeur de conf est élevé, moins l'algorithme a reconnu des visages
                        id = "inconnu {0:.0f}%".format(round(100 - conf, 2)) # Cela évite qu'il affiche un prénom avec un % négatif
                        cv2.putText(self.img,str(id),(x,y+h), font, 1, (255,255,255), 3);
                    else:
                        self.profile=self.getProfile(id)
                        if (self.profile!=None):
                            cv2.putText(self.img,str(self.profile[1]),(x,y+h+30), font, 1, (255,255,255), 3);
                            cv2.putText(self.img,str(self.profile[2]),(x,y+h+60), font, 1, (255,255,255), 3);
                            cv2.putText(self.img,str(self.profile[3]),(x,y+h+90), font, 1, (255,255,255), 3);
                            cv2.putText(self.img,str(self.profile[4]),(x,y+h+120), font, 1, (255,255,255), 3);
###########Ancienne présentation recface #########################"        
                self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
                height, width, channel = self.img.shape
                step = channel * width
                self.qImg = QImage(self.img.data, width, height, step, QImage.Format_RGB888)
                self.ui.image_label.setPixmap(QPixmap.fromImage(self.qImg))
                if(cv2.waitKey(1) ==ord("q")):
                    print("coucou")
                    self.qs=self.profile[1]
                    break;
            cam.release()
            cv2.destroyAllWindows()
            self.qs=self.profile[1]
###################################################
    def FoncVocalRapide(self):
        self.BoutEcrit=0
        self.VocalLent=0        
    def FoncVocalLent(self):
        self.BoutEcrit=0
        self.VocalLent=1
    def FoncEcrit(self):
        self.BoutEcrit=1
###################################################
    def reconn(self):
#        self.result=reconn2()
#        return self.result

        r = sr.Recognizer()
        audio = sr.AudioFile('recording1.wav')
        with audio as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio_file = r.record(source)
        try:            
#            self.result = r.recognize_google(audio_file, language="fr-FR")
            result = r.recognize_google(audio_file, language="fr-FR")
            print("result = ", result)

            #            self.ui.Mic_Ac.setChecked(False)
#            return self.result
            return result

        except sr.UnknownValueError:
#            self.ui.Mic_Ac.setChecked(False)
            print("Erreur 539")
#########################       Inutile !! ??     
    def mouseReleaseEvent(self, QMouseEvent):
        cursor_position = QCursor.pos()
        cursor_array = [int(cursor_position.x()), int(cursor_position.y())]
        x22=cursor_array[1]-72
        y22=cursor_array[0]-10
        if x22>479 and y22>639: #  if x22>489 and y22>649:
            ok=2
        elif x22>479 or y22>639:  # elif x22>489 or y22>649:
            ok=2
        else:            
            self.x2=x22
            self.y2=y22
            self.List_info_paquets=[]
#########################
    def Intro(self):
        #self.ui.Ecrit.setChecked(True)
        self.twordis=0
        self.stop=0
        self.tre=0
        self.fin=0
        self.pass_apprenti=0
        self.qs=""
        self.continu=1
        yep1="Voici mon Dictionnaire : "
        yep=str(self.Dico_memoire)
        self.ui.Interaction_2.setText(yep1)
        self.ui.Interaction.setText(yep)                
        if self.visio==1:
            self.fond()
            name=str(self.profile[1])
            name_format="Capt.jpg"
            imageio.imwrite(name_format, self.img[:, :])
            self.img_red= cv2.resize(self.img,(128,96))       
            height_red, width_red, channel_red = self.img_red.shape
            step_red = channel_red * width_red
            self.qImg_red = QImage(self.img_red.data, width_red, height_red, step_red, QImage.Format_RGB888)
            self.ui.Miniature1.setPixmap(QPixmap.fromImage(self.qImg_red))            
            self.ui.Mintext1.setText(name)        
        else:
            if self.init==1:
                self.fond()
                name=""
                self.init=0
            else:
                self.fond()
#########################
    def Quit(self):
        sys.exit(app.exec_())
#########################       
    def fond(self):
        img = Image.open("fond.jpg")
        self.image_contours = numpy.array(img)
        height, width, channel = self.image_contours.shape
        step = channel * width
        qImg = QImage(self.image_contours.data, width, height, step, QImage.Format_RGB888)
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))            
###################################################
#    ###############################################
#    ###    Enregistrement         #################
#    ###############################################
#    def enregistre(self):    ###   wavio        
#        print("\nok, on enregistre")
#        freq = 44100
#        # Recording duration 
#        duration = 5    ### 5
#        # Start recorder with the given values 
#        # of duration and sample frequency 
#        recording = sd.rec(int(duration * freq), 
#        				samplerate=freq, channels=2) 
#        # Record audio for the given number of seconds 
#        sd.wait() 
#        # This will convert the NumPy array to an audio 
#        # file with the given sampling frequency 
#    #####     write("recording0.wav", freq, recording)   ## precedemment : 2 fichier : le 0 est + gros
#        # Convert the NumPy array to audio file 
#        wv.write("recording1.wav", recording, freq, sampwidth=2) ## fichier1 + petit et fonctionnel
################################################
    def Lecture_Memoire(self):
        Localisation=Lieu+"/Dico_memoire.pickle"
        pickle_in=open(Localisation,"rb")
        self.Dico_memoire=pickle.load(pickle_in)
        pickle_in.close()
        return self.Dico_memoire
############################################""
    def Sauvegarde_Memoire(self,donn):
        Localisation=Lieu+"/Dico_memoire.pickle"
        pickle_out=open(Localisation,"wb+")
        pickle.dump(self.Dico_memoire,pickle_out)
        pickle_out.close()
        print("mémoire sauvegardée")
############################################""
###########################################
    def Lecture_Discussion(self):
        Localisation=Lieu+"/Dico_discussion.pickle"
        pickle_in=open(Localisation,"rb")
        self.Dico_discussion=pickle.load(pickle_in)
        pickle_in.close()
        return self.Dico_discussion
############################################""
    def Sauvegarde_Discussion(self,donn):
        Localisation=Lieu+"/Dico_discussion.pickle"
        pickle_out=open(Localisation,"wb+")
        pickle.dump(self.Dico_discussion,pickle_out)
        pickle_out.close()
        print("discussion sauvegardée")
############################################""
###########################################
    def Lecture_Apprentissage(self):   ##  Inutile !! ??
        Localisation=Lieu+"/Base_de_Donnees.pickle"
        pickle_in=open(Localisation,"rb")
        self.Donnees=pickle.load(pickle_in)
        pickle_in.close()
        return self.Donnees
############################################""
    def Sauvegarde_Apprentissage(self,donn):  ##  Inutile !! ??
        Localisation=Lieu+"/Base_de_Donnees.pickle"
        pickle_out=open(Localisation,"wb+")
        pickle.dump(self.Donnees,pickle_out)
        pickle_out.close()
############################################""
    def apprentissage(self):
        print("self.Raccord' =",self.Raccord)
        ### Gestion Apprentissage Synonymes ###
        if self.synonyme==1:  ##  Inutile !! ??
            print("synonyme")
        else:
            print("no synonyme")
            ### introduction paramètres discussion ###
            self.list_lettre=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            self.List_Cle_Dico_memoire=list(self.Dico_memoire.keys())
            print("List_Cle_Dico_memoire = ",self.List_Cle_Dico_memoire)
            Long_List_Cle_Dico_memoire=len(self.List_Cle_Dico_memoire)
            for i in range(Long_List_Cle_Dico_memoire):
                sous_dico=self.Dico_memoire.get(self.List_Cle_Dico_memoire[i],"N0")
                coord=sous_dico.get("coord","N0")
                self.Dico_coord_cle[coord]=self.List_Cle_Dico_memoire[i]
            print("Dico_coord_cle = ",self.Dico_coord_cle)
            self.dico_tab=self.Dico_coord_cle  ##  {}
            self.discut=[0,0,0,0]
            self.Entree=""
            self.Sortie="##"
            self.coordo="-"
            self.entree_entree=0
            self.taille_discut=0
            self.dico_val={}        
            ### Fin introduction paramètres discussion ###
            if self.fin==1:
                self.stop=1
                print("3")
                self.ui.Apprenti.setChecked(False)
                print("4")
                self.ui.radioButton.setChecked(True)
                print("5")
            else:
                if self.tre==1:
                    ok=1
                else:
                    if self.BoutEcrit==1:
                        tipeInter="par écrit."
                    else:
                        tipeInter="à l'oral."
                    yep="<u><span style=\" color:#006633; \n font: 20pt \"MS Shell Dlg 2\";\n font-weight: bold;\" >"+"Apprentissage : "+tipeInter+"</span></u>"            

                    self.ui.Apprentissage.setText(yep)
                    self.ui.Apprentissage.append("\n")
                    self.tre=1
                while True:
                    if self.pass_apprenti==1:
                        self.pass_apprenti=0
                        print("\n Gestion Apprentissage des éléments retournés de la discussion : \n")
                        ####################################### Gestion Apprentissage des éléments retournés de la discussion
                        if self.BoutEcrit==1:
                            yep="\nDonnez la sortie pour cette entrée qui était inconnue.. : "+self.Raccord
                            self.Entree=self.Raccord
                            self.ui.Apprentissage.append(yep)
                            self.ui.Apprentissage.append("\n")
                            ent=self.Entree                            
                            ##########
                            sous_dico=self.Dico_memoire.get(self.Entree,"N0")
                            print("\n self.Entree = ",self.Entree)
                            print("\n 522 sous_dico=self.Dico_memoire.get(self.Entree,'N0') = ",sous_dico)
                            if sous_dico !="N0":
                                print("\on a sous_dico !='N0' " )
                                synonyme_exist=sous_dico.get("synonyme_référent","N0")
                                print("\n synonyme_exist=sous_dico.get('synonyme_référent','N0'))",synonyme_exist)
                                if synonyme_exist=="N0":
                                    print("\n synonyme_exist : NON")
                                    rien=1
                                else:
                                    print("\n synonyme_exist on passe à self.Entree")
                                    self.Entree=synonyme_exist
                                    print("\nnouvelle self.entree = ",self.Entree)
                            else:
                                rien=1
                            ##########
                            print("\n Go Get_Entree ??")
                            self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire=self.Get_Entree()
                        else:
                            yep="\nDonnez la sortie pour cette entrée qui était inconnue.. : "+self.Raccord
                            self.Entree=self.Raccord
                            self.ui.Apprentissage.append(yep)
                            self.ui.Apprentissage.append("\n")
                            ent=self.Entree                            
                            ##########
                            sous_dico=self.Dico_memoire.get(self.Entree,"N0")
                            if sous_dico !="N0":
                                synonyme_exist=sous_dico.get("synonyme_référent","N0")
                                if synonyme_exist=="N0":
                                    rien=1
                                else:
                                    self.Entree=synonyme_exist
                                    print("\nnouvelle self.entree = ",self.Entree)
                            else:
                                rien=1
                            ##########
                            self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire=self.Get_Entree()

                    else:
                        if self.BoutEcrit==1:
                            self.questi = QInputDialog()
                            self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                            text, ok = self.questi.getText(self,"Apprentissage : ", "Donnez l'entrée : ")
                            self.Entree=text
                            self.Entree=self.Entree.lower()
                            if self.Entree=="":
                                self.fin=1
                                print("1..")
                                self.ui.radioButton.setChecked(True)
                                break
                            else:
                                yep="<u><span style=\" color:#339900; \n font-weight: bold;\" >"+"\nEntrée : "+"</span></u>"+self.Entree
                                self.ui.Apprentissage.append(yep)
                                self.ui.Apprentissage.append("\n")
                                ent=self.Entree
                                ##########
                                sous_dico=self.Dico_memoire.get(self.Entree,"N0")
                                if sous_dico !="N0":
                                    synonyme_exist=sous_dico.get("synonyme_référent","N0")
                                    if synonyme_exist=="N0":
                                        rien=1
                                    else:
                                        self.Entree=synonyme_exist
                                        print("\nnouvelle self.entree = ",self.Entree)
                                else:
                                    rien=1
                                ##########
                                self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire=self.Get_Entree()
##############################################                                 
                        else:
                            self.questi = QInputDialog()
                            self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                            text, ok = self.questi.getText(self,"Apprentissage : ", "Cliquez sur Entrée, et Parlez votre Entrée à l'ordinateur, ou Cancel pour sortir : ")
#                            if text=="":
#                                self.fin=1
#                                print("1")
#                                self.ui.radioButton.setChecked(True)
#                                break                            
                            self.Entree=text
                            self.Entree=self.Entree.lower()       
                            if text=="q":
                                break
                            else:
                                
                                self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")
#                                self.ui.Mic_Ferm.setChecked(False)
                                
                                rec("Je vous écoute :")
                                
#                                self.ui.Mic_Ac.setChecked(False)  
                                self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")
                                self.Entree=self.reconn()
                                print("\<nretour Enregistrement : self.Entree = ",self.Entree)
                                if self.Entree=="":
                                    self.fin=1
                                    print("1")
                                    self.ui.radioButton.setChecked(True)
                                    break
                                print("ok, revenu")
                                try:                       
                                    self.Entree=self.Entree.lower()
                                except AttributeError:
                                    print("Changements de bouton 12")
                                    self.fin=1
                                    self.stop=1
                                    self.ui.Ecrit.setChecked(True)
                                    print("12 2")
                                    self.ui.radioButton.setChecked(True)
                                    print("12 3")
            
                                    break
                                yep="<u><span style=\" color:#339900; \n font-weight: bold;\" >"+"\nEntrée : "+"</span></u>"+self.Entree

                                self.ui.Apprentissage.append(yep)
                                self.ui.Apprentissage.append("\n")
                                ent=self.Entree
                                ##########
                                sous_dico=self.Dico_memoire.get(self.Entree,"N0")
                                if sous_dico !="N0":
                                    synonyme_exist=sous_dico.get("synonyme_référent","N0")
                                    if synonyme_exist=="N0":
                                        rien=1
                                    else:
                                        self.Entree=synonyme_exist
                                        print("\nnouvelle self.entree = ",self.Entree)
                                else:
                                    rien=1
                                ##########
                                self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire=self.Get_Entree()
##############################################                            
                    if self.BoutEcrit==1:
                            self.questi = QInputDialog()
                            self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                            text, ok = self.questi.getText(self,"Apprentissage : ", "Donnez la sortie OU e si l'entrée est erronnée, ou syn pour raccorder cette entrée à un synonyme : ")
                            self.Sortie=text
                            print("8")
                            self.Sortie=self.Sortie.lower()
                            if self.Sortie=="":
                                self.fin=1
                                print("1")
                                self.ui.radioButton.setChecked(True)
                                break                            
                            ##########
                            sous_dico=self.Dico_memoire.get(self.Sortie,"N0")
                            if sous_dico !="N0":
                                synonyme_exist=sous_dico.get("synonyme_référent","N0")
                                if synonyme_exist=="N0":
                                    rien=1
                                else:
                                    self.Sortie=synonyme_exist
                                    print("\nnouvelle self.entree = ",self.Sortie)
                            else:
                                rien=1
                            ##########                                                        
                            if self.Sortie=="e":
                                print("9")
                                self.fin=1
                                print("erreur d'entrée")
                                self.ui.radioButton.setChecked(True)
                                break
                            if self.Sortie=="syn":                                
                                self.ques = QInputDialog()
                                tex, ok = self.ques.getText(self,"Apprentissage Synonyme : ", "Donnez le synonyme référent : ")
                                tex=tex.lower()
                                exist_syn_referent=self.Dico_memoire.get(tex,"N0")
                                if exist_syn_referent !="N0":
                                    sous_dico=self.Dico_memoire.get(self.Entree,"N0")
                                    if sous_dico=="N0":
                                        yep="Désolé ! Je ne retrouve pas l'entrée de départ.. Redémarrez"
                                        self.ui.Apprentissage.append(yep)
                                        self.ui.Apprentissage.append("\n")                                    
                                        self.fin=1
                                        print("erreur d'entrée")
                                        self.ui.radioButton.setChecked(True)
                                        break                                     
                                    sous_dico["synonyme_référent"]=tex
                                    print("le synonyme entré")
                                    print(self.Dico_memoire)
                                    self.syno=1
                                                                        
                                else:
                                    yep="Désolé ! Ce synonyme référent n'existe pas dans le dictionnaire."
                                    self.ui.Apprentissage.append(yep)
                                    self.ui.Apprentissage.append("\n")
                                    self.fin=1
                                    print("erreur d'entrée")
                                    self.ui.radioButton.setChecked(True)
                                    break                                                               
                            else:
                                self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire=self.Get_sortie()
##############################################                                 
                    else:
                        self.questi = QInputDialog()
                        self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                        text, ok = self.questi.getText(self,"Apprentissage : ", "Cliquez sur Entrée, et Parlez votre Sortie à l'ordinateur, ou q pour sortir : ")
                        self.Sortie=text
                        self.Sortie=self.Sortie.lower()       
                        if yep=="q":
                            break
                        else:
                            
                            self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")

                            
                            rec("Je vous écoute :")
                            
                            self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")
                            self.Sortie=self.reconn()
                            if self.Sortie=="":
                                self.fin=1
                                print("1")
                                self.ui.radioButton.setChecked(True)
                                break
                            self.Sortie=self.Sortie.lower()
                            ##########
                            sous_dico=self.Dico_memoire.get(self.Sortie,"N0")
                            if sous_dico !="N0":
                                synonyme_exist=sous_dico.get("synonyme_référent","N0")
                                if synonyme_exist=="N0":
                                    rien=1
                                else:
                                    self.Sortie=synonyme_exist
                                    print("\nnouvelle self.entree = ",self.Sortie)
                            else:
                                rien=1
                            ##########
                            yep="<u><span style=\" color:#003333; \n font-weight: bold;\" >"+"\nSortie : "+"</span></u>"+self.Sortie
                            self.ui.Apprentissage.append(yep)
                            self.ui.Apprentissage.append("\n")
                            self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire=self.Get_sortie()                                
                    print("10")
    ####################################################
                    if self.syno==1:
                        self.Sortie="synonyme_référent = "+tex
                        self.syno=0
                        yep="<u><span style=\" color:#003333; \n font-weight: bold;\" >"+"\nSortie : "+"</span></u>"+str(self.Sortie)

#                        yep="Sortie : "+str(self.Sortie)
                        self.ui.Apprentissage.append(yep)
                        self.ui.Apprentissage.append("\n")
                    else:
                        yep="<u><span style=\" color:#003333; \n font-weight: bold;\" >"+"\nSortie : "+"</span></u>"+str(self.Sortie)

#                        yep="Sortie : "+str(self.Sortie)
                        self.ui.Apprentissage.append(yep)
                        self.ui.Apprentissage.append("\n")
                        print("11")
#                    yep="<u><span style=\" color:#006633; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\nVoici le nouveau dictionnaire des items de discussion : "+"</span ></u>"
#                    self.ui.Apprentissage.append(yep)
#                    self.ui.Apprentissage.append("\n")
#                    VisioDico_memoire=str(self.Dico_memoire)
#                    self.ui.Apprentissage.append(VisioDico_memoire)
#                    yep="<u><span style=\" color:#006633; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\nEt voici le nouveau dictionnaire de discussion : "+"</span ></u>"
#                    self.ui.Apprentissage.append("Et voici le nouveau dictionnaire de discussion: ")
#                    self.ui.Apprentissage.append("\n")
#                    VisioDico_discussion=str(self.Dico_discussion)
#                    self.ui.Apprentissage.append(VisioDico_discussion)
                    yep="<u><span style=\" color:#006633; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\nVoici le dictionnaire des items de discussion : "+"</span ></u>"
                    self.ui.Apprentissage.append(yep)
                    ###
                    list_key_Dico_memoire=list(self.Dico_memoire.keys())
                    list_key_Dico_memoire.sort()
                    len_list_key_Dico_memoire=len(list_key_Dico_memoire)
                    list_val_Dico_memoire=[]
                    for po in range(len_list_key_Dico_memoire):
                        val=self.Dico_memoire.get(list_key_Dico_memoire[po],"N0")
                        list_val_Dico_memoire.append(val)
                    for po in range(len_list_key_Dico_memoire):
                        yep="\n"+"<u><span style=\" color:#000066; font=12pt;\" >"+str(list_key_Dico_memoire[po])+"</span></u>"+" : "+str(list_val_Dico_memoire[po])
                        self.ui.Apprentissage.append(yep)           
                    yep="<u><span style=\" color:#006633; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\nVoici, à présent, le dictionnaire des discussions : "+"\n"+"</span ></u>"
                    self.ui.Apprentissage.append(yep)
                    mem=str(self.Dico_discussion)+"\n"
                    self.ui.Apprentissage.append(mem)
                    self.Sauvegarde_Memoire(self.Dico_memoire)
                    self.Sauvegarde_Discussion(self.Dico_discussion)
#############################################
    def interraction(self):

        if self.red==1:
            self.red=0
            print("go rouge")
            self.rouge()
        print("\ninteract1 *************************************************")
        print("self.pass_apprenti = ",self.pass_apprenti)
        print("self.fin = ",self.fin)
        if self.pass_apprenti==1:
            self.stop=1
            self.ui.Interract.setChecked(False)
            print("9")
            self.ui.Apprenti.setChecked(True)
            print("10")            
        ### Fin introduction paramètres discussion ###
        elif self.fin==1:
            self.stop=1
            print("6")
            self.ui.Interract.setChecked(False)
            print("7")
            self.ui.radioButton.setChecked(True)
            print("8")      
        else:
            if self.tre==1:
                ok=1
            else:
                if self.bonjour_dit!=1 and self.twordis==0:
                #######################################
                    if self.visio==1:
                        name=str(self.profile[1])
                        phrase="bonjour"+name
                        engine.say(phrase)
                        engine.runAndWait()
                        self.bonjour_dit=1
                        self.Sortie="bonjour"           
                    else:
                        name=""
                        phrase="bonjour inconnu"
                        engine.say(phrase)
                        engine.runAndWait()
                        self.bonjour_dit=1
                        self.Sortie="bonjour"
                else:
                    rien=1
                ###########################################
                if self.BoutEcrit==1:
                    tipeInter="par écrit."
                else:
                    if self.twordis==1:
                        tipeInter="Entre deux ordinateurs."
                    else:
                        tipeInter="à l'oral : ==> Parlez quand l'écran est ROUGE."
#                yep="\n"+"<u><span style=\" color:#000066; font=12pt;\" >"+str(list_key_Dico_synonyme[wc])+"</span></u>"+" : "+at  ## str(list_val_Dico_synonyme[wc])
                yep="<u><span style=\" color:#0000FF; \n font: 20pt \"MS Shell Dlg 2\";\n font-weight: bold;\" >"+"Interraction : "+tipeInter+"</span></u>"            
                self.ui.Apprentissage.setText(yep)
                self.ui.Apprentissage.append("\n")
                yep="<u><span style=\" color:#9900CC; \n font-weight: bold;\" >"+"\nAI : "+"</span></u>"+self.Sortie
                self.ui.Apprentissage.append(yep)

                self.tre=1
            while True:
                if self.BoutEcrit==1:
                    self.questi = QInputDialog()
                    self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                    text, ok = self.questi.getText(self,"Interraction : ", "Ecrivez : ")
                    self.Entree=text
                    self.Entree=self.Entree.lower()
                    if self.Entree=="":
                        self.fin=1
                        print("1")
                        self.bonjour_dit=0
                        self.ui.radioButton.setChecked(True)
                        break
                    else:
                        yep="<u><span style=\" color:#330000; \n font-weight: bold;\" >"+"\nVous : "+"</span></u>"+self.Entree
                        self.ui.Apprentissage.append(yep)
                        self.ui.Apprentissage.append("\n")
                        ################################
                        print("self.Sortie = ",self.Sortie)
                        sous_dico_sortie=self.Dico_memoire.get(self.Sortie,"N0")
                        print("sous_dico = ",sous_dico_sortie)
                        Coord_Sortie=sous_dico_sortie.get("coord","N0")
                        print("Coord_Sortie = ",Coord_Sortie)
                        #########
                        print("self.Entree = ",self.Entree)
                        sous_dico_entree=self.Dico_memoire.get(self.Entree,"N0")
                        if sous_dico_entree !="N0":
                            print("sous_dico = ",sous_dico_entree)
                            Coord_Entree=sous_dico_entree.get("coord","N0")
                            print("Coord_Sortie = ",Coord_Entree)
                            ####################"
                            couple=Coord_Sortie+Coord_Entree
                            print("couple = ",couple)
                            ###
                            Reponse=self.Dico_discussion.get(couple,"N0")
                            print("Reponse = ",Reponse)
                            if Reponse=="N0":
                                print("youpla")
                                print("self.Sortie = ",self.Sortie)
                                print("self.Entree = ",self.Entree)
                                Reponse=self.Dico_memoire.get(self.Entree,"N0")
                                print("new Reponse = ",Reponse)
                                cle_choisi_Reponse=self.random_pondere(Reponse)
                                print("Retour random : cle_choisi_Reponse = ",cle_choisi_Reponse)
                                self.Sortie=cle_choisi_Reponse
                            else:
                                cle_choisi_Reponse=self.random_pondere(Reponse)
                                self.Sortie=self.Dico_coord_cle.get(cle_choisi_Reponse,"N0")
                                print("retour du dico coord cle = ",self.Sortie )                            
                            yep="<u><span style=\" color:#9900CC; \n font-weight: bold;\" >"+"\nAI : "+"</span></u>"+self.Sortie
                            
                            self.ui.Apprentissage.append(yep)
    #                        self.ui.Apprentissage.append("\n")                        
                            if self.Sortie=="N0":
                                phrase="attention le dictionnaire des discussions renvois vers une clé non existante"
                                engine.say(phrase)
                                engine.runAndWait()
                            else:
                                phrase=self.Sortie
                                engine.say(phrase)
                                engine.runAndWait()
                                #########
                        else:
                            yep="<span style=\" color:#FF3333; \n font-weight: bold;\" >"+"\nJe ne sais pas quoi répondre... Souhaitez vous passer en mode apprentissage ? "+"</span>"
                            self.ui.Apprentissage.append(yep)
                            yepi="je ne sais pas quoi répondre. souhaitez-vous passer en mode apprentissage ?"
                            engine.say(yepi)
                            engine.runAndWait()                            
                            ################
                            if self.BoutEcrit==1:
                                self.questi = QInputDialog()
                                self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                                text, ok = self.questi.getText(self,"Mode Apprentissage : ", "oui (o) ou non (n) ? : ")
                                if text=="o":
                                    print("okkkka")
                                    self.Raccord=self.Entree
                                    print("self.Raccord 0 = ",self.Raccord)
                                    self.pass_apprenti=1
                                    self.ui.Interract.setChecked(False)
                                    self.ui.Apprenti.setChecked(True)
                                    self.pass_apprenti=1                                    
                                    print("11")
                                    self.bonjour_dit=0
                                    break
                                else:
                                    print("Pourquoiiaaaaaaa")
                                    ok=1
                            else:
                                self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")

                                
                                rec("oui ou non je vous écoute :")
                                
                                self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")                                
                                self.repo=self.reconn()
                                if self.repo=="oui":
                                    print("okkkk")
                                    self.Raccord=self.Entree
                                    self.pass_apprenti=1
                                    self.ui.Interract.setChecked(False)
                                    self.ui.Apprenti.setChecked(True)
                                    self.pass_apprenti=1
                                    print("12")
                                    self.bonjour_dit=0
                                    break
                                else:
                                    ok=1
                            ################                            
                            print("nooo")
                            self.Dico_Sort={}
                            self.fin=0
                            self.continu=1
                            self.interraction()
                else:  ########"  *******************************************************************
                    if self.VocalLent==1:
                        self.questi = QInputDialog()
                        self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                        text, ok = self.questi.getText(self,"interraction : ", "Cliquez sur Entrée, et Parlez votre Entrée à l'ordinateur, ou q pour sortir : ")
                        self.Entree=text
                        self.Entree=self.Entree.lower()       
                        if text=="q":
                            self.ui.Interract.setChecked(False)
                            print("Changements de bouton")
                            self.ui.radioButton.setChecked(True)
                            self.fin=1
                            self.stop=1
                            break
                       
                        else:
                            self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")
    
                            rec("Je vous écoute :")
                    else: 
                        ##################################
                        if self.twordis==1:
                            if self.ordre==1:
                                print("\nself.ordre=1 :      Go serveur ! \n\n")
                                self.ServeurParle()
                                print("120")
                                self.exserveur=1

                            elif self.ordre==2:
                                print("\nself.ordre=2 :      Go Client envoie jecoute et enregistre. ! \n\n")
                                message="jecoute"
                                retour=self.Client(message)
                                self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")    
                                rec("")
                            else:
                                self.ui.Interract.setChecked(False)
                                print("Changements de bouton")
                                self.ui.radioButton.setChecked(True)
                                self.fin=1
                                self.stop=1
                                break
                        ##################################
                        else:
                            self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")    
                            rec("")                        
                        
                    if self.exserveur==1:
                        self.exserveur=0
                        rien=1
                    else:
                        self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")
                        print("\nEnvoie en reconn 1214..")
                        self.Entree=self.reconn()
                        print("ok, revenu")
                        try:                       
                            self.Entree=self.Entree.lower()
                        except AttributeError:
                            print("Changements de bouton 12")
                            self.fin=1
                            self.stop=1
                            self.ui.Ecrit.setChecked(True)
                            print("12 2")
                            self.ui.radioButton.setChecked(True)
                            print("12 3")
    
                            break
                        
                        if self.Entree=="stop":
                            print("stoppi !!!!")
                            self.fin=1
                            print("self.fin =",self.fin)
                            print("1")
                            self.ui.radioButton.setChecked(True) 
                            self.stop=1
                            self.continu=0
                        if self.Entree=="au revoir":
                            print("stoppi !!!!")
                            self.fin=1
                            print("self.fin =",self.fin)
                            print("1")
                            self.ui.radioButton.setChecked(True) 
                            self.stop=1
                            self.continu=0
                        elif self.Entree=="météo":
                            self.fin=1
                            print("self.fin =",self.fin)
                            print("1")
                            self.ui.radioButton.setChecked(True) 
                            self.stop=1
                            self.continu=0
                            webbrowser.open('https://meteofrance.com')
                        elif self.Entree=="agenda":
                            self.fin=1
                            print("self.fin =",self.fin)
                            print("1")
                            self.ui.radioButton.setChecked(True) 
                            self.stop=1
                            self.continu=0
                            webbrowser.open('https://calendar.google.com/calendar/u/0/r?tab=wc')
                        elif self.Entree=="ouvre mes mails":
                            self.fin=1
                            print("self.fin =",self.fin)
                            print("1")
                            self.ui.radioButton.setChecked(True) 
                            self.stop=1
                            self.continu=0
                            webbrowser.open('https://mail.yahoo.com/d/folders/1?.intl=fr&.lang=fr-FR')
                        elif self.Entree=="google":
                            print("google !!")
                            self.fin=1
                            print("self.fin =",self.fin)
                            print("1")
                            self.ui.radioButton.setChecked(True) 
                            self.stop=1
                            self.continu=0
                            webbrowser.open('https://www.google.com')
                        elif self.Entree=="youtube":
                            print("youtube")
                            self.fin=1
                            print("self.fin =",self.fin)
                            print("1")
                            self.ui.radioButton.setChecked(True) 
                            self.stop=1
                            self.continu=0
                            webbrowser.open('https://www.youtube.com/?hl=fr&gl=FR')
                        
                        
                        if self.Entree=="":
                            self.fin=1
                            print("1")
                            self.bonjour_dit=0
                            self.ui.Apprenti.setChecked(False)
                            print("Changements de bouton")
                            self.stop=1
                            self.ui.radioButton.setChecked(True)
                            break
                        else:
                            yep="<u><span style=\" color:#330000; \n font-weight: bold;\" >"+"\nVous : "+"</span></u>"+self.Entree
                            self.ui.Apprentissage.append(yep)
                            self.ui.Apprentissage.append("\n")
                            ################################
                            print("self.Sortie = ",self.Sortie)
                            sous_dico_sortie=self.Dico_memoire.get(self.Sortie,"N0")
                            print("sous_dico = ",sous_dico_sortie)
                            Coord_Sortie=sous_dico_sortie.get("coord","N0")
                            print("Coord_Sortie = ",Coord_Sortie)
                            #########
                            print("self.Entree = ",self.Entree)
                            sous_dico_entree=self.Dico_memoire.get(self.Entree,"N0")
                            if sous_dico_entree !="N0":
                                print("sous_dico = ",sous_dico_entree)
                                Coord_Entree=sous_dico_entree.get("coord","N0")
                                print("Coord_Sortie = ",Coord_Entree)
                                ####################"
                                couple=Coord_Sortie+Coord_Entree
                                print("couple = ",couple)
                                ###
                                Reponse=self.Dico_discussion.get(couple,"N0")
                                print("Reponse = ",Reponse)
                                if Reponse=="N0":
                                    print("youpla")
                                    print("self.Sortie = ",self.Sortie)
                                    print("self.Entree = ",self.Entree)
                                    Reponse=self.Dico_memoire.get(self.Entree,"N0")
                                    print("new Reponse = ",Reponse)
                                    cle_choisi_Reponse=self.random_pondere(Reponse)
                                    print("Retour random : cle_choisi_Reponse = ",cle_choisi_Reponse)
                                    self.Sortie=cle_choisi_Reponse
                                else:
                                    cle_choisi_Reponse=self.random_pondere(Reponse)
                                    self.Sortie=self.Dico_coord_cle.get(cle_choisi_Reponse,"N0")
                                    print("retour du dico coord cle = ",self.Sortie )                            
                                yep="<u><span style=\" color:#9900CC; \n font-weight: bold;\" >"+"\nAI : "+"</span></u>"+self.Sortie
                                
                                self.ui.Apprentissage.append(yep)
        #                        self.ui.Apprentissage.append("\n")                        
                                if self.Sortie=="N0":
                                    phrase="attention le dictionnaire des discussions renvois vers une clé non existante"
                                    engine.say(phrase)
                                    engine.runAndWait()
                                else:
                                    if self.twordis==1:
                                        message="change"
                                        retour=self.Client(message)
                                    else:
                                        phrase=self.Sortie
                                        engine.say(phrase)
                                        engine.runAndWait()
                                    #########
                            else:
                                yep="<span style=\" color:#FF3333; \n font-weight: bold;\" >"+"\nJe ne sais pas quoi répondre... Souhaitez vous passer en mode apprentissage ? "+"</span>"
                                self.ui.Apprentissage.append(yep)
                                yepi="je ne sais pas quoi répondre. souhaitez-vous passer en mode apprentissage ?"
                                engine.say(yepi)
                                engine.runAndWait()                            
                                ################
                                if self.BoutEcrit==1:
                                    self.questi = QInputDialog()
                                    self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                                    text, ok = self.questi.getText(self,"Mode Apprentissage : ", "oui (o) ou non (n) ? : ")
                                    if text=="o":
                                        print("okkkka")
                                        self.Raccord=self.Entree
                                        print("self.Raccord 0 = ",self.Raccord)
                                        self.pass_apprenti=1
                                        self.ui.Interract.setChecked(False)
                                        self.ui.Apprenti.setChecked(True)
                                        self.pass_apprenti=1                                    
                                        print("11")
                                        self.bonjour_dit=0
                                        break
                                    else:
                                        print("Pourquoiiaaaaaaa")
                                        ok=1
                                else:
                                    self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")
    
                                    
                                    rec("oui ou non je vous écoute :")
                                    
    #                                    self.ui.Mic_Ac.setChecked(False)
                                    self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")                                
                                    self.repo=self.reconn()
                                    if self.repo=="oui":
                                        print("okkkk")
                                        self.Raccord=self.Entree
                                        self.pass_apprenti=1
                                        self.ui.Interract.setChecked(False)
                                        self.ui.Apprenti.setChecked(True)
                                        self.pass_apprenti=1
                                        print("12")
                                        self.bonjour_dit=0
                                        break
                                    else:
                                        self.fin=1
                                        print("1")
                                        self.bonjour_dit=0
                                        self.ui.radioButton.setChecked(True)
                                        self.ui.Ecrit.setChecked(True)
                                        break
                                ################                            
                                print("nooo")
                                self.Dico_Sort={}
                                self.fin=0
                                self.continu=1
                                self.interraction()                    
############################################""
    def rouge(self):
        print("\Rouge !!!!!!")
        self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ui.Mic_Ac.setChecked(True)
        self.ui.groupBox_3.setVisible(True)    
        self.ui.Mic_Ferm.setChecked(False)
        self.ui.Mic_Ac.setChecked(True)
        
        rec("Je vous écoute :")
        
#                        self.ui.Mic_Ac.setChecked(False)
        self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.Mic_Ferm.setChecked(True)
        self.Entree=self.reconn()
        print("ok, revenu")
        self.Entree=self.Entree.lower()
    
        if self.Entree=="":
            self.fin=1
            print("1")
            self.bonjour_dit=0
            self.ui.radioButton.setChecked(True)
#            break
        else:
            yep="<u><span style=\" color:#330000; \n font-weight: bold;\" >"+"\nVous : "+"</span></u>"+self.Entree
            self.ui.Apprentissage.append(yep)
            self.ui.Apprentissage.append("\n")
            ################################
            print("self.Sortie = ",self.Sortie)
            sous_dico_sortie=self.Dico_memoire.get(self.Sortie,"N0")
            print("sous_dico = ",sous_dico_sortie)
            Coord_Sortie=sous_dico_sortie.get("coord","N0")
            print("Coord_Sortie = ",Coord_Sortie)
            #########
            print("self.Entree = ",self.Entree)
            sous_dico_entree=self.Dico_memoire.get(self.Entree,"N0")
            if sous_dico_entree !="N0":
                print("sous_dico = ",sous_dico_entree)
                Coord_Entree=sous_dico_entree.get("coord","N0")
                print("Coord_Sortie = ",Coord_Entree)
                ####################"
                couple=Coord_Sortie+Coord_Entree
                print("couple = ",couple)
                ###
                Reponse=self.Dico_discussion.get(couple,"N0")
                print("Reponse = ",Reponse)
                if Reponse=="N0":
                    print("youpla")
                    print("self.Sortie = ",self.Sortie)
                    print("self.Entree = ",self.Entree)
                    Reponse=self.Dico_memoire.get(self.Entree,"N0")
                    print("new Reponse = ",Reponse)
                    cle_choisi_Reponse=self.random_pondere(Reponse)
                    print("Retour random : cle_choisi_Reponse = ",cle_choisi_Reponse)
                    self.Sortie=cle_choisi_Reponse
                else:
                    cle_choisi_Reponse=self.random_pondere(Reponse)
                    self.Sortie=self.Dico_coord_cle.get(cle_choisi_Reponse,"N0")
                    print("retour du dico coord cle = ",self.Sortie )                            
                yep="<u><span style=\" color:#9900CC; \n font-weight: bold;\" >"+"\nAI : "+"</span></u>"+self.Sortie
                self.ui.Apprentissage.append(yep)
#                        self.ui.Apprentissage.append("\n")                        
                if self.Sortie=="N0":
                    phrase="attention le dictionnaire des discussions renvois vers une clé non existante"
                    engine.say(phrase)
                    engine.runAndWait()
                else:
                    phrase=self.Sortie
                    engine.say(phrase)
                    engine.runAndWait()
                    #########
            else:
                yep="<span style=\" color:#FF3333; \n font-weight: bold;\" >"+"\nJe ne sais pas quoi répondre... Souhaitez vous passer en mode apprentissage ? "+"</span>"
                self.ui.Apprentissage.append(yep)
                yepi="je ne sais pas quoi répondre. souhaitez-vous passer en mode apprentissage ?"
                engine.say(yepi)
                engine.runAndWait()                            
                ################
                if self.BoutEcrit==1:
                    self.questi = QInputDialog()
                    self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                    text, ok = self.questi.getText(self,"Mode Apprentissage : ", "oui (o) ou non (n) ? : ")
                    if text=="o":
                        print("okkkka")
                        self.Raccord=self.Entree
                        print("self.Raccord 0 = ",self.Raccord)
                        self.pass_apprenti=1
                        self.ui.Interract.setChecked(False)
                        self.ui.Apprenti.setChecked(True)
                        self.pass_apprenti=1                                    
                        print("11")
                        self.bonjour_dit=0
#                        break
                    else:
                        print("Pourquoiiaaaaaaa")
                        ok=1
                else:
                    self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.ui.Mic_Ac.setChecked(True)
#                                    self.ui.groupBox_3.setVisible(True)    
#                                    self.ui.Mic_Ferm.setChecked(False)
                    
                    rec("oui ou non je vous écoute :")
                    
#                                    self.ui.Mic_Ac.setChecked(False)
                    self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")                                
                    self.ui.Mic_Ferm.setChecked(True)
                    self.repo=self.reconn()
                    if self.repo=="oui":
                        print("okkkk")
                        self.Raccord=self.Entree
                        self.pass_apprenti=1
                        self.ui.Interract.setChecked(False)
                        self.ui.Apprenti.setChecked(True)
                        self.pass_apprenti=1
                        print("12")
                        self.bonjour_dit=0
#                        break
                    else:
                        ok=1
                ################                            
                print("nooo")
                self.Dico_Sort={}
                self.fin=0
                self.continu=1
                self.interraction()                                 
###########################################"
    def go(self):
        yep="\nMicro activé.. Parlez !\n"
        self.ui.Apprentissage.append(yep)
#########################################"
    def efface_cle(self):
        print("youpi : Dico_memoire = ",self.Dico_memoire)
        print("youpi : Dico_discussion = ",self.Dico_discussion)
        yep="\nVoulez vous donner la clé (cl) ou sa coordonnée (co) pour l'effacement ? : "
        self.ui.Apprentissage.append(yep)      
        self.questi = QInputDialog()
        cle, ok = self.questi.getText(self,"clé ou coord","cl ou co : ")
        cle=cle.lower()
        if cle=="co":
            yep="\nDonnez la coordonnée pour l'effacement : "
            self.ui.Apprentissage.append(yep)      
            self.questi = QInputDialog()
            coordo, ok = self.questi.getText(self,"...","coordonnée : ")

            self.Dico_coord_cle={}
            self.List_Cle_Dico_memoire=list(self.Dico_memoire.keys())
#            print("\nList_Cle_Dico_memoire = ",self.List_Cle_Dico_memoire)
            Long_List_Cle_Dico_memoire=len(self.List_Cle_Dico_memoire)
            for i in range(Long_List_Cle_Dico_memoire):
                sous_dico=self.Dico_memoire.get(self.List_Cle_Dico_memoire[i],"N0")
                coord=sous_dico.get("coord","N0")
                self.Dico_coord_cle[coord]=self.List_Cle_Dico_memoire[i]
#            print("\nDico_coord_cle = ",self.Dico_coord_cle)           
            self.cle_effac=self.Dico_coord_cle.get(coordo,"N0")
            if self.cle_effac=="N0":
                yep="\nDésolé, cette coordonnée ne semble pas exister dans le dictionnaire.\n"
                self.ui.Apprentissage.append(yep)                  
            else:
                self.cle_donn=1
                self.effac_cle_donn()
            
            
        elif cle=="cl":
            self.cle_donn=0
            self.effac_cle_donn()
            
    def effac_cle_donn(self):
        if self.cle_donn==1:
            self.cle_donn=0
            cle=self.cle_effac
        else:
            yep="\nQuelle clé voulez vous effacer ? (ex : salut) ou stop pour sortir : "
            self.ui.Apprentissage.append(yep)    
            self.questi = QInputDialog()
            cle, ok = self.questi.getText(self,"...","clé ou s : ")
            cle=cle.lower()
        if cle=="s":
            self.Sauvegarde_Memoire(self.Dico_memoire)
            self.Sauvegarde_Discussion(self.Dico_discussion) 
            yep="\nOk, A+.."
            self.ui.Apprentissage.append(yep)  
        else:
            repi = self.Dico_memoire.get(cle,"N0")
            if repi!= "N0":
                yep="\nVoulez vous vraiment effacer cette clé : "+cle+" ? : "
                self.ui.Apprentissage.append(yep)
                self.questi = QInputDialog()
                yepi, ok = self.questi.getText(self,"...","o/n : ")
                yepi=yepi.lower()
                if yepi!="o" and yepi!="n":
                    yep="\nDésolé, je n'ai pas compris votre réponse (o/n)"
                    self.ui.Apprentissage.append(yep)
                elif yepi=="n":
                    yep="\nCompris ; Nous n'effaçons pas cette clé."
                    self.ui.Apprentissage.append(yep)
                else:
                    yep="\nNous effaçons cette clé..."
                    self.ui.Apprentissage.append(yep)
                    coordon_cle=repi.get("coord","N0")
                    if coordon_cle=="N0":
                        yep="\n ** Désolé, cette clé semble ne pas avoir de coordonnée ..? **"
                        self.ui.Apprentissage.append(yep)
                    else:
                        self.Dico_memoire.pop(cle)
                        self.List_Cle_Dico_memoire=list(self.Dico_memoire.keys())
                        print("list_cle_Dico_memoire=",self.List_Cle_Dico_memoire)
                        val_Dico_memoire=list(self.Dico_memoire.values())
                        len_val_Dico_memoire=len(val_Dico_memoire)
                        coordonnees=[]
                        for y in range(len_val_Dico_memoire):
                            item=val_Dico_memoire[y]
                            item_key=list(item.keys())
                            item_val=list(item.values())
                            len_item_val=len(item_val)
                            for r in range(len_item_val):
                                if item_key[r]=="coord":
                                    coordonnees.append(item_val[r])
                        print("\nVoici les coordonnées : ",coordonnees)
                        list_cle_Dico_discussion=list(self.Dico_discussion.keys())
                        list_val_Dico_discussion=list(self.Dico_discussion.values())
                        long_list_cle_Dico_discussion=len(list_cle_Dico_discussion)
                        for a in range(long_list_cle_Dico_discussion):
                            cle_isole=list_cle_Dico_discussion[a]
                            val_isole=list_val_Dico_discussion[a]
                            print("\ncle_isole [",a,"]=",cle_isole)
                            deb_cle_isole=cle_isole[:2]
                            print("deb_cle_isole [",a,"]= ",deb_cle_isole)
                            fin_cle_isole=cle_isole[-2:]
                            print("fin_cle_isole [",a,"]= ",fin_cle_isole)
                            print("val_isole [",a,"]= ",val_isole)
                            cles_val_isole=list(val_isole.keys())
                            len_cles_val_isole=len(cles_val_isole)
                            for qs in range(len_cles_val_isole):
                                cle_val_isole=cles_val_isole[qs]
                                print("clé_val_isole [",a,"]= ",cle_val_isole)
                                if cle_val_isole==coordon_cle:
                                    print("ici il faut effacer fin_cle_isole = ",fin_cle_isole)
                                    len_coordonnees=len(coordonnees)
                                    print("len_coordonnees =",len_coordonnees)
                                    for sd in range(len_coordonnees):
                                        print("sd =",sd)
                                        wx=coordonnees[sd]
                                        print("coordonnees[sd] = ",wx)
                                        if coordonnees[sd]==fin_cle_isole:
                                            print("on a coordonnees[sd]==fin_cle_isole !!" )
                                            cle_fin_cle_isole=self.List_Cle_Dico_memoire[sd]
                                            print("la clé à cibler est : ",cle_fin_cle_isole)                                            
                                            sous_Dico_memoire_cle_cible=self.Dico_memoire.get(cle_fin_cle_isole,"N0")
                                            print("sous_Dico_memoire_cle_cible avant : ",sous_Dico_memoire_cle_cible)
                                            sous_Dico_memoire_cle_cible.pop(cle)
                                            print("sous_Dico_memoire_cle_cible après : ",sous_Dico_memoire_cle_cible)
                                            input("pause")
                            if fin_cle_isole==coordon_cle:
                                len_coordonnees=len(coordonnees)
                                for k in range(len_coordonnees):
                                    if coordonnees[k]==deb_cle_isole:
                                        cle_inter=self.List_Cle_Dico_memoire[k]
                                        print("\nVoici le mot que je dois effacer car il a pour pong : salut : ",cle_inter)
                                        val_cle_inter=self.Dico_memoire.get(cle_inter,"N0")
                                        print("\nVoici la valeur de bonjour : ",val_cle_inter)
                                        val_cle_inter.pop(cle)
                            if deb_cle_isole==coordon_cle or fin_cle_isole==coordon_cle:
                                self.Dico_discussion.pop(cle_isole)
                                print("----> J'efface cette cle ",cle_isole," de la discussion" )
                                print("\n Voici le Dico_memoire :",self.Dico_memoire)
                                print("\n et voici le Dico_discussion :",self.Dico_discussion)
                        list_values_Dico_discussion=list(self.Dico_discussion.values())
                        print("\nCeci est la liste des valeurs 51 : ",list_values_Dico_discussion)
                        list_cle_Dico_discussion=list(self.Dico_discussion.keys())
                        long_list_values_Dico_discussion=len(list_values_Dico_discussion)
                        print("\nVoici la coordon_cle = ",coordon_cle)
                        for a in range(long_list_values_Dico_discussion):
                            val_isole=list_values_Dico_discussion[a]
                            print("\nYEPPA val_isole [",a,"]=",val_isole)
                            list_cle_val_isol=list(val_isole.keys())
                            print("\nCeci est la liste des clé 59 : ",list_cle_val_isol)
                            print("a=",a)
                            print("Voici la liste cle_val_isol=list(val_isole.keys()) =",list_cle_val_isol)
                            long_list_cle_val_isol=len(list_cle_val_isol)
                            for c in range(long_list_cle_val_isol):
                                if list_cle_val_isol[c]==coordon_cle:
                                    print("coucou")
                                    doublet=list_cle_Dico_discussion[a]
                                    print("----> ok, jefface la discussion 69 : {'",doublet,"':",val_isole )
                                    print("..a=",a)
                                    print("..c=",c)
                                    print("Voici la liste cle_val_isol=list(val_isole.keys()) =",list_cle_val_isol)
                                    val_isole.pop(coordon_cle)
                                    long_val_isole=len(val_isole)
                                    if long_val_isole==0:
                                        print("**** Yadza ********")
                                        self.Dico_discussion.pop(doublet)
                                    yep="\n Voici le nouveau Dico_memoire :"+str(self.Dico_memoire)
                                    self.ui.Apprentissage.append(yep)
                                    yep="\n et voici le nouveau Dico_discussion :"+str(self.Dico_discussion)
                                    self.ui.Apprentissage.append(yep)
                                    self.Sauvegarde_Memoire(self.Dico_memoire)
                                    self.Sauvegarde_Discussion(self.Dico_discussion)                  
            else:
                yep="\nDésolé, cette clé n'existe pas dans le dictionnaire..."
                self.ui.Apprentissage.append(yep)
#########################################"
    def memoire(self):
        if self.fin==1:
            self.stop=1
        else:            
            self.ui.Ecrit.setChecked(True)
            yep="<u><span style=\" color:#000000; \n font-weight: bold; \n background-color: rgb(255, 185, 254); \n font: 20pt \"MS Shell Dlg 2\";\" >"+"\nGestion du dictionnaire : Mode écrit uniquement.\n"+"</span ></u>"
            self.ui.Apprentissage.setText(yep)
            yep="<u><span style=\" color:#660066; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\nVoici le dictionnaire des items de discussion : "+"</span ></u>"
            self.ui.Apprentissage.append(yep)
            ###
            list_key_Dico_memoire=list(self.Dico_memoire.keys())
            list_key_Dico_memoire.sort()
            len_list_key_Dico_memoire=len(list_key_Dico_memoire)
            list_val_Dico_memoire=[]
            for po in range(len_list_key_Dico_memoire):
                val=self.Dico_memoire.get(list_key_Dico_memoire[po],"N0")
                list_val_Dico_memoire.append(val)
            for po in range(len_list_key_Dico_memoire):
                yep="\n"+"<u><span style=\" color:#000066; font=12pt;\" >"+str(list_key_Dico_memoire[po])+"</span></u>"+" : "+str(list_val_Dico_memoire[po])
                self.ui.Apprentissage.append(yep)           
            yep="<u><span style=\" color:#660066; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\nVoici, à présent, le dictionnaire des discussions : "+"\n"+"</span ></u>"
            self.ui.Apprentissage.append(yep)
            mem=str(self.Dico_discussion)+"\n"
            self.ui.Apprentissage.append(mem)
            while True:
                yep="<span style=\" color:#660033; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\nSouhaitez vous rechercher une donnée ? (r), effacer une donnée ? (e), voir les synonymes ? (syn) ou sortir (s) : "+"\n"+"</span >"
                self.ui.Apprentissage.append(yep)                
                self.questi = QInputDialog()
                texto, ok = self.questi.getText(self,"...","r / e / syn / s : ")
                texto=texto.lower()
                if texto !="r" and texto !="e" and texto !="s" and texto !="syn":
                    yep="<u><span style=\" color:#660033; \n font-weight: bold; \n  font: 14pt \"MS Shell Dlg 2\";\" >"+"\ndésolé, je n'ai pas compris votre réponse ..."+"\n"+"</span ></u>"
                    self.ui.Apprentissage.append(yep)                    
                if texto=="syn":
                    self.Dico_synonyme={}
                    list_key_Dico_memoire=list(self.Dico_memoire.keys())
                    len_list_key_Dico_memoire=len(list_key_Dico_memoire)
                    for df in range(len_list_key_Dico_memoire):
                        sous_dico_key=self.Dico_memoire.get(list_key_Dico_memoire[df])
                        syn_ref_exist=sous_dico_key.get("synonyme_référent","N0")
                        if syn_ref_exist=="N0":
                            rien=1
                        else:
                            exist_syn_ref_exist=self.Dico_synonyme.get(syn_ref_exist,"N0")
                            if exist_syn_ref_exist=="N0":
                                self.Dico_synonyme[syn_ref_exist]=[list_key_Dico_memoire[df]]
                            else:
                                exist_syn_ref_exist.append(list_key_Dico_memoire[df])
                                self.Dico_synonyme[syn_ref_exist]=exist_syn_ref_exist
                    yep="<u><span style=\" color:#006633; \n font-weight: bold; \n font: 20pt \"MS Shell Dlg 2\";\" >"+"\nVoici le dictionnaire des synonymes : "+"</span ></u>"
                    self.ui.Apprentissage.append(yep)
                    yep="("+"<u><span style=\" color:#000066; \" >"+"synonyme référent :"+"</span></u>"+" synonyme )\n\n"
                    self.ui.Apprentissage.append(yep)
                    yep="<i><span>"+"--> Par ordre alphabétique des synonymes référents."+"</span></i>"
                    self.ui.Apprentissage.append(yep)
                    yep="\n"
                    self.ui.Apprentissage.append(yep)
                    list_key_Dico_synonyme=list(self.Dico_synonyme.keys())
                    list_key_Dico_synonyme.sort()
                    len_list_key_Dico_synonyme=len(list_key_Dico_synonyme)
                    list_val_Dico_synonyme=[]
                    for po in range(len_list_key_Dico_synonyme):
                        val=self.Dico_synonyme.get(list_key_Dico_synonyme[po],"N0")
                        list_val_Dico_synonyme.append(val)
#                    list_val_Dico_synonyme=list(self.Dico_synonyme.values())
                    
                    print("\n list_key_Dico_synonyme = ",list_key_Dico_synonyme)
                    for wc in range(len_list_key_Dico_synonyme):
                        print("\n wc = ",wc)
                        at=str(list_val_Dico_synonyme[wc])
                        print("at = ",at)
                        at=at.replace("[","")
                        print("at = ",at)
                        at=at.replace("]","")
                        print("at = ",at)
                        for a in range(50):
                            at=at.replace("'","")
                        print("\nnew_at = ",at)
                        yep="\n"+"<u><span style=\" color:#000066; font=12pt;\" >"+str(list_key_Dico_synonyme[wc])+"</span></u>"+" : "+at  ## str(list_val_Dico_synonyme[wc])
                        self.ui.Apprentissage.append(yep)
                    yep="\n"
                    self.ui.Apprentissage.append(yep)
                if texto=="r":
                    yep="\nVous recherchez une clé(c) (ex: bonjour) ou une discussion(d) (ex: A1D1) ?"+"\n"
                    self.ui.Apprentissage.append(yep)                    
                    self.questi = QInputDialog()
                    text, ok = self.questi.getText(self,"c ou d ?","...")
                    text=text.lower()
                    if text=="c":
                        yep="\nQuelle clé recherchez-vous ?"+"\n"
                        self.ui.Apprentissage.append(yep)                        
                        self.questi = QInputDialog()
                        text, ok = self.questi.getText(self,"clé ?","... ")
                        text=text.lower()
                        exist_cle=self.Dico_memoire.get(text,"N0")
                        if exist_cle=="N0":
                            yep="Désolé, cette clé n'existe pas en mémoire.."+"\n"
                            self.ui.Apprentissage.append(yep)
                        else:
                            yep="Voici le contenu de cette clé : "+text+" : "+str(exist_cle)+"\n"
                            self.ui.Apprentissage.append(yep)
                    elif text=="d":
                        yep="\nQuelle discussion (ex: A1D1) recherchez-vous ?"+"\n"
                        self.ui.Apprentissage.append(yep)
                        self.questi = QInputDialog()
                        text, ok = self.questi.getText(self,"Discussion ?","... ")
                        text=text.upper()
                        exist_cle=self.Dico_discussion.get(text,"N0")
                        if exist_cle=="N0":
                            yep="Désolé, cette discussion n'existe pas en mémoire.."+"\n"
                            self.ui.Apprentissage.append(yep)
                        else:
                            yep="Voici le contenu de cette discussion : "+text+" : "+str(exist_cle)+"\n"
                            self.ui.Apprentissage.append(yep)
                if texto=="e":
                    self.efface_cle()                   
                elif texto=="s":
                    self.Sauvegarde_Memoire(self.Dico_memoire)
                    self.Sauvegarde_Discussion(self.Dico_discussion)
                    yep="<i><span style=\" color:#FF0000; \n font-weight: bold; \n  font: 12pt \"MS Shell Dlg 2\";\" >"+"\n \nOk, A+ "+"\n"+"</span ></i>"                    
                    self.ui.Apprentissage.append(yep)
                    self.fin=1
                    self.ui.radioButton.setChecked(True) 
                    self.stop=1
                    break
###########################################
    def synonyme_list(self,quest):
        dico_synonyme={}
        list_rep=quest.keys()
        list_rep=list(list_rep)
        long_list_rep=len(list_rep)
        list_val=quest.values()
        list_val=list(list_val)
        long_list_val=len(list_val)
        for er in range(long_list_val):
            self.dico_val=list_val[er]
            et=len(self.dico_val)
            if et==1:
                cle_dico_val=self.dico_val.keys()
                cle_dico_valo=list(cle_dico_val)
                clee=str(cle_dico_valo[0])
                if clee=='synonyme_ref':
                    syn_ref=self.dico_val.values()
                    list_syn_ref=list(syn_ref)
                    synonyme=str(list_syn_ref[0])
                    entr=list_rep[er]
                    syn_exist=dico_synonyme.get(synonyme,"N0")
                    if syn_exist=="N0":
                        dico_synonyme[synonyme]=entr
                    else:
                        syn_exist=str(syn_exist)
                        new_syn=syn_exist+", "+entr
                        dico_synonyme[synonyme]=new_syn
        return dico_synonyme        
###########################################
    def random_pondere(self,quest):
        new_list=[]
        result=""
        sous_dico=quest
        list_rep=sous_dico.keys()
        list_rep=list(list_rep)
        print("list_rep = ",list_rep)
        long_list_rep=len(list_rep)
        print("long_list_rep = ",long_list_rep)
        synony=0
        for er in range(long_list_rep):
            print("er=",er)
            qd=list_rep[er]
            print("list_rep[er] = ",qd)
            if list_rep[er]=="synonyme_référent":
                synony=1
                print("on met synony=1")
                valeur = er
        if synony==1:
            self.Entree=sous_dico.get("synonyme_référent","N0")
            print("self.Entree=sous_dico.get('synonyme_référent','N0') = ",self.Entree)
            self.quest=self.Dico_memoire.get(self.Entree,"N0")
            print("self.quest=self.Dico_memoire.get(self.Entree,'N0') = ",self.quest)
    #        print("quest = ",quest)
            if self.quest =="N0":
                yep="<span style=\" color:#FF3333; \n font-weight: bold;\" >"+"\nJe ne sais pas quoi répondre... Souhaitez vous passer en mode apprentissage ? "+"</span>"
                self.ui.Apprentissage.append(yep)
                yepi="je ne sais pas quoi répondre passez en mode apprentissage"
                engine.say(yepi)
                engine.runAndWait()
                self.Dico_Sort={}                
            else:
                y=self.random_pondere(self.quest)
                return y
        else:
            print("on est passé par bonjour")
            list_val=sous_dico.values()
            list_val=list(list_val)
            long_list=len(list_rep)
            for i in range(long_list):
                x=list_val[i]
                try:
                    for boucle in range(x):
                        z=str(list_rep[i])
                        result=z  ## +","
                        new_list.append(result)
                except TypeError:
                    rien=1
            list_sous_dico=list(sous_dico)
            longueur=len(new_list)   
            if longueur !=0:
                x =random.randint(1,longueur)
                y=new_list[x-1]
                print("y = ",y)
                return y
            else:
                yep="<span style=\" color:#FF3333; \n font-weight: bold;\" >"+"\nJe ne sais pas quoi répondre... Souhaitez vous passer en mode apprentissage ? "+"</span>"
                self.ui.Apprentissage.append(yep)
                yepi="je ne sais pas quoi répondre. souhaitez-vous passer en mode apprentissage ?"
                engine.say(yepi)
                engine.runAndWait()                
                ################
                if self.BoutEcrit==1:
                    self.questi = QInputDialog()
                    self.questi.setStyleSheet("background-color: rgb(255, 170, 0);")
                    text, ok = self.questi.getText(self,"Mode Apprentissage : ", "oui (o) ou non (n) ? : ")
                    if text=="o":
                        self.apprentissage()
                    else:
                        ok=1
                else:
                    self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 0, 0);")
#                    self.ui.Mic_Ac.setChecked(True)
#                    self.ui.groupBox_3.setVisible(True)    
#                    self.ui.Mic_Ferm.setChecked(False)
                    
                    rec("oui ou non je vous écoute :")
                    
#                    self.ui.Mic_Ac.setChecked(False)
                    self.ui.Apprentissage.setStyleSheet("background-color: rgb(255, 255, 255);")
#                    self.ui.Mic_Ferm.setChecked(True)
                    self.repo=self.reconn()
                    if self.repo=="oui":
                        print("okkkk")
                        self.fin=1
                        print("self.fin =",self.fin)
                        print("1")
                        self.stop=1
                        self.continu=0
                        self.ui.Apprenti.setChecked(True)
                    else:
                        ok=1
####################################################"
    def Trouver_new_coord(self):
        dico_tabo={}
        list_key_Dico_memoire=list(self.Dico_memoire.keys())
        long_list_key_Dico_memoire=len(list_key_Dico_memoire)
        print("long_list_key_Dico_memoire =",long_list_key_Dico_memoire)
        list_coord_cle_Dico_memoire=[]
        print("dico_tabo_avant =",dico_tabo)
        for az in range(long_list_key_Dico_memoire):
            print("az = ",az)
            val_cle_Dico_memoire=self.Dico_memoire.get(list_key_Dico_memoire[az])
            coordonne=val_cle_Dico_memoire.get("coord")
            list_coord_cle_Dico_memoire.append(coordonne)
            dico_tabo[list_key_Dico_memoire[az]]=coordonne
        print("dico_tabo =",dico_tabo)
        lista=list(dico_tabo.values())
        print("lista = ",lista)
        list_lettre=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        long_list_lettre=len(list_lettre)
        long_lista=len(lista)
        dernier=lista[long_lista-1]
        colonnee=dernier[0]
        lignee=int(dernier[1])
        for zer in range(long_list_lettre):
            if list_lettre[zer]==colonnee:
                plus=zer+1
        taille=(lignee*26)+plus
        ligne=(taille//26)#+1
        colonne=taille-((taille//26)*26)
        couple1=str(list_lettre[colonne])+str(ligne) ## Nouvelle coordonnée !
        lista.append(couple1)
        print("lista = ",lista)
        return couple1
#####################################################
    def Get_Entree(self):
        print(" 1564 ## self.entree = ",self.Entree)
        question=self.Dico_memoire.get(self.Sortie,"N0")
        if question =="N0":
            print("1567 la sortie précédente  (",self.Sortie,")  n'était pas dans le dico")
            self.taille_discut+=1
            longueur_dico_tab=len(self.dico_tab)
            list_val_dico_tab=list(self.dico_tab.values())
            list_cle_dico_tab=list(self.dico_tab.keys())
            self.entree_entree=0
            for a in range(longueur_dico_tab):
                if list_val_dico_tab[a]==self.Entree:
                    print("1575 Attention, l'entrée  (",self.Entree,")  en cours a déjà été entrée...")
                    self.entree_entree=1
                    valeur=list_cle_dico_tab[a]
                    print("la valeur récupérée est : ",valeur)
                else:
                    ok=1
            if self.entree_entree==0:
                print("1582 lentree en cours (",self.Entree,") nétait pas déjà entree..")
                couple1=self.Trouver_new_coord()
                self.dico_tab[couple1]=self.Entree
                print("self.dico_tab E : ",self.dico_tab)
                list_val_dico_tab=list(self.dico_tab.values())
                print("list val = ",list_val_dico_tab)
                list_cle_dico_tab=list(self.dico_tab.keys())
                print("list clé = ",list_cle_dico_tab)
                long_dico_tab=len(list_cle_dico_tab)
                couple1="**"
                for a in range(long_dico_tab):
                    if list_val_dico_tab[a]==self.Entree:   #Sortie:
                        couple1=list_cle_dico_tab[a]
                self.Dico_memoire[self.Sortie]={"coord":couple1,self.Entree:1}
                print("self.Dico_memoire E 1603 : ",self.Dico_memoire)  
            else:
                print("lentree en cours était déjà entree..")
                self.entree_entree=0
                list_val_dico_tab=list(self.dico_tab.values())
                print("list val = ",list_val_dico_tab)
                list_cle_dico_tab=list(self.dico_tab.keys())
                print("list clé = ",list_cle_dico_tab)
                long_dico_tab=len(list_cle_dico_tab)
                couple1="**"
                for a in range(long_dico_tab):
                    if list_val_dico_tab[a]==self.Sortie:
                        couple1=list_cle_dico_tab[a]
                self.Dico_memoire[self.Sortie]={"coord":couple1,self.Entree:1}  # incre
                print("self.Dico_memoire E 1639 : ",self.Dico_memoire)
            self.discut[self.taille_discut]=couple1
            print("discut E 97 = ",self.discut)
            if self.taille_discut!=3:
                ok=1
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
            else:  ## on produit le décalage de discussion
                doublet=str(self.discut[1])+str(self.discut[2])
                print("doublet E=",doublet)
                self.dico_val[str(self.discut[3])]= 1  ###b taille_discut
                #### Analyse discussion
                interro=self.Dico_discussion.get(doublet,"N0")
                if interro=="N0":
                    print(" ** Ce doublet",doublet," n'avait pas déjà été enregistré dans la discut")
                    self.Dico_discussion[doublet]=self.dico_val
                else:
                    print(" ** Ce doublet",doublet," avait déjà été enregistré dans la discut")
                    print("\n * * * Voici linfo dico de ce doublet (",doublet,") :",interro)
                    inser=str(self.discut[3])
                    appro=interro.get(inser,"N0")
                    if appro=="N0":                    
                        interro[inser]=1
                    else:
                        interro[inser]=appro+1
                        print("********************  Yadza !!")
                    print("\n * * * * * * Voici le nouveau dico proposé pour ce doublet : ",interro)
                    self.Dico_discussion[doublet]=interro
                #### Fin Analyse discussion
                self.dico_val={}
                val1=self.discut[2]
                val2=self.discut[3]
                self.discut[1]=val1
                self.discut[2]=val2
                print("discut apres décalage = ",self.discut)
                self.taille_discut=self.taille_discut-1
                print("self.Dico_discussion E = ",self.Dico_discussion)
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
        else: ## la sortie précédente était dans le dico
            print("La sortie davant : ",self.Sortie," était déjà rentré : dico de la sortie 2032 = ",question)
            c=type(question)
            print("type(question) =",c)
            self.coordo=question["coord"]
            print("la coord de la sortie précédente (",self.Sortie,") est : ",self.coordo)
            self.taille_discut+=1
        #################################  yep
            longueur_dico_tab=len(self.dico_tab)
            print("longueur_dico_tab 2041 = ",longueur_dico_tab)
            list_val_dico_tab=list(self.dico_tab.values())
            list_cle_dico_tab=list(self.dico_tab.keys())
            self.entree_entree=0
            for a in range(longueur_dico_tab):
                print("a = ",a)
                print("list_val_dico_tab[a] = ",list_val_dico_tab[a])
                if list_val_dico_tab[a]==self.Entree:
                    print("Attention, l entree en cours a déjà été entrée...")
                    self.entree_entree=1
                    valeur=list_cle_dico_tab[a]
                    recup=self.Dico_memoire.get(self.Entree)
                    print("recup =",recup)
                    d=type(recup)
                    print("type recup = ",d)
                    coo_recup=recup.get("coord")
                    reponse=question.get(self.Entree,"N0") ###a
                    print("reponse=question.get(self.Entree,'N0')=",reponse)
                    if reponse=="N0":
                        print("youplii !")
                        question[self.Entree]=1 ###a
                        self.Dico_memoire[self.Sortie]=question  ###a                        
                    else:
                        freq=reponse+1
                        print("freq=reponse+1 =",freq)
                        question[self.Entree]=freq ###a
                        print("question modifiée =",question)
                        self.Dico_memoire[self.Sortie]=question ###a
                    print("self.Dico_memoire S : ",self.Dico_memoire)
                else:
                    print("pas trouvé")
                    ok=1
            if self.entree_entree==0:
                print("lentree en cours nétait pas déjà entree..")
                couple2=self.Trouver_new_coord()
                self.dico_tab[couple2]=self.Entree
                print("self.dico_tab S 1704 : ",self.dico_tab)
        #####################"  ici
                reponse=question.get(self.Entree,"N0") ###a
                print("reponse=question.get(self.Entree,'N0')=",reponse)
                if reponse=="N0":
                    print("youplaa !")
                    question[self.Entree]=1 ###a
                    self.Dico_memoire[self.Sortie]=question  ###a
                    if self.Sortie!="##":
                        ok=1
                        print("c'est 1")
                        self.Dico_memoire[self.Entree]={"coord":couple2} # ,self.Sortie:1}
                    else:
                        print("c'est 2")
                        self.Dico_memoire[self.Entree]={"coord":couple2}                    
                else:
                    freq=reponse+1
                    print("freq=reponse+1 =",freq)
                    question[self.Entree]=freq ###a
                    print("question modifiée =",question)
                    self.Dico_memoire[self.Sortie]=question ###a
                print("self.Dico_memoire S : ",self.Dico_memoire)
#######################################################################            
            self.discut[self.taille_discut]=self.coordo   ## couple2
            print("discut S2 = ",self.discut)
            if self.taille_discut!=3:
                ok=1 
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
            else:
                doublet=str(self.discut[1])+str(self.discut[2])
                print("doublet S2 =",doublet)
                #### Analyse discussion
                interro=self.Dico_discussion.get(doublet,"N0")
                if interro=="N0":
                    print(" ** Ce doublet",doublet," n'avait pas déjà été enregistré dans la discut")
                    self.dico_val[str(self.coordo)]=1
                    self.Dico_discussion[doublet]=self.dico_val
                else:
                    print(" ** Ce doublet",doublet," avait déjà été enregistré dans la discut")
                    print("\n * * * Voici linfo dico de ce doublet (",doublet,") :",interro)
                    inser=str(self.discut[3])
                    appro=interro.get(inser,"N0")
                    if appro=="N0":                    
                        interro[inser]=1
                    else:
                        interro[inser]=appro+1
                        print("********************  Yadza !!")
                    print("\n * * * * * * Voici le nouveau dico proposé pour ce doublet : ",interro)
                    self.Dico_discussion[doublet]=interro
                #### Fin Analyse discussion
                self.dico_val={}
                val1=self.discut[2]
                val2=self.discut[3]
                self.discut[1]=val1
                self.discut[2]=val2
                print("discut S2 apres decalage = ",self.discut)
                self.taille_discut=self.taille_discut-1
                print("self.Dico_discussion E = ",self.Dico_discussion)
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
#######################################################################################################
    def Get_sortie(self):
        question=self.Dico_memoire.get(self.Entree,"N0")
        if question =="N0":
            print("1762 L'entrée précédente (",self.Entree,") n'était pas dans le dico")
            self.taille_discut+=1
            longueur_dico_tab=len(self.dico_tab)
            list_val_dico_tab=list(self.dico_tab.values())
            list_cle_dico_tab=list(self.dico_tab.keys())
            self.entree_entree=0
            for a in range(longueur_dico_tab):
                if list_val_dico_tab[a]==self.Sortie:
                    print("1770 Attention, la sortie en cours (",self.Sortie,") a déjà été entrée...")
                    self.entree_entree=1
                    valeur=list_cle_dico_tab[a]
                else:
                    ok=1
            if self.entree_entree==0:
                print("1776 la sortie en cours (",self.Sortie,") nétait pas déjà entree..")
                couple2=self.Trouver_new_coord()
                self.dico_tab[couple2]=self.Sortie
                print("self.dico_tab S 1782 : ",self.dico_tab)
                dico1={}
                dico1["coord"]=couple2
                dico2={}
                dico2[self.Sortie]=1 ###c taille_discut
                list_val_dico_tab=list(self.dico_tab.values())
                print("list val = ",list_val_dico_tab)
                list_cle_dico_tab=list(self.dico_tab.keys())
                print("list clé = ",list_cle_dico_tab)
                long_dico_tab=len(list_cle_dico_tab)
                print("long_dico_tab 1791 = ",long_dico_tab)
                couple2="**"
                print("self.Entree 1794 =",self.Entree)
                for a in range(long_dico_tab):
                    print("a = ",a)
                    if list_val_dico_tab[a]==self.Entree:
                        couple2=list_cle_dico_tab[a]
                        print("New couple2 1799 = ",couple2)
                self.Dico_memoire[self.Entree]={"coord":couple2,self.Sortie:1} ###c taille_discut
                print("Dico_memoire S : ",self.Dico_memoire)
            else:
                self.entree_entree=0
                list_val_dico_tab=list(self.dico_tab.values())
                print("list val = ",list_val_dico_tab)
                list_cle_dico_tab=list(self.dico_tab.keys())
                print("list clé = ",list_cle_dico_tab)
                long_dico_tab=len(list_cle_dico_tab)
                couple2="**"
                for a in range(long_dico_tab):
                    if list_val_dico_tab[a]==self.Entree:
                        couple2=list_cle_dico_tab[a]
                self.Dico_memoire[self.Entree]={"coord":couple2,self.Sortie:1} # incre
                print("Dico_memoire S : ",self.Dico_memoire)
                ##################
            self.discut[self.taille_discut]=couple2
            print("discut S1 = ",self.discut)
            if self.taille_discut!=3:
                ok=1
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
            else:
                doublet=str(self.discut[1])+str(self.discut[2])
                print("doublet S1 =", doublet)
                self.dico_val[str(self.discut[3])]=1  ###b  taille_discut
                #### Analyse discussion
                interro=self.Dico_discussion.get(doublet,"N0")
                if interro=="N0":
                    print(" ** Ce doublet",doublet," n'avait pas déjà été enregistré dans la discut")
                    self.Dico_discussion[doublet]=self.dico_val
                else:
                    print(" ** Ce doublet",doublet," avait déjà été enregistré dans la discut")
                    print("\n * * * Voici linfo dico de ce doublet (",doublet,") :",interro)
                    inser=str(self.discut[3])
                    appro=interro.get(inser,"N0")
                    if appro=="N0":                    
                        interro[inser]=1
                    else:
                        interro[inser]=appro+1
                        print("********************  Yadza !!")
                    print("\n * * * * * * Voici le nouveau dico proposé pour ce doublet : ",interro)
                    self.Dico_discussion[doublet]=interro
                #### Fin Analyse discussion
                self.dico_val={}
                val1=self.discut[2]
                val2=self.discut[3]
                self.discut[1]=val1
                self.discut[2]=val2
                print("discut apres decalage S1 = ",self.discut)
                self.taille_discut=self.taille_discut-1
                print("Dico_discussion S = ",self.Dico_discussion)
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
        else:
            print("lentree précédente (",self.Entree,") était dans le dico")
            print("question = ",question)
            c=type(question)
            print("type(question) =",c)
            self.coordo=question["coord"]
            print("la coord de l'entrée précédente (",self.Entree,") est : ",self.coordo)
            self.taille_discut+=1
#################################  yep
            longueur_dico_tab=len(self.dico_tab)
            list_val_dico_tab=list(self.dico_tab.values())
            list_cle_dico_tab=list(self.dico_tab.keys())
            self.entree_entree=0
            for a in range(longueur_dico_tab):
                print("a= ",a)
                if list_val_dico_tab[a]==self.Sortie:
                    print("Attention, la sortie en cours a déjà été entrée...")
                    self.entree_entree=1
                    print("on passe self.entree_entree=1")
                    valeur=list_cle_dico_tab[a]
                    print("on passe valeur=list_cle_dico_tab[a] = ",valeur)
                    couple2=valeur
                    print("on passe couple2=valeur=",valeur)
                else:
                    ok=1
            if self.entree_entree==0:
                print("la sortie en cours nétait pas déjà entree..")
                couple2=self.Trouver_new_coord()
                self.dico_tab[couple2]=self.Sortie
                print("self.dico_tab S 1889 : ",self.dico_tab)            
#####################"  ici
            reponse=question.get(self.Sortie,"N0")
            if reponse=="N0":
                freq=1
                question[self.Sortie]=freq
                self.Dico_memoire[self.Entree]=question
                self.Dico_memoire[self.Sortie]={"coord":couple2} # ,self.Entree:1}                
            else:
                freq=reponse+1
                question[self.Sortie]=freq
                self.Dico_memoire[self.Entree]=question
            print("Dico_memoire S : ",self.Dico_memoire)
            self.discut[self.taille_discut]=self.coordo   ## couple2
            print("discut S2 = ",self.discut)
            if self.taille_discut!=3:
                ok=1
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
            else:
                doublet=str(self.discut[1])+str(self.discut[2])
                print("doublet S2 =",doublet)
                interro=self.Dico_discussion.get(doublet,"N0")
                if interro=="N0":
                    print(" ** Ce doublet",doublet," n'avait pas déjà été enregistré dans la discut")
                    self.dico_val[str(self.coordo)]=1
                    self.Dico_discussion[doublet]=self.dico_val
                else:
                    print(" ** Ce doublet",doublet," avait déjà été enregistré dans la discut")
                    print("\n * * * Voici linfo dico de ce doublet (",doublet,") :",interro)
                    inser=str(self.discut[3])
                    appro=interro.get(inser,"N0")
                    if appro=="N0":                    
                        interro[inser]=1
                    else:
                        interro[inser]=appro+1
                        print("********************  Yadza !!")
                    print("\n * * * * * * Voici le nouveau dico proposé pour ce doublet : ",interro)
                    self.Dico_discussion[doublet]=interro
                #### Fin Analyse discussion
                self.dico_val={}
                val1=self.discut[2]
                val2=self.discut[3]
                self.discut[1]=val1
                self.discut[2]=val2
                print("discut S2 apres decalage = ",self.discut)
                self.taille_discut=self.taille_discut-1
                print("Dico_discussion E = ",self.Dico_discussion)
                return self.Entree, self.Sortie, self.taille_discut, self.dico_tab, self.Dico_discussion, self.Dico_memoire
#############################################
if __name__ == "__main__":
        #########
    font = cv2.FONT_HERSHEY_SIMPLEX  # FONT_HERSHEY_SIMPLEX  # FONT_HERSHEY_PLAIN
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
###################################################