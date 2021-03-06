###############################
"User-Safe" Password Organizer
###############################

User-Safe is a program to save usernames and passwords for all the different online accounts
that the modern internet user has. Users are prompted to input the website, username and password,
which is then stored. Users can then look up stored information by typing in the name of the 
website, which will then generate the username and password on file.

Funcional requirements for password organization program.
--------------------------------------------------------------------------------------------------------------


*********************
Persona
*********************

Name: 
===============
Alex

Details:
===============
A Young professional that works full time in an office and is also an online student.
Uses computer and technology often for many different tasks, including, work, 
studies and entertainment. Currently lives abroad and does not want to accumulate
too many physical belongings and items. Sometimes unorganized and forgetful.

Goals:
===============
Wants to be able to store information digitally rather than in writing in a notebook
to allow for better organization, accessibility and portability, facilitating travel and
avoiding loss.



*********************
Problem Scenario
*********************

Problem Scenario:
==========================
As Alex relies on the computer and different internet accounts to carry out his activities.
He has many different user accounts on many different sites, each of which require different
username and password specifications. All of these different combinations are
very difficult for him to remember.

Current Alternatives:
==========================
Write down user information in notebook; keep Excel or Word document of user information;
try to remember user information and complete reset procedures when he forgets such 
information.

Value Proposition:
==========================
Create a program to store user information that corresponds to certain sites, such as 
Blackboard, Netflix, Facebook, etc. User should be able to enter information via interactive
prompt and have it automatically stored.The user can then call user information by inputting
the website name, to be displayed cleanly in a table. In order to call the user information, 
it may be beneficial to require the entry of a password and to encrypt the stored information.


************************
User Stories
************************
As Alex the young worker/student, I want to be able to store all of my user information in
one program on my computer, allowing me to input this information once and be able to
retrieve it easilly later on. I do not want to have to write anything down. I want to be able
to type in the name of the service and have it generate my saved username and password.
The service should be secure, so there should a at least a password prompt in order to receive 
the information.

*************************
Acceptance Stories
*************************

Scenario 01: Storing User Information
Given that I do not want to write my passwords and usernames on paper, I need a program
in which to store them. 
When I open up the program, I will be prompted to either enter a new password or to
look up a current one. When choosing to enter new user information I will be prompted
to enter the corresponding website, username, and password, which will then be written
to a file. Ideally, when stored, passwords would be encrypted.

Scenario 02: Looking Up User Information
When user information for a website is forgotten, it may be consulted using the program.
When I choose to consult my user information for a site, I will need to first enter a password.
This password mustn't be forgotten, or else I will not be able to access any user information.
Password retrievel questions may be added, to be prompted after a certain number of failed attempts..
After the password is entered correctly, I should be able to type in the website and access
both the username and password.
