from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from pil import ImageTk,Image
import sys,random,pygame

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
    
img = Image.open("Courtn2.png")
width,height=800,800
img = img.resize((width,height), Image.ANTIALIAS)
Img =  ImageTk.PhotoImage(img)
background_label =Label(root, image=Img)
background_label.Img = Img

background_label.place(x=0, y=0, relwidth=1, relheight=1)
db=mysql.connector.connect(host='localhost',database='project',user='root',password='Agasthya0112')
mycur=db.cursor()

sql = "select * from myteam order by rand()" #to make the players in the table randomized
c2=0
mycur.execute(sql)

result = mycur.fetchall() #fetching the values

l = list(result)#to get it in tuple form

teamlist=[] #list that stores all the names of the players

for i in range(len(l)):
    
    teamlist.append("\'{}\'".format(l[i][1]))
for i in range(0,len(teamlist)):
    x=teamlist[i].strip("'")
    teamlist[i]=x
nlist=[] #list that stores all the loctaions of the players i.e player image
for i in range(len(l)):
    
    nlist.append(l[i][11])

klist=[]
screenlist=[]
for i in range(0,5):
    screenlist.append((l[i][1],l[i][12]))
for i in l:
    klist.append(i[11])
r=StringVar()
def draft_screen():
    global screenlist
    root.withdraw()
    new = Toplevel(root)
    new.geometry('1000x900')
    img = Image.open("Courtn2.png")
    width,height=1000,1000
    img = img.resize((width,height), Image.ANTIALIAS)
    Img =  ImageTk.PhotoImage(img)
    background_label =Label(new, image=Img)
    background_label.Img = Img
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    new.title("SELECT TEAM")
    
    frame_container = Frame(new)
    
    canvas_container = Canvas(frame_container, height=800, width=1500)
    frame2 = Frame(canvas_container)
    myscrollbar = Scrollbar(frame_container, orient="vertical",
                            command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
    canvas_container.create_window((0, 0), window=frame2, anchor='nw')
    
    def detect(val): #returns the cordinate of the selected player
        if val.find('0')!=-1: #explain after clicking the button
            return "r1"       # basicaly meant for indentifying which button is clicked out of those 5
        elif val.find('1')!=-1: # if true it shall show the grid of the buttons
            return "r2"
        elif val.find('2')!=-1:
            return "r3"
        elif val.find('3')!=-1:
            return "r4"
        elif val.find('4')!=-1:
            return "r5"
                   

    def clicked(value):
        global c2
        for i,c in enumerate(value):
            if c.isdigit():
                pos=i
        x=value[:(pos-1)]
        x=str('"')+x+str('"')
        sql2="select * from newteam" #team being the dummy table to store the players
        exists=False
        mycur.execute(sql2)
        nm=[]
        res=mycur.fetchall()
        for i in res:
            nm.append(i[1])
        name=x.strip('"')
        if name in nm:
            exists=True
        
        lx =[]
        if len(res)<=4:
            z=messagebox.askyesno("new team member","{} is now in your team".format(x)+str("  Are you sure about this"))
            if exists==False:
                if z==True:
                    sql = "insert into newteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image,points,img1,cost) select * from myteam where Name={}".format(x)
                    mycur.execute(sql)
                    
                    db.commit()
                    lx=[]
                    x=detect(value)
                    
                    if x=="r1":
                        r1.config(value=(teamlist[c2+5]+" 0"),image=eval(klist[c2+5]))
                        screenlist.pop(0)
                        for i in l:
                            if i[1]==teamlist[c2+5]:
                                newc=i[12]
                        screenlist.insert(0,(teamlist[c2+5],newc))
                    elif x=="r2":
                        r2.config(value=(teamlist[c2+5]+" 1"),image=eval(klist[c2+5]))
                        screenlist.pop(1)
                        for i in l:
                            if i[1]==teamlist[c2+5]:
                                newc=i[12]
                        screenlist.insert(1,(teamlist[c2+5],newc))
                    elif x=="r3":
                        r3.config(value=(teamlist[c2+5]+" 2"),image=eval(klist[c2+5]))
                        screenlist.pop(2)
                        for i in l:
                            if i[1]==teamlist[c2+5]:
                                newc=i[12]
                        screenlist.insert(2,(teamlist[c2+5],newc))
                    elif x=="r4":
                        r4.config(value=(teamlist[c2+5]+" 3"),image=eval(klist[c2+5]))
                        screenlist.pop(3)
                        for i in l:
                            if i[1]==teamlist[c2+5]:
                                newc=i[12]
                        screenlist.insert(3,(teamlist[c2+5],newc))
                    elif x=="r5":
                        r5.config(value=(teamlist[c2+5]+" 4"),image=eval(klist[c2+5]))
                        screenlist.pop(4)
                        for i in l:
                            if i[1]==teamlist[c2+5]:
                                newc=i[12]
                        screenlist.insert(4,(teamlist[c2+5],newc))
                    c2+=1
                
            else:

                messagebox.showerror("Error","You have selected this player already")
                
    
            
        else:
            messagebox.showerror("Error","You have already selected 5 players")
            

        
            

    new.grab_set()
    labels=[]
    
    def view2():
        labels2=[]
        new4=Toplevel(new)
        new4.geometry("500x500")
        new4.configure(background="black")
        for i in range(0,len(screenlist)):
            labels2.append(tk.Label(new4,bg="black",font="Cambria 17", fg="red", text=str(str(screenlist[i][0])+" - "+str(screenlist[i][1]))))
            labels2[i].place(x=100,y=50+(80*i))
        new4.after(10000,lambda:new4.destroy())
        
    def view():
        new3=Toplevel(new)
        new3.geometry("800x800")
        new3.configure(background="black")
        sql="select * from myteam"
        mycur.execute(sql)
        res=mycur.fetchall()
        del labels[:]
        for i in range(0,len(res)):
            
            labels.append(tk.Label(new3,bg="black",font="Cambria 15",fg="red",text=str(str(res[i][1])+" - "+str(res[i][12]))))
            if i<=25:
                labels[i].place(x=10,y=10+(30*i))

            elif i>25 and i<=51:
                labels[i].place(x=250,y=10+(30*(i-26)))
            else:
                labels[i].place(x=500,y=10+(30*(i-52)))
    def calculator():
        new3=Toplevel(new)
        new3.geometry("500x500")
        new3.configure(background="black")
        sql="select * from newteam"
        mycur.execute(sql)
        res=mycur.fetchall()
        totalcost=0
        plycost=[]
        for i in res:
            totalcost+=i[12]
            plycost.append((i[1],i[12]))
        remainder=5000-totalcost
        frame_container = Frame(new3)
    
        canvas_container = Canvas(frame_container, height=800, width=1500)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",
                                command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        tk.Label(new3,text="Budget=5000",font="Cambria 25",fg="red",bg="Black",pady=25).pack()
        tk.Label(new3,text="Remaining cost ="+str(remainder),fg="red",bg="Black",font="Cambria 25",pady=15).pack()
        var,var2,var3,var4,var5=StringVar(),StringVar(),StringVar(),StringVar(),StringVar()
        try:
            tk.Label(new3,textvariable=var,font="Cambria 20",fg="red",bg="black",anchor="c",pady=15).pack()
            var.set(str(plycost[0][0])+" - "+str(plycost[0][1]))
        except:
            var.set("No Player Selected")
        try:
            tk.Label(new3,textvariable=var2,font="Cambria 20",fg="red",bg="black",pady=15).pack()
            var2.set(str(plycost[1][0])+" - "+str(plycost[1][1]))
        except:
            var2.set("No Player Selected")
        try:
            tk.Label(new3,textvariable=var3,font="Cambria 20",fg="red",bg="black",pady=15).pack()
            var3.set(str(plycost[2][0])+" - "+str(plycost[2][1]))
        except:
            var3.set("No Player Selected")
        try:
            tk.Label(new3,textvariable=var4,font="Cambria 20",fg="red",bg="black",pady=15).pack()
            var4.set(str(plycost[3][0])+" - "+str(plycost[3][1]))
        except:
            var4.set("No Player Selected")
        try:
            tk.Label(new3,textvariable=var5,font="Cambria 20",fg="red",bg="black",pady=15).pack()
            var5.set(str(plycost[4][0])+" - "+str(plycost[4][1]))
        except:
            var5.set("No Player Selected")
        frame2.update()


    r1=Radiobutton(new,variable=r,value=(teamlist[0]+" 0"),command=lambda:clicked(r.get()),image=eval(klist[0]))
    r2=Radiobutton(new,variable=r,value=(teamlist[1]+" 1"),command=lambda:clicked(r.get()),image=eval(klist[1]))
    r3=Radiobutton(new,variable=r,value=(teamlist[2]+" 2"),command=lambda:clicked(r.get()),image=eval(klist[2]))
    r4=Radiobutton(new,variable=r,value=(teamlist[3]+" 3"),command=lambda:clicked(r.get()),image=eval(klist[3]))
    r5=Radiobutton(new,variable=r,value=(teamlist[4]+" 4"),command=lambda:clicked(r.get()),image=eval(klist[4]))

    
    r1.grid(row=2,column=1)

    r2.grid(row=2,column=200)

    r3.grid(row=10, column=5)

    r4.grid(row=30, column=1)

    r5.grid(row=30, column=200)
    frame2.update()
    canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height())
    canvas_container.pack(side=RIGHT)
    myscrollbar.pack(side=RIGHT, fill=Y)
    b1=Button(new,text="Calculate Remaining Costs", command=calculator)
    b1.place(x=800,y=150,height=50,width=150)
    b2=Button(new,text="View Costs of All Players",command=view)
    b2.place(x=800,y=350,height=50,width=150)
    b3=Button(new,text="View Costs of Players on Screen",command=view2)
    b3.place(x=780,y=550,height=75,width=200)
    frame_container.pack()





    

b2=Button(root,text="Proceed",command=draft_screen)
b2.place(x=330,y=500,height=50,width=150)  

    
