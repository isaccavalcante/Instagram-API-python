#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = "/home/isac/Dropbox/Instagram-API-python/examples/ibagens/" # mude o diretório para a pasta com as fotos
IGUSER    = "justgirls.me" # mude para o nome de usuário
PASSWD    = "500reaispracada" # mude para a senha
# mude para a hashtag
IGCaption = "LEGENDA AQUI #hashtag" # TODO: Receber uma lista de legendas


os.chdir(PhotoPath)
ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))]
print ("Total de imagens nesta pasta:" + str (len(ListFiles)))

# fazendo login 
igapi = InstagramAPI(IGUSER,PASSWD)
igapi.login() 

# Percorrendo as imagens da pasta
for i in range(len(ListFiles)):
    with open("log.txt", "a") as arquivo:
        photo = ListFiles[i]
        msg  = "Progresso :" + str([i+1]) + " de " + str(len(ListFiles))
        print(msg)
        log = "Fazendo upload da foto para o instagram: " + photo
        print(msg)
        igapi.uploadPhoto(photo,caption=IGCaption,upload_id=None)
        n = randint(28800, 36000) # espera entre 8 e 10 horas para postar a proxima imagem
        msg = "Esperando " + str(float(n)/60.0/60.0) + " horas..."
        print(msg)
        time.sleep(n)