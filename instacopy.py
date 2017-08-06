#!/usr/bin/env python
import time, sys, os
from instaLooter import InstaLooter
from instaLooter.urlgen import resizer

conta = sys.argv[1]

if not sys.argv[1]:
	conta = raw_input("Informe a conta do instagram: ")

pasta_imagens = "imagens"
if not os.path.exists(pasta_imagens):
	os.makedirs(pasta_imagens)
pasta_legendas = "legendas"
if not os.path.exists(pasta_legendas):
	os.makedirs(pasta_legendas)



looter = InstaLooter(profile=conta, get_videos=False, url_generator=resizer(640), directory=pasta_imagens)

print "Baixando imagens..."
looter.download()
print "Salvo na pasta %s" % pasta_imagens

print "Baixando legendas..."
counter = 0
for media in looter.medias():
	filename = "%s/caption%d.txt" % (pasta_legendas, counter)
	arq = open(filename, "w")
	try:
		arq.write(media["caption"].encode('utf8', 'ignore'))
	except KeyError:
		pass
	arq.close()
	time.sleep(0.1)
	counter += 1
print "Salvo na pasta %s" % pasta_legendas
