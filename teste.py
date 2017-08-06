#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# testes.py
# written by isac
# isaccavalcante AT trixlog DOT com
import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.instagram.com/resultadosrapidos')
soup = BeautifulSoup(page.content, "html.parser")

follow = soup.find("meta",  property="og:description")
lista = follow["content"].split('-')[0].split()


seguidores = lista[0]
seguindo = lista[2]
publicacoes = lista[4]


print seguidores
print seguindo
print publicacoes


