#sub_call.py
''' It lets the user to choose a stream and receive marks of different subjects as per the subject combination'''
import RAM.commerce.commerce_sub as com
import RAM.humanities.hum_sub as hum
import RAM.science.sci_sub as sci
#Functions
def Subjects_Chooser():
    '''' Calls all the streams'''
    print("CHOOSE A STREAM\n")
    choose_stream=input("Press\n A.SCIENCE\n B.COMMERCE \n C.HUMANITIES\n")
    if choose_stream=='A' or choose_stream=='a':
            sci.Science_Input()
    if  choose_stream=='B' or choose_stream=='b':
            com.Commerce_Input()
    if  choose_stream=='C' or choose_stream=='c':
            hum.Humanities_Input()
            
            
        
#sci_file=open("C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\RAM\\science\\ins_science.txt","a+")


