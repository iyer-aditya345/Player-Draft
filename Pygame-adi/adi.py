from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from pil import ImageTk,Image
import sys,random

def draft():
    global im3,a3,pf6,i2,ar3,i11,im7,count
    root=Tk()
    
    root.title("Draft")
    root.geometry('800x800')
    im1 = ImageTk.PhotoImage(Image.open("stephcurry.png"))
    im2 = ImageTk.PhotoImage(Image.open("russelwestbrook.png"))
    im3 = ImageTk.PhotoImage(Image.open("kyrieirving.png"))
    im4 = ImageTk.PhotoImage(Image.open("chrispaul.png"))
    im5 = ImageTk.PhotoImage(Image.open("damianlillard.png"))
    im6 = ImageTk.PhotoImage(Image.open("kembawalker.png"))
    im7 = ImageTk.PhotoImage(Image.open("traeyoung.png"))
    im8 = ImageTk.PhotoImage(Image.open("bensimmons.png"))
    im9 = ImageTk.PhotoImage(Image.open("deaaronfox.png"))
    im10 = ImageTk.PhotoImage(Image.open("kylelowry.png"))
    im11 = ImageTk.PhotoImage(Image.open("jamorant.png"))
    im12=ImageTk.PhotoImage(Image.open("dangelorussel.png"))

    i1 = ImageTk.PhotoImage(Image.open("joelembid.png"))
    i2 = ImageTk.PhotoImage(Image.open("nikolajokic.png"))
    i3 = ImageTk.PhotoImage(Image.open("karlanthonytowns.png"))
    i4 = ImageTk.PhotoImage(Image.open("rudygobert.png"))
    i5 = ImageTk.PhotoImage(Image.open("hassanwhiteside.png"))
    i6 = ImageTk.PhotoImage(Image.open("kristapsporzingis.png"))
    i7 = ImageTk.PhotoImage(Image.open("bamadebayo.png"))
    i8 = ImageTk.PhotoImage(Image.open("clintcapela.png"))
    i9=ImageTk.PhotoImage(Image.open("nikolavucevic.png"))
    i10=ImageTk.PhotoImage(Image.open("stevenadams.png"))
    i11=ImageTk.PhotoImage(Image.open("andredrummond.png"))
    i12=ImageTk.PhotoImage(Image.open("montrezlharrel.png"))

    a1 = ImageTk.PhotoImage(Image.open('jamesharden.png'))
    a2 = ImageTk.PhotoImage(Image.open("lukadoncic.png"))
    a3 = ImageTk.PhotoImage(Image.open("paulgeorge.png"))
    a4 = ImageTk.PhotoImage(Image.open("bradleybeal.png"))
    a5 = ImageTk.PhotoImage(Image.open("klaythompson.png"))
    a6 = ImageTk.PhotoImage(Image.open("devinbooker.png"))
    a7 = ImageTk.PhotoImage(Image.open("cjmcollum.png"))
    a8 = ImageTk.PhotoImage(Image.open("donovanmitchell.png"))
    a9 = ImageTk.PhotoImage(Image.open("victoroladipo.png"))
    a10 = ImageTk.PhotoImage(Image.open("zachlavine.png"))
    a11 = ImageTk.PhotoImage(Image.open("jaylenbrown.png"))
    a12 = ImageTk.PhotoImage(Image.open("shaigalexander.png"))

    pf1 = ImageTk.PhotoImage(Image.open('gantetokounmpo.png'))
    pf2 = ImageTk.PhotoImage(Image.open("anthonydavis.png"))
    pf3 = ImageTk.PhotoImage(Image.open("pascalsiakam.png"))
    pf4 = ImageTk.PhotoImage(Image.open("jaysontatum.png"))
    pf5 = ImageTk.PhotoImage(Image.open("zionwilliamson.png"))
    pf6 = ImageTk.PhotoImage(Image.open("johncollins.png"))
    pf7 = ImageTk.PhotoImage(Image.open("blakegriffin.png"))
    pf8 = ImageTk.PhotoImage(Image.open("domantassabonis.png"))
    pf9 = ImageTk.PhotoImage(Image.open("danilogallinari.png"))
    pf10 = ImageTk.PhotoImage(Image.open("jarenjacksonjr.png"))
    pf11 = ImageTk.PhotoImage(Image.open("alhorford.png"))
    pf12 = ImageTk.PhotoImage(Image.open("kevinlove.png"))

    ar1 = ImageTk.PhotoImage(Image.open('lebronjames.png'))
    ar2 = ImageTk.PhotoImage(Image.open("kevindurant.png"))
    ar3 = ImageTk.PhotoImage(Image.open("kawhileonard.png"))
    ar4 = ImageTk.PhotoImage(Image.open("jimmybutler.png"))
    ar5 = ImageTk.PhotoImage(Image.open("khrismiddleton.png"))
    ar6 = ImageTk.PhotoImage(Image.open("demarderozan.png"))
    ar7 = ImageTk.PhotoImage(Image.open("brandoningram.png"))
    ar8 = ImageTk.PhotoImage(Image.open("tobiasharris.png"))
    ar9 = ImageTk.PhotoImage(Image.open("gordonhayward.png"))
    ar10 = ImageTk.PhotoImage(Image.open("andrewwiggins.png"))
    ar11 = ImageTk.PhotoImage(Image.open("tjwarren.png"))
    ar12 = ImageTk.PhotoImage(Image.open("jonathanisaac.png"))
    plylist=[im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10,ar11,ar12,pf1,pf2,pf3,pf4,pf5,pf6,pf7,pf8,pf9,pf10,pf11,pf12,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]
        
        
    width=800
    height=800
    img = Image.open("Courtn2.png")
    width,height=800,800
    img = img.resize((width,height), Image.ANTIALIAS)
    Img =  ImageTk.PhotoImage(img)
    background_label =Label(root, image=Img)
    background_label.Img = Img
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    db=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
    mycur=db.cursor()
    
    
    plylist=[im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10,ar11,ar12,pf1,pf2,pf3,pf4,pf5,pf6,pf7,pf8,pf9,pf10,pf11,pf12,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]
    k2=random.choices(plylist,k=5)
    
    
    sql = "select * from myteam order by rand()" #to make the players in the table randomized

    mycur.execute(sql)

    result = mycur.fetchall() #fetching the values

    l = list(result)#to get it in tuple form

    teamlist=[] #list that stores all the names of the players

    for i in range(len(l)):

        teamlist.append(["\'{}\'".format(l[i][1]),i])
    for i in range(0,len(teamlist)):
        
        x=teamlist[i][0].strip("'")
        teamlist[i][0]=x
    nlist=[] #list that stores all the loctaions of the players i.e player image
    for i in range(len(l)):
        
        nlist.append(l[i][11])
    
    klist=[]
    for i in l:
        klist.append(i[11])
    klist.append("im7")
    count=0
    def draft_screen():
           
        root.withdraw()
        new2=Toplevel(root)
        new2.title("Shooting Guard")
        new2.title("Draft Screen")
        new2.geometry('800x800')
        width=800
        height=800
        img = Image.open("Courtn2.png")
        width,height=800,800
        img = img.resize((width,height), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(new2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        frame_container = Frame(new2)

        canvas_container = Canvas(frame_container,height=8000,width=1500)

        frame2 = Frame(canvas_container)

        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas

        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def detect(val): #returns the cordinate of the selected player
            if val.find('0')!=-1: #explain after clicking the button
                return (0,1)       # basicaly meant for indentifying which button is clicked out of those 5
            elif val.find('1')!=-1: # if true it shall show the grid of the buttons
                return (0,3)
            elif val.find('2')!=-1:
                return (0,5)
            elif val.find('3')!=-1:
                return (1,2)
            elif val.find('4')!=-1:
                return (1,4)
                       

            
        def clicked(value):#when thebutton is clicked
            global count
            pos=value.find("}")
            x=value[1:pos]
            x=str('"')+x+str('"')
            row,col=detect(value)[0],detect(value)[1]
            sql2="select * from newteam" #team being the dummy table to store the players

            mycur.execute(sql2)

            res=mycur.fetchall()

             #initializing count to be 0
            c2=0
            while count<1 and len(res)<=4: #count of the player shown at once
                print(count)
                z=messagebox.askyesno("new team member","{} is now in your team".format(x)+str("  Are you sure about this"))
                if z==True:
                    sql = "insert into newteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image,points,img1) select * from myteam where Name={}".format(x)
                    count+=1
                    mycur.execute(sql)
                    
                    db.commit()
                    
        
                l =[]
                for i in range(c2+5,c2+6): #since count will be 0 and at once we are showing 5 players
                    print(klist[i])
                    l.append(Radiobutton(frame2,variable=r,value=teamlist[i],command=clicked(r.get()),image=eval(klist[i])))
                      #this changes the picture of the radiobutton
                l[0].grid(row=row,column=col)
                

            else:

                messagebox.showerror("error","Error")
                

        new2.grab_set()
        r=StringVar()

        img = Image.open("Courtn2.png")

        img = img.resize((1300,1200), Image.ANTIALIAS) #to outsource

        Img =  ImageTk.PhotoImage(img)

        background_label =Label(frame2, image=Img)

        background_label.Img = Img

        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        

        l2=[]
        def no():
            print("PDPD")
        
        
        for i in range(0,5):
            l2.append(Radiobutton(frame2,variable=r,value=teamlist[i],command=lambda:clicked(r.get()),image=eval(klist[i])))
                     #initial button layout i.e shows 5 initial buttons

        l2[0].grid(row=0,column=1)

        l2[1].grid(row=0,column=3)

        l2[2].grid(row=0, column=5)

        l2[3].grid(row=1, column=2)

        l2[4].grid(row=1, column=4)
        
        
     
        frame2.update() #updating the initial screen by new players

        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())

        canvas_container.pack(side=RIGHT)

        myscrollbar.pack(side=RIGHT, fill=Y)

        frame_container.pack()





        
    '''b1=Button(root,text="Proceed", command=mainl)
    b1.place(x=800,y=350,height=50,width=150)'''
    b2=Button(root,text="Proceed",command=draft_screen)
    b2.place(x=330,y=500,height=50,width=150)  
    
draft()
        
