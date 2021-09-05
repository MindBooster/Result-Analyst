#hum_sub.py
'''  It receives marks of different subjects of Humanities as per the subject combination'''

#Functions
def Humanities_Input():
    '''' defines methods to receive details of a humanities student'''
    #percentage of boards CBSE hummanities 1
    print("enter marks of the following subjects:")
    e=float(input("English"))
    h=float(input(" history"))
    p=float(input("Enter the marks of political science"))
    geo=float(input("Enter the marks of geography"))
    psy=float(input("Enter the marks of psycology"))
    pe=float(input("Enter the marks of Physical Education"))
    sum=e+p+psy+geo+h+pe
    min=pe
    if h<min:
        min=h
    if p<min:
        min=p
    if geo<min:
        min=geo
    if psy<min:
        min=psy
    print(min)
    TM=sum-min
    per=(TM/500)*100
    print("Percentage accuired in boards (Best of five):",per,"%")

            
        
#sci_file=open("C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\RAM\\science\\ins_science.txt","a+")


