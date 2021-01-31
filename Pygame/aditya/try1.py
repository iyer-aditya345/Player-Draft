
from tkinter import *

from tkinter import ttk

from tkinter.ttk import *

from tkinter import messagebox

import mysql.connector

from pil import ImageTk,Image

root=Tk() #initial window page

root.title("Select you player")

root.geometry('800x800')

width=800

height=800

img = Image.open("Courtn2.png")

width,height=800,800

img = img.resize((width,height), Image.ANTIALIAS)

Img = ImageTk.PhotoImage(img)

background_label =Label(root, image=Img)

background_label.Img = Img

background_label.place(x=0, y=0, relwidth=2, relheight=1)

mydb=mysql.connector.connect(host='localhost',database='project',password='Agassthya0112')
mycur=db.cursor()

i1 = ImageTk.PhotoImage(Image.open("tosend_stephcurry.png"))

i2 = ImageTk.PhotoImage(Image.open("tosend_russelwestbrook.png"))

i3 = ImageTk.PhotoImage(Image.open("tosend_kyrieirving.png"))

i4 = ImageTk.PhotoImage(Image.open("tosend_chrispaul.png"))

i5 = ImageTk.PhotoImage(Image.open("tosend_damianlillard.png"))

     

       
i6 = ImageTk.PhotoImage(Image.open("tosend_jamesharden.png"))

i7 = ImageTk.PhotoImage(Image.open("tosend_lukadoncic.png"))

i8 = ImageTk.PhotoImage(Image.open("tosend_paulgeorge.png"))

i9 = ImageTk.PhotoImage(Image.open("tosend_bradleybeal.png"))

i10 = ImageTk.PhotoImage(Image.open("tosend_klaythompson.png"))

   
i11 = ImageTk.PhotoImage(Image.open("tosend_gantetokounmpo.png"))

i12 = ImageTk.PhotoImage(Image.open("tosend_anthonydavis.png"))

i13 = ImageTk.PhotoImage(Image.open("tosend_pascalsiakam.png"))

   
i14 = ImageTk.PhotoImage(Image.open("tosend_danilogallinari.png"))

i15 = ImageTk.PhotoImage(Image.open("tosend_jarenjacksonjr.png"))

i16 = ImageTk.PhotoImage(Image.open("tosend_alhorford.png"))

i17 = ImageTk.PhotoImage(Image.open("tosend_kevinlove.png"))

 

i18 = ImageTk.PhotoImage(Image.open("tosend_lebronjames.png"))

i19 = ImageTk.PhotoImage(Image.open("tosend_kevindurant.png"))

i20 = ImageTk.PhotoImage(Image.open("tosend_kawhileonard.png"))

     

teamlist = [i1, i2 ,i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20]

x=im1.height()

y=im1.width()

l = list(result)

sql = "select * from player order by rand()" #to make the players in the table randomized

mycur.execute(sql)

result = mycur.fetchall() #fetching the values

l = list(result)#to get it in tuple form

teamlist=[] #list that stores all the names of the players

for i in range(len(l)):

    teamlist.append("\'{}\'".format(l[i][1]))

nlist=[] #list that stores all the loctaions of the players i.e player image
for i in range(len(l)):
    nlist.append("\'{}\'".format(l[i][9]) )#meant to remove all backslashes
                    

def team():#the table where all the players are stored

    new2=Toplevel(root)

    new2.title("team") # title of the page

    frame_container = Frame(new2)

    canvas_container = Canvas(frame_container,height=850,width=1300)

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
        row,col=detect(value)[0],detect(value)[1]
        sql2="select * from team" #team being the dummy table to store the players

        mycur.execute(sql2)

        res=mycur.fetchall()

        count=0 #initializing count to be 0

    
        if count<5: #count of the player shown at once

            sql = "insert into team(jersey_number integer , player_name VARCHAR(255),overall integer, shooting integer, defense integer, offence integer, passing integer,image) select * from player and Name like {}".format(value)

            mycur.execute(sql)

            db.commit()

            messagebox.showinfo("new team member","{} is now in your team".format(value[0]))
            l =[]
            for i in range(count+5,count+6): #since count will be 0 and at once we are showing 5 players
                l.append(Radiobutton(frame2,variable=r,value=teamlist[i],command=clicked(r.get()),image=nlist[i]))
                    #this changes the picture of the radiobutton
            l.grid(row=row,column=col)
                

        else:

            messagebox.showerror("error")

            new2.destroy() #to destroy the page ad create another one

    r=StringVar()

    img = Image.open("Courtn2.png")

    img = img.resize((1300,1200), Image.ANTIALIAS) #to outsource

    Img =  ImageTk.PhotoImage(img)

    background_label =Label(frame2, image=Img)

    background_label.Img = Img

    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    l2=[]

    for i in range(0,5):

        l2.append(Radiobutton(frame2,variable=r,value=(teamlist[i],i),command=clicked(r.get()),image=nlist[i]))
                    #initial button layout i.e shows 5 initial buttons

    l2[0].grid(row=0,column=1)

    l2[1].grid(row=0,column=3)

    l2[2].grid(row=0, column=5)

    l2[3].grid(row=1, column=2)

    l2[4].grid(row=1, column=4)

    
    frame2.update() #updating the initial screen by new players

    canvas_container.configure(myscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())

    canvas_container.pack(side=RIGHT)

    myscrollbar.pack(side=RIGHT, fill=Y)

    frame_container.pack()


