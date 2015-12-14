#!user/bin/env python
# -*- coding: utf-8 -*-
"""Final Project"""

import pickle
import os

RUN_PROGRAM = True


def usersafe():
    """ Program to add new and look up user informatino from a file.
    Args:
        None - defaults to True so program will continue running.
    Returns:
        Allows user to input user information for a website or retrieve
        previousy input information.
    Examples:
    >>>Would you like to enter a new password or look up an old one?
    Enter: "new" or "look up" new
    Please enter the name of the website. Ex.: facebook.com: WEBSITE
    Please enter your username for this website: USERNAME
    Please enter your password for this website: PASSWORD

    >>>Would you like to enter a new password or look up an old one?
    Enter: "new" or "look up" look up
    Please enter the website for which you would like to look up
    your user information: facebook.com
                USERNAME: username
                PASSWORD: password
    """
    userinput = raw_input('Would you like to enter a new password or \
look up an old one? Enter: "new" or "look up" ')
    userinput = userinput.lower()

    userdict = {}

    if os.path.exists('user_info.pkl'):
        filehandler = open('user_info.pkl', 'rb')
        userdict = pickle.load(filehandler)
        filehandler.close()

    if userinput == 'new':
        enternew = raw_input('Please enter the name of the website. '
                             'Ex.: facebook.com: ')
        enternew = enternew.lower()
        enternew_name = raw_input('Please enter your username for this \
website: ')
        enternew_name = enternew_name.lower()
        enternew_pass = raw_input('Please enter your password for \
this website: ')
        enternew_pass = enternew_pass.lower()

        if enternew not in userdict:  # adds new input

            userdict[enternew] = (enternew_name, enternew_pass)
            filehandler = open('user_info.pkl', 'wb')
            pickle.dump(userdict, filehandler)
            filehandler.close()
            print '\nYou have successfully entered your user information!\n'
            return None

        elif enternew in userdict:  # replaces old input if same website
            updatedict = {}
            updatedict[enternew] = (enternew_name, enternew_pass)
            userdict.update(updatedict)
            filehandler = open('user_info.pkl', 'wb')
            pickle.dump(userdict, filehandler)
            filehandler.close()
            print '\nYou have successfully updated your user information!\n'
            return None

    elif userinput == 'look up':
        lookup = False
        while lookup not in userdict:
            lookup = raw_input('Please enter the website for which you would \
like to look up your user information: ')

        userinfo = 'Your user information for the website "{}"\
is as follows:\n\n\
                    USERNAME: {}\n\
                    PASSWORD: {}\n\n\n'

    print userinfo.format(lookup.upper(), userdict[lookup][0],
                          userdict[lookup][1])
    return None

while RUN_PROGRAM:  # keeps program running
    usersafe()
