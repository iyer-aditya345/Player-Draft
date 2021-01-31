from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
from pil import ImageTk,Image
def draft():
    root=Tk()
    root.title("Draft")
    root.geometry('800x800')
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

    sflist=[ar1,ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9,ar10,ar11,ar12]
    pflist=[pf1,pf2,pf3,pf4,pf5,pf6,pf7,pf8,pf9,pf10,pf11,pf12]
    sglist=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12]
    centerlist=[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12]
    l3 = [im1, im2, im3, im4, im5, im6, im7, im8, im9, im10, im11,im12]
    x=im1.height()
    y=im1.width()
    k=ar11
    panel=Label(root,image=k)
    panel.pack(side="bottom", fill="both",expand="yes")
    sql = "select * from players where position='C' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))
    listc = l4[:12]
    nlist=[]
    sql = "select * from players where position='SG' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))
    listsg = l4[:12]

    nlist=[]
    pos=-1
    def myteam():
        global pos
        new = Toplevel(root)
        new.geometry('1000x900')
        img = Image.open("Courtn2.png")
        width,height=1000,1000
        img = img.resize((width,height), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(new, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        new.title("MY TEAM")
        frame_container = Frame(new)
        
        canvas_container = Canvas(frame_container, height=8000, width=1500)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        sql="select * from myteam"
        mycur.execute(sql)
        res=mycur.fetchall()
        name=[]
        index=[]
        for i in range(len(res)):
            name.append("\'{}\'".format(res[i][1]))
            index.append("\"{}\"".format(res[i][9]))
        imgs=[]
        l2 = []
        
        def change():
            global pos
            if j.get()==0:
                b2['state']='NORMAL'
                pos=0
            elif j.get()==1:
                b2['state']='NORMAL'
                pos=1
            elif j.get()==2:
                b2['state']='NORMAL'
                pos=2
            elif j.get()==3:
                b2['state']='NORMAL'
                pos=3
            elif j.get()==4:
                b2['state']='NORMAL'
                pos=4
        def dele():
            sql="""DELETE FROM myteam where Name = %s"""
            print(name)
            if pos==0:
                print(name[0],pos)
                mycur.execute(sql,(name[0],))
            if pos==1:
                print(name[1],pos)
                mycur.execute(sql,(name[1],))
            if pos==2:
                print(name[2],pos)
                mycur.execute(sql,(name[2],))
            if pos==3:
                print(name[3],pos)
                mycur.execute(sql,(name[3],))

            if pos==4:
                print(name[4],pos)
                mycur.execute(sql,(name[4],))
            db.commit()
            messagebox.showinfo("ALERT","This player has been removed,select a new player")
            new.destroy()
        for i in range(0,len(name)):
            name[i]=name[i].strip("\'")
        for i in index:
            i = i.strip('\"')
            imgs.append(ImageTk.PhotoImage(Image.open(i)))
        j=IntVar()
        for i in range(0,len(index)):
            l2.append(Radiobutton(new,variable=j,value=i,image=imgs[i],state=ACTIVE,command = change))
        
        try:
            l2[0].grid(row=2,column=1)
        except:
            pass
        try:
            l2[1].grid(row=2, column=200)
        except:
            pass
        try:
            l2[2].grid(row=10, column=5)
        except:
            pass
        try:
            l2[3].grid(row=30, column=1)
        except:
            pass
        try:
            l2[4].grid(row=30, column=200)
        except:
            pass
        
        def mainl():
            global RUN
            if len(name)<=4:
                messagebox.showerror("ERROR","You must select 5 players before proceeding")
                new.destroy()
            else:
                messagebox.showerror("READY","By pressing ok you will close the entire draft section and move to game. Press only if you are ready")
                new.destroy()
                root.destroy()
                RUN=True
        
            
            
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set, scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        b1=Button(new,text="Proceed", command=mainl)
        b1.place(x=800,y=350,height=50,width=150)
        b2=Button(new,text="Delete",state="disabled",command=dele)
        b2.place(x=800,y=550,height=50,width=150)        
        frame_container.pack()
        



    def sg():
        new2=Toplevel(root)
        new2.title("Shooting Guard")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def detect(val):
            print(val)
            if val.find('0')!= -1:
                
                return(0,1)
            elif val.find('1') != -1:
                return(0,3)
            elif val.find('2')!= -1:
                return(1,1)
            elif val.find('3')!= -1:
                return(1,3)
            elif val.find('4')!= -1:
                return(2,2)
        def clicked(value):
            print(detect(value))
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="SG":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='SG' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value[0]))
            else:
                messagebox.showerror("error", "You already have a Shooting Guard")
            new2.destroy()
        new2.grab_set()
        #new.grab_release()
        r=StringVar()
        
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
        
            l2.append(Radiobutton(frame2,variable=r,value=(listsg[i],i),command=lambda : clicked(r.get()),image=sglist[i]))

        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3,column=4)
        l2[11].grid(row=3, column=6)
        
        
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    sql = "select * from players where position = 'PF' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    listpf = []
    for i in range(len(l)):
        listpf.append("\'{}\'".format(l[i][1]))
    nlist=[]
    def pf():
        new2=Toplevel(root)
        new2.title("Power Forward")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def clicked(value):
            print(type(value))
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="PF":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='PF' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Power Forward")
            #new2.destroy()
        new2.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame2,variable=r,value=listpf[i],command=lambda : clicked(r.get()),image=pflist[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    def center():
        new2=Toplevel(root)
        new2.title("Center")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="C":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='C' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Center")
            new2.destroy()

        new2.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame2,variable=r,value=listc[i],command=lambda : clicked(r.get()),image=centerlist[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    sql = "select * from players where position = 'SF' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))

    listsf = l4[:12]
    nlist=[]
    def sf():
        new2=Toplevel(root)
        new2.title("Small Forward")
        frame_container = Frame(new2)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame2 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)  # will be visible if the frame2 is to to big for the canvas
        canvas_container.create_window((0, 0), window=frame2, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="SF":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='SF' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Small Forward")
            new2.destroy()

        new2.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame2, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame2,variable=r,value=listsf[i],command=lambda : clicked(r.get()),image=sflist[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)
        
        frame2.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()

    sql = "select * from players where position = 'PG' order by Overall desc"
    mycur.execute(sql)
    result = mycur.fetchall()
    l = list(result)
    l4 = []
    for i in range(len(l)):
        l4.append("\'{}\'".format(l[i][1]))

    l5 = l4[:12]
    nlist=[]

    def pg():
        new3=Toplevel(root)
        new3.title("Point Guard")
        frame_container = Frame(new3)
        canvas_container = Canvas(frame_container,height=850,width=1300)
        frame3 = Frame(canvas_container)
        myscrollbar = Scrollbar(frame_container, orient="vertical",command=canvas_container.yview)
        canvas_container.create_window((0, 0), window=frame3, anchor='nw')
        def clicked(value):
            sql2="select * from myteam"
            mycur.execute(sql2)
            res=mycur.fetchall()
            count=0
            for i in res:
                if i[2]=="PG":
                    count+=1
            if count<1:
                sql = "insert into myteam(Jersey_number,Name,Position,Overall,Shooting_Outside,Shooting_inside,Defense_outside,Defense_inside,Passing,image) select * from players where position='PG' and Name like {}".format(value)
                mycur.execute(sql)
                db.commit()
                messagebox.showinfo("new team member","{} is now in your team".format(value))
            else:
                messagebox.showerror("error", "You already have a Point Guard")
            new3.destroy()
        new3.grab_set()
        #new.grab_release()
        r=StringVar()
        bn=-1
        img = Image.open("Courtn2.png")
        img = img.resize((1300,1200), Image.ANTIALIAS)
        Img =  ImageTk.PhotoImage(img)
        background_label =Label(frame3, image=Img)
        background_label.Img = Img
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        l2=[]
        for i in range(0,12):
            l2.append(Radiobutton(frame3,variable=r,value=l5[i],command=lambda : clicked(r.get()),image=l3[i]))
        l2[0].grid(row=0,column=1)
        l2[1].grid(row=0,column=3)
        l2[2].grid(row=0, column=5)
        l2[3].grid(row=1, column=2)
        l2[4].grid(row=1, column=4)
        l2[5].grid(row=1, column=6)
        l2[6].grid(row=2, column=1)
        l2[7].grid(row=2, column=3)
        l2[8].grid(row=2, column=5)
        l2[9].grid(row=3, column=2)
        l2[10].grid(row=3, column=4)
        l2[11].grid(row=3, column=6)

        frame3.update()
        canvas_container.configure(yscrollcommand=myscrollbar.set,scrollregion="0 0 0 %s" % frame3.winfo_height())
        canvas_container.pack(side=RIGHT)
        myscrollbar.pack(side=RIGHT, fill=Y)
        frame_container.pack()
    
    pg=Button(root,text="Choose a Point Guard", command=pg)
    pg.place(x=90,y=90,height=50,width=150)
    center=Button(root,text="Choose a Center",command=center)
    center.place(x=325,y=390,height=50,width=150)
    sg=Button(root,text="Choose a Shooting Guard", command=sg)
    sg.place(x=90,y=700,height=50,width=150)
    sf=Button(root,text="Chose a Small Forward", command=sf)
    sf.place(x=600,y=90,height=50,width=150)
    pf=Button(root,text="Choose a Power Forward", command=pf)
    pf.place(x=600,y=700,height=50,width=150)
    MYTEAM=Button(root,text="Check your team", command=myteam)
    MYTEAM.place(x=330,y=600,height=50,width=150)
    root.deiconify()
root=Tk()
root.title("Welcome Page")
root.geometry('1000x1000')
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo 
def k():
    abox=messagebox.askquestion("Are you ready?","Press Yes to start the draft")
    if abox=="yes":
        root.destroy()
        draft()
def s():
    abox=messagebox.askquestion("Exit","Press Yes to exit game")
    if abox=="yes":
        root.destroy()
image = Image.open('courtn3.png')
photo = ImageTk.PhotoImage(image)
copy_of_image=image.copy()
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

root.iconphoto(False,photo)

a=Button(root,text="BEGIN GAME",command=k)
a.place(x=380,y=700,height=75,width=250)
n=Button(root,text="Quit",command=s)
n.place(x=850,y=900,height=50,width=75)
root.mainloop()
    
