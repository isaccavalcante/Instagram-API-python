#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Edited by: Isac C.
# isaccavalcante AT alu DOT ufc DOT br
import os
import sys
import time
import requests
from bs4 import BeautifulSoup
sys.path.append(os.path.join(sys.path[0], 'src'))
from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol
from random import shuffle

bot = InstaBot(
    login="justgirls.me",
    password="500reaispracada",
    like_per_day=999,
    comments_per_day=7,
    tag_list=['follow4follow', 'f4f', 'cute', 'likeforlike', 'l4l',
"love", "instagood", "photooftheday", "beautiful", "fashion", "tbt", 
"happy", "cute", "me", "follow", "picoftheday", "selfie", "instadaily",    
"friends", "summer", "girl", "art", "sexy", "hot","nofilter", "fitness",
"style", "life", "travel","pretty", "makeup"],
    tag_blacklist=['blacklist1','blacklist2'],
    user_blacklist={},
    max_like_for_one_tag=99,
    follow_per_day=333,
    follow_time=1 * 60,
    unfollow_per_day=111,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["this", "the", "your", "a", "Wow. this", "Nice! this"], 
                  #######
                  ["photo", "picture", "pic", "shot", "snapshot", "take"], 
                  #######
                  ["is", "looks", "feels", "is really", "really", "is kinda", "is so", "is almost"], 
                  #######
                  ["great", "super", "good",
                    "cool", "GREAT","magnificent", "magical",
                    "stylish", "beautiful", "so beautiful",
                    "professional", "so lovely", "lovely", "glorious",
                   "gorgeous", "adorable", "excellent", "amazing"],
                  [".", "...", "!", ". May I repost it?", ". Can I repost it?"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list= ["user1", "user2"],
    unfollow_whitelist=['ana_hauachen', 'isac.jpg'])
while True:
    shuffle(bot.tag_list)
    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 2

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        # Enquanto seguir mais que 200 além dos seguidores:
        # começar a dar unfollow em quem não segue de volta
        # Exemplo: seguindo 1200, com 1000 seguidores
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(15 * 60) # Espera 15 minutos
            check_status(bot)
        # Enquanto seguir menos que 400 além dos seguidores:
        # ????
        # Exemplo: seguindo 1000, seguidores 1200 
        while bot.self_following - bot.self_follower < 200:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot) # ???
                time.sleep(5 * 60) # Espera 5 minutos
                follow_protocol(bot) # ???
                time.sleep(10 * 60) # Espera 10 minutos
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
