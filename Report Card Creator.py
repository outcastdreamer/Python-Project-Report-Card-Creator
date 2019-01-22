import time
import os
from Tkinter import *
import tkMessageBox
import tkSimpleDialog
import string
import random
import getpass
import base64     
import math

#let's Begin!!
class RM1(object):
   #'Clas' has been used instead of 'Class' as python recognizes 'class' as a built-in object to represent the class student studies in.
    os.system('cls')
    def __init__(self,ct_name="teacher",school_name="null",user="null",total_no=0,date=0,student_name="null",clas="null",sec="null",roll_no=0,stream="null",no_subs=0,subjects="null",perc=0,search=[],):
            self.ct_name=ct_name
            self.school_name=school_name
            self.user=user
            self.total_no=total_no
            self.date=date
            self.student_name=student_name
            self.clas=clas
            self.sec=sec
            self.roll_no=roll_no
            self.stream=stream
            self.no_subs=no_subs
            self.subjects=subjects
            self.perc=perc
            self.search=search
            self.makedir()
    def makedir(self):
            z1="C:\Users\Saket\Desktop"
            z="RM1"
            z2="\RM1"
            z3=os.listdir(z1)
            flag=0
            for i in range(len(z3)):
                if z3[i]==z:
                    os.chdir(z1+z2)
                    flag=1
            if flag==0:
                os.mkdir(z1+z2)
                os.chdir(z1+z2)
            self.data_entry()
    def data_entry(self):
            root=Tk()
            w=Label(root,text="REPORT MASTER 1.0~\n Welcomes You!!")
            w.pack()
            time.sleep(1)
            print "REPORT MASTER 1.0 is loading!"
            time.sleep(1)
            print "Loading!"
            time.sleep(1)
            print "Loading!"
            print "Kindly read all the instructions before filling the fields!"
            time.sleep(2)
            self.user=tkMessageBox.askyesno("WELCOME TEACHER!!~","\tTHANK YOU FOR USING REPORT MASTER 1.0!!\nREPORT MASTER 1.0 is a copyright of SSLabs~\nREPORT MASTER 1.0 aims to help teachers make report cards and maintain them with ease.\n\n\t Are you an Existing user or New User?\n Click \'YES\' if you are an existing user or \'NO\' if you are a new user - ")
            if self.user==True:                #Creating user profiles txt file to store profile names
                self.file=open("Users.txt",'a')
                self.file.close()
                self.file=open("Users.txt",'r')
                self.file.seek(0)
                x1=self.file.readlines()
                if x1==[]:                      #Checking if the user profiles is empty or not
                    pop=tkMessageBox.showerror("ERROR!!","Our records are currently empty!!\nKindly make a new profile!!")
                    root.destroy()
                    quit()
                self.file=open("Users.txt",'r')
                x=self.file.read()     #Enter user name to check if your profile exists or not
                self.b=tkSimpleDialog.askstring("REPORT MASTER 1.0~","Kindly enter your name of your profile to use your profile and it\'s details - ")
                print "\t","----------------------------------------------------------------"
                time.sleep(1)
                print "Checking our records..."
                time.sleep(1)
                print "Please wait, we are almost done..."  #Searching for existing profiles here
                self.search=x.split()
                self.store=self.b.split()
                if len(self.store)==1:
                        for i in range(len(self.search)):        #Searching for first name users here
                            flag=0
                            k=self.search[i]
                            if k==self.b:
                                self.password_check()
                                self.ct_name=self.search[i]
                                self.choice=tkSimpleDialog.askinteger("WELCOME "+self.ct_name.upper()+"!!~","It's good to see you again!!\nKindly Choose what you want to do with your existing data - \n\t1)Open Report card file\n\t2)Open Directory of Report Card file.\n\t3)Exit \nType 1,2 or 3 to choose - ")
                                flag=1      #ENTER CHOICE OPTIONS HERE
                                if self.choice==1:
                                    self.opening()
                                if self.choice==2:
                                    os.startfile(os.getcwd())
                                    self.ending()
                                if self.choice==3:
                                    msg=tkMessageBox.showinfo("RESULT MASTER 1.0~","THANK YOU FOR USING REPORT MASTER 1.0!!\nWe hope to see you again!")
                                    self.ending()
                                    root.destroy()
                                    quit()
                        if flag==0:
                            self.pop2=tkMessageBox.askyesno("ERROR!!","Our Records show you are not an existing user! Would you like to make a new profile!?")
                            if self.pop2==False:
                                    msg=tkMessageBox.showinfo("RESULT MASTER 1.0~","THANK YOU FOR USING REPORT MASTER 1.0!!\nWe hope to see you again!")
                                    root.destroy()
                                    quit()
                            if self.pop2==True:
                                    self.ct_name=tkSimpleDialog.askstring("REPORT MASTER 1.0~","WELCOME TEACHER!!\n Thank you for using REPORT MASTER 1.0~\nKindly enter your name to build your profile for your class - ")
                                    self.file=open("Users.txt",'a')
                                    self.file.writelines(self.ct_name+" ")
                                    self.file.close()
                                    self.password_store()
                if len(self.search)<2:              #FAKE ENTRY OF USERNAME
                        if len(self.store)==2:
                            self.pop3=tkMessageBox.askyesno("ERROR!!","Our Records show you are not an existing user! Would you like to make a new profile!?")
                            if self.pop3==False:
                                    msg=tkMessageBox.showinfo("RESULT MASTER 1.0~","THANK YOU FOR USING REPORT MASTER 1.0!!\nWe hope to see you again!")
                                    root.destroy()
                                    quit()
                            if self.pop3==True:
                                    self.ct_name=tkSimpleDialog.askstring("REPORT MASTER 1.0~","WELCOME TEACHER!!\n Thank you for using REPORT MASTER 1.0~\nKindly enter your name to build your profile for your class - ")
                                    self.file=open("Users.txt",'a')
                                    self.file.writelines(self.ct_name+" ")
                                    self.file.close()
                                    self.password_store()
                if len(self.search)>2:
                        if len(self.store)==2:          #Searching for first & Surname users
                                for i in range(len(self.search)):
                                    flag1=0
                                    k=self.search[i]+" "+self.search[i+1]
                                    if k==self.b:
                                        self.password_check()
                                        self.ct_name=self.search[i]+" "+self.search[i+1]
                                        self.choice=tkSimpleDialog.askinteger("WELCOME "+self.ct_name.upper()+"!!~","It's good to see you again!!\nKindly Choose what you want to do with your existing data - \n\t1)Open Report card file\n\t2)Open Directory of Report Card file.\n\t3)Exit \nType 1,2 or 3 to choose - ")
                                        flag1=1      #ENTER CHOICE OPTIONS HERE
                                        if self.choice==1:
                                            self.opening()
                                        if self.choice==2:
                                            os.startfile(os.getcwd())
                                            self.ending()
                                        if self.choice==3:
                                            msg=tkMessageBox.showinfo("RESULT MASTER 1.0~","THANK YOU FOR USING REPORT MASTER 1.0!!\nWe hope to see you again!")
                                            self.ending()
                                            root.destroy()
                                            quit()
                                if flag1==0:
                                    self.pop1=tkMessageBox.askyesno("ERROR!!","Our Records show you are not an existing user! Would you like to make a new profile!?")
                                    if self.pop1==False:
                                            msg=tkMessageBox.showinfo("RESULT MASTER 1.0~","THANK YOU FOR USING REPORT MASTER 1.0!!\nWe hope to see you again!")
                                            root.destroy()
                                            quit()
                                    if self.pop1==True:
                                            self.ct_name=tkSimpleDialog.askstring("REPORT MASTER 1.0~","WELCOME TEACHER!!\n Thank you for using REPORT MASTER 1.0~\nKindly enter your name to build your profile for your class - ")
                                            self.file=open("Users.txt",'a')
                                            self.file.writelines(self.ct_name+" ")
                                            self.file.close()
                                            self.password_store()
            if self.user==False:       #Making a new profile here
                self.ct_name=tkSimpleDialog.askstring("REPORT MASTER 1.0~","WELCOME TEACHER!!\n Thank you for using REPORT MASTER 1.0~\nKindly enter your name to build your profile for your class - ")
                self.file=open("Users.txt",'a')
                self.file.writelines(self.ct_name+" ")
                self.file.close()     #ADDING DETAILS
            pop=tkMessageBox.showinfo("NOTICE!","Now the data will be inputed on python console to maintain simplicity.\n Thank you.")
            self.password_store()
            self.school_name=tkSimpleDialog.askstring(self.ct_name+"\'s Profile~","Enter the name of school you work for - ")
            self.clas=tkSimpleDialog.askstring(self.ct_name+"\'s Profile~","Kindly enter the class you teach - \n(NOTE - Don't Input Section yet)")
            self.sec=tkSimpleDialog.askstring(self.ct_name+"\'s Profile~","Enter the section of the class - ")
            time.sleep(0.5)
            pop=tkMessageBox.showinfo("NOTICE!","Kindly avoid inputting large numbers for your class strength and number of subjects as the program will get tedious to complete.\nSuggested values for class strength and subjects is between 2 to 5 for both.\n\tThank You for you understanding!~")
            self.total_no=tkSimpleDialog.askinteger(self.ct_name+"\'s Profile~","Enter number of students of your class to input marks of - ")
            pop=tkMessageBox.showinfo("NOTICE!","Now the data will be inputed on python console to maintain simplicity.\n Thank you.")
            self.store_st_names()
    def password_store(self):
            print "\t","----------------------------------------------------------------"
            print "Kindly Enter Password. Whatever password you will type won't be visible for security purposes! \n"
            initial=getpass.getpass()
            print "Kindly Re-Enter your password~\n"
            password=getpass.getpass()
            if initial==password:
                x=open("meh.txt",'a')
                crypt=base64.b64encode(password)
                x.writelines(crypt+" ")
                x.close()                                    
            else:
                print "Your passwords did not match!!\nKindly re-run the program again!"
                p=open("Users.txt",'r')
                q=p.read()
                r=q.split()
                del r[-1]
                p.close()
                time.sleep(5)
                quit()
            self.capche()
    def password_check(self):
            os.chdir("C:\Users\Saket\Desktop\RM1")
            x=open("meh.txt",'r')
            y=x.read()
            z=y.split()
            print "\t","----------------------------------------------------------------"
            print "Kindly Enter your password - "
            r=getpass.getpass()
            k=base64.b64encode(r)
            flag=0
            for i in range(len(z)):
                if z[i]==k:
                    print "Access Granted!!\n WELCOME BACK!!"
                    flag=1
            if flag==0:
                    print "ACCESS DENIED\n\nWRONG PASSWORD!!\n\nQUITTING PROGRAM FOR SECURITY REASONS!KINDLY RESTART THE APPLICATION AGAIN!"
                    time.sleep(10)
                    quit()
            x.close()
            self.capche()
    def capche(self):
            c=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
            d=tkSimpleDialog.askstring("CAPCHE VERIFICATION!","Kindly enter the following case-sensitive Capche to prove you are not a robot -\n\n\t\t %s"%c)
            if d==c:
                print "\t","----------------------------------------------------------------"
                print "Verification Done!"
                print "\t","----------------------------------------------------------------"
            else:
                print "\t","----------------------------------------------------------------"
                print "YOU ENTERED THE WRONG CAPCHE!! YOU HAVE ONE LAST TRY!"
                c=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
                d=tkSimpleDialog.askstring("CAPCHE VERIFICATION!","Kindly enter the following case-sensitive Capche to prove you are not a robot -\n\n\t\t %s"%c)
                if d==c:
                    print "Verification Done!"
                    print "\t","----------------------------------------------------------------"
                else:
                    print "\t","----------------------------------------------------------------"
                    print "WRONG CAPCHE! ACCESS DENIED!CLOSING APPLICATION FOR SECURITY REASONS. KINDLY RETRY AGAIN!"
                    time.sleep(7)
                    quit()
    def store_st_names(self):
            #Making Dict1 for Storing Names of students
            self.name=[]     #LIST CONTAINING NAME OF STUDENTS
            self.roll=[]     #LIST CONTAINING NUMBER OF STUDENTS
            self.dnam={}
            print "\n","\t","KINDLY ENTER THE DETAILS OF YOUR STUDENTS - "
            time.sleep(1)
            for i in range(self.total_no):
                    self.student_name=raw_input("Please enter the name of the student no. %d - "%(i+1))
                    self.name+=[self.student_name,]
            self.name.sort()
            pop=tkMessageBox.showinfo("NOTICE!","All the names of the students have been arranged in ascending/alphabetc order!")
            for j in range(self.total_no):
                    self.dnam[j+1]=self.name[j]
                    self.roll+=[str(j+1),]
                    self.roll.sort()
            self.store_subjects()
    def store_subjects(self):                		
            #Making Dict2 for Storing Subjects of the class
            self.stream=tkSimpleDialog.askstring(self.ct_name+"\'s Profile~","Enter the stream of the class you teach - \n(Eg: Science, Medical Science, Humanities, Commerce,etc..)")
            self.no_subs=tkSimpleDialog.askinteger(self.ct_name+"\'s Profile~","Enter number of subjects in the stream - ")
            pop=tkMessageBox.showinfo("NOTICE!","Now values will be inputed in python instead of GUI Boxes for convienence!")
            self.subs=[]
            self.dsubs={}
            self.dsubs_roll=[]
            self.u=['st','nd','rd']
            self.a='th'
            self.c=len(self.u)
            print "\t","----------------------------------------------------------------"
            print "\n","\t","KINDLY ENTER THE SUBJECTS IN THE %s STREAM - "%self.stream.upper()
            time.sleep(1)
            for i in range(self.no_subs):   #ENTERING SUBJECTS
                    if self.c<self.no_subs:
                        self.u+=[self.a,]
                        self.c+=1
                    self.subjects=raw_input("Kindly enter name of %s%s subject - "%(str((i+1)),self.u[i]))
                    self.subs+=[self.subjects,]
                    self.dsubs[i+1]=self.subs[i]
                    self.dsubs_roll+=[str(i+1),]
                    self.dsubs_roll.sort()
            self.subject=list()
            self.subject+=self.subs
            self.m_subs=[]
            sp=" "
            self.maxi=tkSimpleDialog.askinteger(self.ct_name+"\'s Profile~","Enter MAXIMUM marks attainable on the test - ")
            self.outf=[]
            raw=[]
            for i in range(self.no_subs):              #CREATING MAIN LIST FOR SUBJECTS AND OUT OF
                self.outf+=[str(self.maxi),]
                while len(self.subs[i])!=15:
                    self.subs[i]+=sp
                self.m_subs+=[self.subs[i],]        
            self.marks_entry()
    def marks_entry(self):    #ENTERING MARKS
            RM1.a=self.no_subs
            time.sleep(1)
            print "\t","---------------------------------------------------------------"
            print "\n","\t","KINDLY INPUT THE MARKS OF THE STUDENTS NOW! - "
            p=0
            u=0
            self.n=self.total_no
            self.marks=[]
            self.t=self.ct_name
            while p!=self.n:       #CREATING LOG FILES
                k=0
                time.sleep(0.5)
                print "\n"," "*7,"Input %s\'s Marks - "%(self.name[u])
                time.sleep(0.5)
                while k!=RM1.a:
                    z=str(input("Enter marks of %s subject - "%(self.subject[k])))
                    if float(z)>int(self.outf[0]):
                        while int(self.outf[0])<float(z):
                            pop=tkMessageBox.showerror("ERROR!!","Marks inputted are more than the Max. Marks attainable!!.\n\t PLEASE TRY AGAIN!!")
                            z=str(input("Enter marks of %s subject - "%(self.subject[k])))
                    self.marks+=[z+" ",]
                    k+=1
                self.wk=open("%s\'s log%d.txt"%(self.t[0]+self.t[-1],u+1),'a')
                print "\n","\t","\t","-----------------------------------------------"
                self.wk.writelines(self.marks)
                self.marks=[]
                p+=1
                u+=1
                self.wk.close()
            self.wk.close()	  #COMPLETED MAKING LOG FILES
            done=tkMessageBox.showinfo("RESULT MASTER 1.0~","Thank you for inputting all the data.\nKindly wait till the output Report card is generated!")
            time.sleep(1)
            print "Calculating total percentage of each student... please wait..."
            time.sleep(1)
            print"DONE!!"
            print "\t","---------------------------------------------------------------"
            self.calc_Tmarks()
    def calc_Tmarks(self):
            zn=0
            for i in range(len(self.outf)):
                zn+=float(self.outf[i])
            k=0
            self.perc=0
            self.calc=[]
            prc=0
            self.t_perc=[]          #TOTAL PERCENTAGE LIST
            while k!=self.total_no:
                n=0
                f=open("%s\'s log%d.txt"%(self.ct_name[0]+self.ct_name[-1],k+1),'r')
                a=f.readline()
                b=a.split()
                while n!=len(self.outf):
                        self.calc+=b
                        prc+=float(self.calc[n])
                        self.perc=(prc/zn)*100.0
                        n+=1
                        self.calc=[]
                self.t_perc+=[str(self.perc),]
                k+=1
                prc=0
                f.close()   
            self.Date_Year()
    def Date_Year(self):
            self.meh=tkMessageBox.askyesno("NOTICE!~","Do you want to enter today\'s date or any other date?\nClick on YES to enter today\'s date or on NO to enter any other specific date on report card - ")
            t=time.localtime()
            self.year="%d-%d"%(t[0],t[0]+1)
            if self.meh==True:
                    self.dt="%d/%d/%d"%(t[2],t[1],t[0])
            if self.meh==False:
                    self.dt=tkSimpleDialog.askstring(self.ct_name+"\'s Profile~","Enter today\'s date seperated by back slashes (/) in following format - \'dd/mm/yyyy\'")
            self.Gen_File()
    def Gen_File(self):
            time.sleep(1)
            print "Generating Output file..."
            time.sleep(1)
            print "Please wait... generating Report card..."
            time.sleep(1)
            x=self.ct_name.split()
            se=" "
            if len(x)==1:
                self.f=open("%s\'s class report card.txt"%(x[0]),'a')
                kk=0
                k1=0
                k2=0
                while kk!=len(self.roll):
                    self.f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n"+"\n")
                    self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+" "+self.school_name.upper()+"\n")
                    self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+se*7+"REPORT CARD"+"\n")
                    self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+self.year+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"DATE : "+self.dt+"\n"+"\n")
                    self.f.writelines("\t"+"NAME OF STUDENT :  "+self.name[kk].upper()+"\n")
                    self.f.writelines("\t"+"CLASS : "+self.clas.upper()+"-"+self.sec.upper()+"\n"+"\t"+"ROLL NO. : "+self.roll[kk]+"\n")
                    self.f.writelines("\t"+"CLASS TEACHER : "+self.ct_name.upper()+"\n"+"\t"+"STREAM : "+self.stream.upper()+"\n"+"\n")
                    self.f.write("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"SUBJECT"+"\t"+"\t"+"\t"+"\t"+"MARKS"+"\t"+"\t"+"\t"+"OUT OF"+"\n"+"\n")
                    mh=open("%s\'s log%d.txt"%(self.ct_name[0]+self.ct_name[-1],kk+1),'r')
                    a=mh.readline()
                    b=a.split()
                    k1=0
                    while k1!=(len(self.subs)):
                            self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+self.m_subs[k1]+"\t"+"\t"+"\t"+" "+b[k1]+"\t"+"\t"+"\t"+" "+self.outf[k1]+"\n")
                            k1+=1
                    self.f.writelines("\n"+"\n"+"\t"+"TOTAL PERCENTAGE - "+self.t_perc[kk]+"%"+"\n"+"\n")        
                    kk+=1
                self.f.close()
                mh.close()
            if len(x)==2:
                self.f=open("%s\'s class report card.txt"%(x[0]+" "+x[-1]),'a')
                kk=0
                k1=0
                k2=0
                while kk!=len(self.roll):
                    self.f.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n"+"\n")
                    self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+" "+self.school_name.upper()+"\n")
                    self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+se*7+"REPORT CARD"+"\n")
                    self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+self.year+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"DATE : "+self.dt+"\n"+"\n")
                    self.f.writelines("\t"+"NAME OF STUDENT :  "+self.name[kk].upper()+"\n")
                    self.f.writelines("\t"+"CLASS : "+self.clas.upper()+"-"+self.sec.upper()+"\n"+"\t"+"ROLL NO. : "+self.roll[kk]+"\n")
                    self.f.writelines("\t"+"CLASS TEACHER : "+self.ct_name.upper()+"\n"+"\t"+"STREAM : "+self.stream.upper()+"\n"+"\n")
                    self.f.write("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"SUBJECT"+"\t"+"\t"+"\t"+"\t"+"MARKS"+"\t"+"\t"+"\t"+"OUT OF"+"\n"+"\n")
                    mh=open("%s\'s log%d.txt"%(self.ct_name[0]+self.ct_name[-1],kk+1),'r')
                    a=mh.readline()
                    b=a.split()
                    k1=0
                    while k1!=(len(self.subs)):
                            self.f.writelines("\t"+"\t"+"\t"+"\t"+"\t"+"\t"+"\t"+self.m_subs[k1]+"\t"+"\t"+"\t"+" "+b[k1]+"\t"+"\t"+"\t"+" "+self.outf[k1]+"\n")
                            k1+=1
                    self.f.writelines("\n"+"\n"+"\t"+"TOTAL PERCENTAGE - "+self.t_perc[kk]+"%"+"\n"+"\n")        
                    kk+=1
                self.f.close()
                mh.close()
            pop=tkMessageBox.showinfo("WOW!!","You have reached the end.\nTHANK YOU FOR USING REPORT MASTER 1.0.\nYour Report Card is ready!!\n\n\t\t ~ A work of Saket Savarn~")
            for i in range(self.total_no):
                    io=open("%s\'s log%d.txt"%(self.ct_name[0]+self.ct_name[-1],i+1),'r')
                    io.read()
                    io.close()
                    os.remove("%s\'s log%d.txt"%(self.ct_name[0]+self.ct_name[-1],i+1))   #DELETING LOG FILES
            self.opening()
    def opening(self):
            print "\t","----------------------------------------------------------------"
            time.sleep(1)
            print "Opening your final output of report card..."
            time.sleep(1)
            print "THANK YOU FOR USING \'REPORT MASTER 1.0~\'!! HERE IS YOUR OUTPUT FILE!! :D "
            qw=self.ct_name.split()
            if len(qw)==1:
                    os.startfile("%s\'s class report card.txt"%(qw[0]))
            if len(qw)==2:    
                    os.startfile("%s\'s class report card.txt"%(qw[0]+" "+qw[1]))                     
            self.ending()
    def ending(self):
            print "\t","++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
            print "REPORT MASTER 1.0~ is closing now..."
            time.sleep(2)
            print "Saving any remaining data... Closing..."
            time.sleep(4)
            print "Bye!!~ :D"
            time.sleep(0.75)
            quit()
                    
                                    


class results(RM1):
	time.sleep(1)
	print "\n","\n","\t","\t","---------------+REPORT MASTER 1.0+---------------","\n","\n"
	SaketIsCool=RM1()
