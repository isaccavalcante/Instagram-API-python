#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI

user, pwd = 'justgirls.me', '500reaispracada'

InstagramAPI = InstagramAPI(user,pwd)
InstagramAPI.login() # login

InstagramAPI.uploadPhoto("/home/isac/Dropbox/Instagram-API-python/examples/ibagens/1.jpg",caption="love",upload_id=None)
