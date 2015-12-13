#!user/bin/env python
# -*- coding: utf-8 -*-
"""Final Project"""

import pickle
import os

USERINPUT = raw_input('Would you like to enter a new password or '
                      'look up an old one? Enter: "new" or "look up" ')
USERINPUT = USERINPUT.lower()

USERDICT = {}

if os.path.exists('user_info.pkl'):
    filehandler = open('user_info.pkl', 'rb')
    USERDICT = pickle.load(filehandler)
    filehandler.close()
else:
    filehandler = open('user_info.pkl', 'wb')
    filehandler.close()

if USERINPUT == 'new':
    ENTERNEW = raw_input('Please enter the name of the website. '
                         'Ex.: facebook.com ')
    ENTERNEW = ENTERNEW.lower()
    ENTERNEW_NAME = raw_input('Please enter your username for this website ')
    ENTERNEW_NAME = ENTERNEW_NAME.lower()
    ENTERNEW_PASS = raw_input('Please enter you password for this website ')
    ENTERNEW_PASS = ENTERNEW_PASS.lower()
    
    if ENTERNEW not in USERDICT:
        
        USERDICT[ENTERNEW] = (ENTERNEW_NAME, ENTERNEW_PASS)
        filehandler = open('user_info.pkl', 'wb')
        pickle.dump(USERDICT, filehandler)
        filehandler.close()


elif USERINPUT == 'look up':
    LOOKUP = raw_input('Please enter the website for which you would like to '
                  'look up your user information ')
    USERINFO = 'Your user information for the website\ "{}" is as follows:\n\
                USERNAME: {}\n\
                PASSWORD: {}'

    print USERINFO.format(LOOKUP.upper(), USERDICT[LOOKUP][0], USERDICT[LOOKUP][1])


    

                     
