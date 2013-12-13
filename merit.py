#MSC Merit System
#Code by Harrison Scott 2013

#Version History:
#   0.0.1 - added usernames
#   0.0.2 - added merits
#               added logging out
#               added user types
#   0.0.3 - added sending merits
#   0.0.4 - added passwords
#             - added requests, no accepting yet

import getpass
#functions
def login(u,p):
    us = open("merit/user.txt").read()
    if u in users and us[us.index(u)+len(u)] == "|" and p in us and us[us.index(p)+len(p)] =="\\":
        return True
    else:
        return False
def comlist(t):
    print("\nCommands:\n'logout'")
    if t != "s":
        print("'send'")
    else:
        print("'request'")
    return ""

#variables
version = "0.0.4"
title = open("merit/title.txt").read()
users = open("merit/user.txt").read()

#login
logged = False
isquit = False
print(title,"\nVersion:",version,"\n\nLogin:")
while logged == False and isquit == False:
    
    username = input("Username:    ").lower()
    password = input("Password:    ")
    
    if login(username,password):
    
        #logged in now
        print("\nWelcome,",username)
        logged = True
        
        #work out if teacher or student or admin
        user_type = users[1+users.index(username)+len(username)]
        if user_type == "a":
            print("        Administrator user type")
            #teacher/admin load functions
            #get requests from file
            my_file = "merit/requests/"+str(username.lower())+".txt"
            my_merits = open(my_file).readlines()
            #print requests  from variables  
            print("\nMerit Requests:")
            for line in my_merits:
                print(line)
        elif user_type == "t":
            print("        Teacher user type")
            #teacher/admin load functions
            #get requests from file
            my_file = "merit/requests/"+str(username.lower())+".txt"
            my_merits = open(my_file).readlines()
            #print requests  from variables  
            print("\nMerit Requests:")
            for line in my_merits:
                print(line)
        elif user_type == "s":
            print("        Student user type")
            #student load functions
            #get merits from file
            my_file = "merit/merits/"+str(username.lower())+".txt"
            my_merits = open(my_file).readlines()
            #get number of merits from file
            with open(my_file, "r") as f:
                i = -1
                for i, l in enumerate(f):
                    pass
                my_file_len =  i + 1
            #print number and merits  from variables  
            print("You have",my_file_len,"merit(s)\n\nMerits:")
            for line in my_merits:
                print(line)          
        else:
            print("       ",user_type,"user type. Defaulting to student...")
            user_type = "s"
        
        
        
        
        
        #commands
        com = ""
        while com != "logout":
            com = input("\nEnter a command. Type 'commands' for help.    ")
            if com == "commands":
                print(comlist(user_type))
            elif com ==  "send" and user_type != "s":
                rvalid = False
                while rvalid == False:
                    recipient = input("\nStudent to send merit too:    ")
                    if recipient.lower() in users and users[users.index(recipient)+len(recipient)] == "|":
                        if users[1+users.index(recipient)+len(recipient)] == "s":
                            reason = input("Description:    ")
                            with open("merit/merits/"+str(recipient.lower())+".txt", "a") as recipfile:
                                recipfile.write(reason+"\n")
                            #print(open("merit/merits/"+str(recipient.lower())+".txt").readlines())
                            print("\nMerit sent!")
                            rvalid = True
                            
                        else:
                            print("\nYou may only send merits to students.")
                    else:
                        print("User not found.")
                        
            
            elif com ==  "request" and user_type == "s":
                rvalid = False
                while rvalid == False:
                    recipient = input("\nTeacher to send merit request too:    ")
                    if recipient.lower() in users and users[users.index(recipient)+len(recipient)] == "|":
                        if users[1+users.index(recipient)+len(recipient)] == "t" or users[1+users.index(recipient)+len(recipient)] == "a":
                            reason = input("Description:    ")
                            with open("merit/requests/"+str(recipient.lower())+".txt", "a") as recipfile:
                                recipfile.write(reason+"\n")
                            #print(open("merit/merits/"+str(recipient.lower())+".txt").readlines())
                            print("\nMerit sent!")
                            rvalid = True
                            
                        else:
                            print("\nYou may only send merits to students.")
                    else:
                        print("User not found.")
            elif com == "logout":
                print("\nLogging out...")
                for i in range(0,60):
                    print("")
                print("MSC Merit System Version",version,"\n\nLogin:")
            else:
                print("\nInvalid command.")
        logged = False
    else:
        print("\nIncorrect username/password")
