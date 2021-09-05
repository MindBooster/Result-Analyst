#registration.py
'''Defines functions to register and login into the system'''
import RAM.sub_call as subjects

#Functions
def login():
    uname="Bhargab"
    pwd='*****'
    uname=input("Enter Login Details\n User Name: ")
    pwd=input("  Password: ")
    if uname=="Bhargab" and pwd=='*****':
        print("Login Success")
        subjects.Subjects_Chooser()
    else:
        print("Invalid Login Details")
