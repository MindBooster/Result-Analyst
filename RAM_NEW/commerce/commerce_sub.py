#commerce_sub.py
''' It lets the user to choose a stream and receive marks of different subjects as per the subject combination'''

#Functions
def Commerce_Input():
    '''' defines methods to receive details of a commerce student'''
    #percentage of boards CBSE commerce 1
    print("Percentage caculater")
    e=float(input("Enter the marks of English"))
    a=float(input("Enter the marks of Accountacy"))
    b=float(input("Enter the marks of Business studies"))
    eco=float(input("Enter the marks of Economics"))
    m=float(input("Enter the marks of Maths"))
    pe=float(input("Enter the marks of Physical Education"))
    sum=e+a+eco+b+m+pe
    min=pe
    if a<min:
        min=a
    if m<min:
        min=m
    if eco<min:
        min=eco
    if b<min:
        min=b
    print(min)
    TM=sum-min
    per=(TM/500)*100
    print("Percentage accuired in boards (Best of five):",per,"%")


            
        
#sci_file=open("C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\RAM\\science\\ins_science.txt","a+")


