#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#https://openclassrooms.com/forum/sujet/pyaudio-enregistre-son-puis-associe-tkinter
"""
Created on Fri Dec  3 16:11:37 2021

@author: thomaslesaulnier
"""

import pyaudio
import wave
  
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "test.wav"
  
audio = pyaudio.PyAudio()
  
                                        # Debut enregistrement
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print("Enregistrement en cours...")
 
frames = []
  
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
     
print("Fin d'enregistrement")
  
  
                                        # Fin enregistrement
stream.stop_stream()
stream.close()
audio.terminate()
  
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()