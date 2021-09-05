#sci_sub.py
'''  It lets user to receive marks of different subjects of science as per the subject combination'''
#Functions
def Science_Input():
    '''' defines methods to receive details of a science student'''
    sub_c=int(input("Choose subject combination:\n 1. PHY(040) | CHEMISTRY (041) | MATHS (042) | CS (083) | ENG(044) | PHY EDU(048) \n 2. PHY(040) | CHEMISTRY (041) | MATHS (042) | BIOLOGY (044) | ENG(044) | PHY EDU(048) \n 3. PHY(040) | CHEMISTRY (041) | MATHS (042) | ENG(044) | PHY EDU(048)\n 4. PHY(040) | CHEMISTRY (041)| BIOLOGY (044) | ENG(044) | PHY EDU(048) \n 5. PHY(040) | CHEMISTRY (041) | COMPUTER SCIENCE (044) | ENG(044) | PHY EDU(048)\n 6. PHY(040) | CHEMISTRY (041) | MATHS (042) | COMPUTER SCIENCE (083) | ENG(044) \n"))
    if sub_c==1:
            print("Enter marks in the following Subjects:\n")
            eng=float(input("English: "))
            #sci_file.write(str(eng))
            p=float(input("Physics: "))
            #sci_file.write(str(p))
            c=float(input("Chemistry: "))
            #sci_file.write(str(c))
            cs=float(input("Computer Science: "))
            #sci_file.write(str(cs))
            m=float(input("Maths: "))
            #sci_file.write(str(m))
            pe=float(input("Physical Education: "))
            #sci_file.write(str(pe))
            #sci_file.close()
            min=p
            if c<min:
                min=c
            if cs<min:
                min=cs
            if m<min:
                min=m
            if pe<min:
                min=pe
            total=(eng+p+c+cs+m+pe)-min
            p=(total/500)*100
            #print("Marks Obtained: ",total)
            #print("Percentage: ",p," % ")
            print("\t\tSBOA PUBLIC SCHOOL")
            print("SUBJECT\t\tMARKS\n")
            print("-------\t\t-----\n")
            print("English\t\t",eng,"\n")
            print("Physics\t\t",p,"\n")
            print("Chemistry\t\t",c,"\n")
            print("Computer Science\t\t",cs,"\n")
            print("Maths\t\t",m,"\n")
            print("Physical Education\t\t",pe,"\n")
            print("------------------------------")
            print("TOTAL:",total)
            print("PERCENTAGE: ",p,"%")
            
            
    
            
            
        
#sci_file=open("C:\\Users\\Hp\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\RAM\\science\\ins_science.txt","a+")


