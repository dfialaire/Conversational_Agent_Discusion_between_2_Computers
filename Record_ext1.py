# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 20:55:43 2020

@author: dfial
"""

import numpy as np
import pyttsx3
from time import gmtime, strftime
import sounddevice as sd
from scipy.io.wavfile import write ## enregistrer des fichiers WAV à partir de données
import wavio as wv 
#from Reconnaitre3_self import * ## Module necessitant detre en exterieur
#from Reconn_Face import *
def rec(yepi):
    horloge=strftime("%Y-%m-%d %H:%M:%S")
    print("\n Passage Rec = ",horloge)
    print("Passage par Rec...")
#    self.ui.groupBox_3.setVisible(True)    
#    self.ui.Mic_Ferm.setChecked(False)
#    self.ui.Mic_Ac.setChecked(True)

    engine = pyttsx3.init()
    # Set properties _before_ you add things to say
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
#    yepi="Je vous écoute"
    engine.say(yepi)
    engine.runAndWait()
    freq = 44100
    duration = 3
    # Start recorder with the given values 
    # of duration and sample frequency 
#    try:
    recording = sd.rec(int(duration * freq), 
    				samplerate=freq, channels=2) 
        # Record audio for the given number of seconds 
    sd.wait() 
#    except PortAudioError:
#        print("\n Attention, aucun micro n'est repéré...\n")
#        print("Changements de bouton 12")
#        self.fin=1
#        self.stop=1
#        self.ui.Ecrit.setChecked(True)
#        print("12 2")
#        self.ui.radioButton.setChecked(True)
#        print("12 3")

#        break
    # This will convert the NumPy array to an audio 
    # file with the given sampling frequency 
    #####     write("recording0.wav", freq, recording)   ## precedemment : 2 fichier : le 0 est + gros
    # Convert the NumPy array to audio file 
    wv.write("recording1.wav", recording, freq, sampwidth=2) ## fichier1 + petit et fonctionnel                    
#    self.ui.Mic_Ferm.setChecked(True)
#    self.ui.Mic_Ac.setChecked(False)              