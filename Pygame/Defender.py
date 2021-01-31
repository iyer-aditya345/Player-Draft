import pygame
import random
import math
from sys import exit
import warnings
warnings.filterwarnings("ignore")
pygame.init()
global offopp
offopp="pg"
pass1=True
pass2=True
pass3=True
pass4=True
pass1dur = random.randint(3,5)
pass2dur = random.randint(7,9)
pass3dur = random.randint(11,13)
pass4dur=  random.randint(15,17)
a1=random.randint(1,2)
a1=10

block=False
i = True
coord=[]
h1,L1,h2=0,0,0
status= 'DEFENSE'
if status == 'DEFENSE':
    b,b2=280,130
    count=0
    a=465
    
    while i:
        if a<285:
            break
        coord.append([a,b])
        coord.append([a,b2])
        if a==305:
            a-=5
        elif count>=5:
            a-=20
        else:
            a-=10
        b +=10
        b2 -=10
        count+=1
    def TP(x,y):
        TP= False
        if y==390:
            TP= True
        elif y==15:
            TP= True
        elif x>=285:
            TP= True
        for i in coord:
            if y<=130:
                if y==i[1] or y == i[1]-5 or y==i[1]+5:
                    if x>=i[0]:
                        TP=True
            elif y>=280:
                if y==i[1] or y == i[1]+5:
                    if x>=i[0]:
                        TP=True
        if TP==True:
            return True
def activeopp():
    if offopp=="pg":
        return o1
    elif offopp=="sg":
        return o2
    elif offopp=="sf":
        return o3
    elif offopp=="pf":
        return o4
    elif offopp=="c":
        return o5
def curplayer():
    if defplayer=="pg":
        return p1
    elif defplayer=="sg":
        return p2
    elif defplayer=="sf":
        return p3
    elif defplayer=="pf":
        return p4
    elif defplayer=="c":
        return p5
def collside(x1,x2,y1,y2): 
    global h1,L1,h2
    if x1>y1:
        if x2>y2:
            h1=1
            L1=1
            h2=-1
        else:
            h1=-1
            L1=1
            h2=1
    elif x1<y1:
        if x2>y2:
            h1=1
            L1=-1
            h2=1
        elif x2<y2:
            h1=-1
            L1=-1
            h2=1
        else:
            h2=-1
    else:
        if x2>y2:
            h1=1
            L1=1
        else:
            h1=-1
            L1=-1
    return [h1,L1]
def nonpcollide():
    global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
    global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y        
    
    if pygame.sprite.collide_rect(o1,o2):
        oy+=collside(ox,oy,o2x,o2y)[0]
        ox+=collside(ox,oy,o2x,o2y)[1]
    if pygame.sprite.collide_rect(o1,o3):
        oy+=collside(ox,oy,o3x,o3y)[0]
        ox+=collside(ox,oy,o3x,o3y)[1]
    if pygame.sprite.collide_rect(o1,o4):
        oy+=collside(ox,oy,o4x,o4y)[0]
        ox+=collside(ox,oy,o4x,o4y)[1]
    if pygame.sprite.collide_rect(o1,o5):
        oy+=collside(ox,oy,o5x,o5y)[0]
        ox+=collside(ox,oy,o5x,o5y)[1]
    if pygame.sprite.collide_rect(o3,o2):
        o3y+=collside(o3x,o3y,o2x,o2y)[0]
        o3x+=collside(o3x,o3y,o2x,o2y)[1] 
    if pygame.sprite.collide_rect(o4,o2):
        o4y+=collside(o4x,o4y,o2x,o2y)[0]
        o4x+=collside(o4x,o4y,o2x,o2y)[1]
    if pygame.sprite.collide_rect(o5,o2):
        o5y+=collside(o5x,o5y,o2x,o2y)[0]
        o5x+=collside(o5x,o5y,o2x,o2y)[1] 
    if pygame.sprite.collide_rect(o3,o4):
        o3y+=collside(o3x,o3y,o4x,o4y)[0]
        o3x+=collside(o3x,o3y,o4x,o4y)[1] 
    if pygame.sprite.collide_rect(o4,o5):
        o4y+=collside(o4x,o4y,o5x,o5y)[0]
        o4x+=collside(o4x,o4y,o5x,o5y)[1]
    if pygame.sprite.collide_rect(o3,o5):
        o3y+=collside(o3x,o3y,o5x,o5y)[0]
        o3x+=collside(o3x,o3y,o5x,o5y)[1]
    if pygame.sprite.collide_rect(o1,p1):
        oy+=collside(ox,oy,px,py)[0]
        ox+=collside(ox,oy,px,py)[1]
    if pygame.sprite.collide_rect(o1,p2):
        oy+=collside(ox,oy,p2x,p2y)[0]
        ox+=collside(ox,oy,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o1,p3):
        oy+=collside(ox,oy,p3x,p3y)[0]
        ox+=collside(ox,oy,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o1,p4):
        oy+=collside(ox,oy,p4x,p4y)[0]
        ox+=collside(ox,oy,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o1,p5):
        oy+=collside(ox,oy,p2x,p2y)[0]
        ox+=collside(ox,oy,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o2,p1):
        o2y+=collside(o2x,o2y,px,py)[0]
        o2x+=collside(o2x,o2y,px,py)[1]
    if pygame.sprite.collide_rect(o2,p2):
        o2y+=collside(o2x,o2y,p2x,p2y)[0]
        o2x+=collside(o2x,o2y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o2,p3):
        o2y+=collside(o2x,o2y,p3x,p3y)[0]
        o2x+=collside(o2x,o2y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o2,p4):
        o2y+=collside(o2x,o2y,p4x,p4y)[0]
        o2x+=collside(o2x,o2y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o2,p5):
        o2y+=collside(o2x,o2y,p5x,p5y)[0]
        o2x+=collside(o2x,o2y,p5x,p5y)[1]
    if pygame.sprite.collide_rect(o3,p1):
        o3y+=collside(o3x,o3y,px,py)[0]
        o3x+=collside(o3x,o3y,px,py)[1]
    if pygame.sprite.collide_rect(o3,p2):
        o3y+=collside(o3x,o3y,p2x,p2y)[0]
        o3x+=collside(o3x,o3y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o3,p3):
        o3y+=collside(o3x,o3y,p3x,p3y)[0]
        o3x+=collside(o3x,o3y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o3,p4):
        o3y+=collside(o3x,o3y,p4x,p4y)[0]
        o3x+=collside(o3x,o3y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o3,p5):
        o3y+=collside(o5x,o5y,p5x,p5y)[0]
        o3x+=collside(o5x,o5y,p5x,p5y)[1]
    if pygame.sprite.collide_rect(o4,p1):
        o4y+=collside(o4x,o4y,px,py)[0]
        o4x+=collside(o4x,o4y,px,py)[1]
    if pygame.sprite.collide_rect(o4,p2):
        o4y+=collside(o4x,o4y,p2x,p2y)[0]
        o4x+=collside(o4x,o4y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o4,p3):
        o4y+=collside(o4x,o4y,p3x,p3y)[0]
        o4x+=collside(o4x,o4y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o4,p4):
        o4y+=collside(o4x,o4y,p4x,p4y)[0]
        o4x+=collside(o4x,o4y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o4,p5):
        o4y+=collside(o4x,o4y,p5x,p5y)[0]
        o4x+=collside(o4x,o4y,p5x,p5y)[1]
    if pygame.sprite.collide_rect(o5,p1):
        o5y+=collside(o5x,o5y,px,py)[0]
        o5x+=collside(o5x,o5y,px,py)[1]
    if pygame.sprite.collide_rect(o5,p2):
        o5y+=collside(o5x,o5y,p2x,p2y)[0]
        o5x+=collside(o5x,o5y,p2x,p2y)[1]
    if pygame.sprite.collide_rect(o5,p3):
        o5y+=collside(o5x,o5y,p3x,p3y)[0]
        o5x+=collside(o5x,o5y,p3x,p3y)[1]
    if pygame.sprite.collide_rect(o5,p4):
        o5y+=collside(o5x,o5y,p4x,p4y)[0]
        o5x+=collside(o5x,o5y,p4x,p4y)[1]
    if pygame.sprite.collide_rect(o5,p5):
        o5y+=collside(o5x,o5y,p5x,p5y)[0]
        o5x+=collside(o5x,o5y,p5x,p5y)[1]
    if pygame.sprite.collide_rect(p1,p2):
        collside(px,py,p2x,p2y)
    if pygame.sprite.collide_rect(p1,p3):
        collside(px,py,p3x,p3y)
    if pygame.sprite.collide_rect(p1,p4):
        collside(px,py,p4x,p4y)
    if pygame.sprite.collide_rect(p1,p5):
        collside(px,py,p5x,p5y)  
    if pygame.sprite.collide_rect(p3,p2):
        collside(p2x,p2y,p3x,p3y) 
    if pygame.sprite.collide_rect(p4,p2):
        collside(p2x,p2y,p4x,p4y) 
    if pygame.sprite.collide_rect(p5,p2):
        collside(p2x,p2y,p5x,p5y) 
    if pygame.sprite.collide_rect(p3,p4):
        collside(p3x,p3y,p4x,p4y) 
    if pygame.sprite.collide_rect(p4,p5):
        collside(p4x,p4y,p5x,p5y) 
    if pygame.sprite.collide_rect(p3,p5):
        collside(p3x,p3y,p5x,p5y)
def coll2():
    global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
    if a1==1:
        if pygame.sprite.collide_rect(o1,o4):
            o4x-=3
        if pygame.sprite.collide_rect(o2,o4):
            o4x+=3
            o4y-=3
        if  pygame.sprite.collide_rect(o2,o1):
            o2x-=3
            o2y+=3
        if  pygame.sprite.collide_rect(o2,o3):
            o3y+=5
        if  pygame.sprite.collide_rect(o5,o4):
            o5y+=3
    elif a1==2:
        if  pygame.sprite.collide_rect(o1,o5):
            if seconds<=8:
                o5x+=3
            else:
                oy+=3
        if  pygame.sprite.collide_rect(o3,o5):
            o5x-=3
            o5y+=3
        if  pygame.sprite.collide_rect(o3,o1):
            o3x-=3
            oy-=3
    elif a1==5:
        if pygame.sprite.collide_rect(o2,o4):
            if seconds<=7:
                o4y+=3
            else:
                o4y-=3
        if  pygame.sprite.collide_rect(o1,o5):
            o5y-=3
    elif a1==6:
        if  pygame.sprite.collide_rect(o3,o5):
                    o5y-=3
    elif a1==8:
        if  pygame.sprite.collide_rect(o1,o4):
            o4x-=3
    elif a1==9:
        if  pygame.sprite.collide_rect(o2,o5):
            o5x-=3
    elif a1==10:
        if  pygame.sprite.collide_rect(o2,o3):
            o3x+=5
        if  pygame.sprite.collide_rect(o3,o4):
            o4x-=5
def boundforall():
    global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y 
    if px>=675:
        px=675
    if px<=30:
        px=30
    if py<=15:
        py=15
    if py>=390:
        py=390
    if p2x>=675:
        p2x=675
    if p2x<=30:
        p2x=30
    if p2y<=15:
        p2y=15
    if p2y>=390:
        p2y=390
    if p3x>=675:
        p3x=675
    if p3x<=30:
        p3x=30
    if p3y<=15:
        p3y=15
    if p3y>=390:
        p3y=390
    if p4x>=675:
        p4x=675
    if p4x<=30:
        p4x=30
    if p4y<=15:
        p4y=15
    if p4y>=390:
        p4y=390
    if p5x>=675:
        p5x=675
    if p5x<=30:
        p5x=30
    if p5y<=15:
        p5y=15
    if p5y>=390:
        p5y=390
def plymove(x1,y1,a,b):
    if x1>=350:
        if y1>200:
            x2=x1-60
            y2=y1-60
        elif y1<=200:
            x2=x1-60
            y2=y1+60
        else:
            x2=x1-60
            y2=y1
    elif x1<=350:
        if y1>200:
            x2=x1
            y2=y1-80
        elif y1<200:
            x2=x1
            y2=y1+80
        else:
            x2=x1-60
            y2=y1
    return [x2,y2]
class opponent(pygame.sprite.Sprite):
        def __init__(self,imagefile,x,y):
            super().__init__()
            pygame.sprite.Sprite.__init__(self)
            self.load=pygame.image.load(imagefile).convert()
            self.rect=self.load.get_rect()
            self.movex=0
            self.movey=0
            self.rect.x=x
            self.rect.y=y
            self.Z= 0
            self.shotprob,self.dis,self.defprob=0,0,0                
        def boundary(self):
            if self.rect.x>=675:
                self.rect.x=675
            if self.rect.x<=30:
                self.rect.x=30
            if self.rect.y<=15:
                self.rect.y=15
            if self.rect.y>=390:
                self.rect.y=390
        def oppmove(self, player):
            global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
            global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
            global fin
            hoopdis=math.dist([self.rect.x,self.rect.y],[65,202.5])
            if a1==1:
                ax,ay=405,80
                bx,by=85,15
                cx,cy=405,330
                dx,dy=330,200
                ex,ey=115,300
                a2x,a2y=310,250
                b2x,b2y=405,320
                c2x,c2y=85,390
                d2x,d2y=85,280
                e2x,e2y=185,155
            elif a1==2:
                ax,ay=400,330
                bx,by=400,80
                cx,cy=85,390
                dx,dy=105,120
                ex,ey=330,200
                a2x,a2y=305,160
                b2x,b2y=90,15
                c2x,c2y=400,80
                d2x,d2y=150,250
                e2x,e2y=90,120
            elif a1==3:
                ax,ay=85,390
                bx,by=85,20
                cx,cy=450,120
                dx,dy=270,280
                ex,ey=270,130
                a2x,a2y=85,330
                b2x,b2y=85,80
                c2x,c2y=330,200
                d2x,d2y=270,300
                e2x,e2y=270,110
            elif a1==4:
                ax,ay=85,20
                bx,by=465,200
                cx,cy=85,390
                dx,dy=240,280
                ex,ey=240,130
                a2x,a2y=85,80
                b2x,b2y=330,200
                c2x,c2y=85,330
                d2x,d2y=270,300
                e2x,e2y=270,110
                
            elif a1==5:
                ax,ay=185,300
                bx,by=130,100
                cx,cy=70,390
                dx,dy=390,80
                ex,ey=310,150
                a2x,a2y=325,220
                b2x,b2y=450,120
                c2x,c2y=270,30
                d2x,d2y=230,120
                e2x,e2y=130,250
            elif a1==6:
                ax,ay=205,120
                bx,by=90,15
                cx,cy=150,310
                dx,dy=310,240
                ex,ey=390,330
                a2x,a2y=325,180
                b2x,b2y=290,20
                c2x,c2y=390,340
                d2x,d2y=130,160
                e2x,e2y=230,290
            elif a1==7:
                ax,ay=160,390
                bx,by=250,120
                cx,cy=250,290
                dx,dy=110,15
                ex,ey=110,390
                a2x,a2y=265,390
                b2x,b2y=110,290
                c2x,c2y=110,110
                d2x,d2y=310,110
                e2x,e2y=310,290
            elif a1==8:
                ax,ay=160,20
                bx,by=250,120
                cx,cy=250,290
                dx,dy=110,15
                ex,ey=110,390
                a2x,a2y=265,15
                b2x,b2y=110,110
                c2x,c2y=110,290
                d2x,d2y=290,290
                e2x,e2y=290,110
            elif a1==9:
                ax,ay=305,280
                bx,by=85,390
                cx,cy=310,15
                dx,dy=390,200
                ex,ey=130,150
                a2x,a2y=125,320
                b2x,b2y=270,390
                c2x,c2y=465,195
                d2x,d2y=290,110
                e2x,e2y=90,90
            elif a1==10:
                ax,ay=305,120
                bx,by=350,390
                cx,cy=90,15
                dx,dy=150,250
                ex,ey=390,210
                a2x,a2y=145,80
                b2x,b2y=470,210
                c2x,c2y=305,15
                d2x,d2y=90,310
                e2x,e2y=310,290
            step=max(abs(ax-ox),abs(ay-oy))
            step2=max(abs(bx-o2x),abs(by-o2y))
            step3=max(abs(cx-o3x),abs(cy-o3y))
            step4=max(abs(dx-o4x),abs(dy-o4y))
            step5=max(abs(ex-o5x),abs(ey-o5y))
            step6=max(abs(a2x-ox),abs(a2y-oy))
            step7=max(abs(b2x-o2x),abs(b2y-o2y))
            step8=max(abs(c2x-o3x),abs(c2y-o3y))
            step9=max(abs(d2x-o4x),abs(d2y-o4y))
            step10=max(abs(e2x-o5x),abs(e2y-o5y))
            if fin==True:
                if math.dist([a2x,a2y],[ox,oy])<=3:
                    ox=a2x
                    oy=a2y
                    if math.dist([b2x,b2y],[o2x,o2y])<=3:
                        o2x=b2x
                        o2y=b2y
                        if math.dist([c2x,c2y],[o3x,o3y])<=3:
                            o3x=c2x
                            o3y=c2y
                            if math.dist([d2x,d2y],[o4x,o4y])<=3:
                                o4x=d2x
                                o4y=d2y
                                if math.dist([e2x,e2y],[o5x,o5y])<=3:
                                    o5x=e2x
                                    o5y=e2y
                                else:
                                    o5x+=((e2x-o5x)/step10)*1.7
                                    o5y+=((e2y-o5y)/step10)*1.7
                            else:
                                o4x+=((d2x-o4x)/step9)*1.7
                                o4y+=((d2y-o4y)/step9)*1.7
                        else:
                            o3x+=((c2x-o3x)/step8)*1.7
                            o3y+=((c2y-o3y)/step8)*1.7
                    else:
                        o2x+=((b2x-o2x)/step7)*1.7
                        o2y+=((b2y-o2y)/step7)*1.7
                else:
                    ox+=((a2x-ox)/step6)*1.7
                    oy+=((a2y-oy)/step6)*1.7
            else:
                if math.dist([ax,ay],[ox,oy])<=3:
                    ox=ax
                    oy=ay
                    if math.dist([bx,by],[o2x,o2y])<=3:
                        o2x=bx
                        o2y=by
                        if math.dist([cx,cy],[o3x,o3y])<=3:
                            o3x=cx
                            o3y=cy
                            if math.dist([dx,dy],[o4x,o4y])<=3:
                                o4x=dx
                                o4y=dy
                                if math.dist([ex,ey],[o5x,o5y])<=3:
                                    o5x=ex
                                    o5y=ey
                                    fin=True
                                else:
                                    o5x+=((ex-o5x)/step5)*1.7
                                    o5y+=((ey-o5y)/step5)*1.7
                            else:
                                o4x+=((dx-o4x)/step4)*1.7
                                o4y+=((dy-o4y)/step4)*1.7
                        else:
                            o3x+=((cx-o3x)/step3)*1.7
                            o3y+=((cy-o3y)/step3)*1.7
                    else:
                        o2x+=((bx-o2x)/step2)*1.7
                        o2y+=((by-o2y)/step2)*1.7
                else:
                    ox+=((ax-ox)/step)*1.7
                    oy+=((ay-oy)/step)*1.7
    
                    
        def activecoord(x):
                if x==o1:
                    z=[ox,oy]
                elif x==o3:
                    z=[o3x,o3y]
                elif x==o2:
                    z=[o2x,o2y]
                elif x==o4:
                    z=[o4x,o4y]
                elif x==o5:
                    z=[o5x,o5y]
                return z
        def opppass(self):
                global offopp,movement
                pos1=zpr[0]
                pos2=zpr[1]
                pos3=zpr[2]
                pos4=zpr[3]
                pos5=zpr[4]
                dis1=math.dist(opponent.activecoord(self),pos1)
                dis2=math.dist(opponent.activecoord(self),pos2)
                dis3=math.dist(opponent.activecoord(self),pos3)
                dis4=math.dist(opponent.activecoord(self),pos4)
                dis5=math.dist(opponent.activecoord(self),pos5)
                dislist=[dis1,dis2,dis3,dis4,dis5]
                dislist.sort()
                if dislist[1]==dis1:
                    prob1="pg"
                    moveloc=[ox,oy]
                if dislist[2]==dis1:
                    prob2="pg"
                    moveloc2=[ox,oy]
                if dislist[1]==dis2:
                    prob1="sg"
                    moveloc=[o2x,o2y]
                if dislist[2]==dis2:
                    prob2="sg"
                    moveloc2=[o2x,o2y]
                if dislist[1]==dis3:
                    prob1="sf"
                    moveloc=[o3x,o3y]
                if dislist[2]==dis3:
                    prob2="sf"
                    moveloc2=[o3x,o3y]
                if dislist[1]==dis4:
                    prob1="pf"
                    moveloc=[o4x,o4y]
                if dislist[2]==dis4:
                    prob2="pf"
                    moveloc2=[o4x,o4y]
                if dislist[1]==dis5:
                    prob1="c"
                    moveloc=[o5x,o5y]
                if dislist[2]==dis5:
                    prob2="c"
                    moveloc2=[o5x,o5y]
                    
                pprob=random.randint(1,10)
                if shoot==False:
                    if coll==False:
                        if pprob in range(1,7):
                            offopp=prob1
                            moveball=moveloc
                        else:
                            offopp=prob2
                            moveball=moveloc2
                            
                        if offopp=="pg":
                            ball.movement(b1,ox,oy)
                        elif offopp=="sg":
                            ball.movement(b1,o2x,o2y)
                        elif offopp=="sf":
                            ball.movement(b1,o3x,o3y)
                        elif offopp=="pf":
                            ball.movement(b1,o4x,o4y)
                        elif offopp=="c":
                            ball.movement(b1,o5x,o5y)
                        movement=False
                        print(offopp,prob1,prob2,moveball[0],moveball[1])
        def shot2(self,x,y,player):
            if TP(opponent.activecoord(self)[0],opponent.activecoord(self)[1]):
                self.K=True
            else:
                self.K=False
            
            if math.dist(opponent.activecoord(self),[65,202.5])<=100:
                self.dis=10
            elif math.dist(opponent.activecoord(self),[65,202.5])<=200 and math.dist(opponent.activecoord(self),[65,202.5])>100:
                self.dis=8
            elif math.dist(opponent.activecoord(self),[65,202.5])<=300 and math.dist(opponent.activecoord(self),[65,202.5])>200:
                self.dis=6
            elif math.dist(opponent.activecoord(self),[65,202.5])<=400 and math.dist(opponent.activecoord(self),[65,202.5])>300:
                self.dis=4
            elif math.dist(opponent.activecoord(self),[65,202.5])<=550 and math.dist(opponent.activecoord(self),[65,202.5])>400:
                self.dis=2
            else:
                self.dis=0
            if self.K:
                if x[1]-y[1]>=20:
                    self.shotprob=8 + random.randint(0,2)
                elif x[1]-y[1]>=15 and x[1]-y[1]<20:
                    self.shotprob=7 + random.randint(0,3)
                elif x[1]-y[1]>=10 and x[1]-y[1]<15:
                    self.shotprob=6 + random.randint(0,4)
                elif x[1]-y[1]>=7 and x[1]-y[1]<10:
                    self.shotprob=5 + random.randint(0,5)
                else:
                    self.shotprob=2+ random.randint(0,8)
            else:
                if x[0]-y[0]>=20:
                    self.shotprob=8 + random.randint(0,2)
                elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                    self.shotprob=7 + random.randint(0,3)
                elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                    self.shotprob=6 + random.randint(0,4)
                elif x[0]-y[0]>=7 and x[0]-y[0]<10:
                    self.shotprob=5 + random.randint(0,5)
                else:
                    self.shotprob=2+ random.randint(0,8)
            if  math.dist(opponent.activecoord(activeopp()),[player.rect.x,player.rect.y])<80:
                self.defprob=random.randint(1,10)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            blockprob=random.randint(1,2)
                            if blockprob==1:
                                block = True
                            else:
                                block = False 
            elif math.dist(opponent.activecoord(activeopp()),[player.rect.x,player.rect.y])<100 and  math.dist(opponent.activecoord(self),[player.rect.x,player.rect.y])>=80:
                    self.defprob=2+random.randint(0,8)
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_SPACE:
                                blockprob=random.randint(0,3)
                                if blockprob==1:
                                    block = True
                                else:
                                    block = False
            elif math.dist(opponent.activecoord(self),[player.rect.x,player.rect.y])>=100 and  math.dist(opponent.activecoord(self),[player.rect.x,player.rect.y])<120:
                self.defprob=4+random.randint(0,6)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            blockprob=random.randint(0,9)
                            if blockprob==1:
                                block = True
                            else:
                                block = False
            elif math.dist(opponent.activecoord(self),[player.rect.x,player.rect.y])>=120 and  math.dist(opponent.activecoord(self),[player.rect.x,player.rect.y])<140:
                self.defprob=6+random.randint(0,4)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            block = False
            else:
                self.defprob=8+random.randint(0,2)
                for event in pygame.event.get():
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            block = False
            self.Z=self.shotprob+self.defprob+self.dis
                
        def shot(self,x,y):
            global RUN
            if TP(opponent.activecoord(self)[0],opponent.activecoord(self)[1]):
                self.K=True
            else:
                self.K=False
        
            if math.dist(opponent.activecoord(activeopp()),player.activecoord(curplayer()))>=150:
                 if self.K:
                     if math.dist(opponent.activecoord(self),[65,202.5])<=450:
                              if x[1]-y[1]>=20:
                                  chance=random.randint(1,400)
                                  if chance == 1:
                                      opponent.shot2(activeopp(),valo,valp,curplayer())
                              elif x[1]-y[1]>=15 and x[1]-y[1]<20:
                                    chance = random.randint(1,500)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),valo,valp,curplayer())
                              elif x[1]-y[1]>=10 and x[1]-y[1]<15:
                                    chance = random.randint(1,600)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),valo,valp,curplayer())
                              elif x[1]-y[1]>=5 and x[1]-y[1]<10:
                                    chance = random.randint(1,700)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),valo,valp,curplayer())
                              else:
                                    chance = random.randint(1,800)
                                    if chance == 1:
                                      opponent.shot2(activeopp(),valo,valp,curplayer())
                    
                 elif self.K==False:
                    if math.dist(opponent.activecoord(self),[65,202.5])<=100:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,50)
                            if chance ==6:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            schance=random.randint(1,100)
                            if chance !=5:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,200)
                            if chance !=4:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=5 and x[0]-y[0]<10:
                            chance=random.randint(1,300)
                            if chance !=3:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        else:
                            chance=random.randint(1,400)
                            if chance !=2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                    elif math.dist(opponent.activecoord(self),[65,202.5])<=200 and math.dist(opponent.activecoord(self),[65,202.5])>100:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,100)
                            if chance ==5:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            schance=random.randint(1,200)
                            if chance !=4:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,300)
                            if chance !=3:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=5 and x[0]-y[0]<10:
                            schance=random.randint(1,400)
                            if chance !=2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        else:
                            chance=random.randint(1,500)
                            if chance ==1:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                    elif math.dist(opponent.activecoord(self),[65,202.5])<=300 and math.dist(opponent.activecoord(self),[65,202.5])>200:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,100)
                            if chance ==3:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            schance=random.randint(1,200)
                            if chance !=2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,300)
                            if chance ==2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=5 and x[0]-y[0]<10:
                            schance=random.randint(1,500)
                            if chance ==2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        else:
                            chance=random.randint(1,600)
                            if chance ==1:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                    elif math.dist(opponent.activecoord(self),[65,202.5])<=400 and math.dist(opponent.activecoord(self),[65,202.5])>300:
                        if x[0]-y[0]>=20:
                            chance=random.randint(1,300)
                            if chance ==5:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                            schance=random.randint(1,400)
                            if chance !=2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                            chance=random.randint(1,500)
                            if chance ==2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        elif x[0]-y[0]>=7 and x[0]-y[0]<10:
                            schance=random.randint(1,600)
                            if chance ==2:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
                        else:
                            chance=random.randint(1,700)
                            if chance ==1:
                                opponent.shot2(activeopp(),valo,valp,curplayer())
            
            if seconds==900000:
                RUN=False
        def score(self):
            global state,RUN,shoot,status,movement
            if status == 'DEFENSE':
                    opponent.shot(self,valo,valp)
            global F2
            score=0
            if TP(opponent.activecoord(self)[0],opponent.activecoord(self)[1]):
                self.K=True
            else:
                self.K=False
            if block==True:
                score =0
                state="b"
            
            elif self.Z>0:
                if movement==True:
                    if coll==False:
                        shoot=True
                        if self.Z>=23:
                            
                            if self.K:
                                score=3
                                state='3p'
                            else:
                                score = 2
                                state = '2p'
                            
                            
                        else:
                            state="M"
                            score=0
                        ball.movement(b1,cx,cy)
                        movement=False
                        print(self.Z,self.shotprob,self.defprob,self.dis,state)
                        status="PAUSE"
            if score>0:
                F2=True
            
            return score
        def win(self):
            if sc >=21:
                wintext= "YOU LOSE"
                winblit = winfont.render(wintext,True, [0,0,0], [155,0,0])
                s.blit(winblit,wincenter)
                wintext2="Exit window to close game"
                winblit2=winfont2.render(wintext2,True,[0,0,0],[155,0,0])
                s.blit(winblit2,wincenter2)
                return True
        def update(self):
            global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
            if shoot==False and status=="DEFENSE":
                    opponent.oppmove(self,curplayer())
            opponent.win(self)
            opponent.boundary(self)
            
            if self==o1:
                self.rect.x=ox
                self.rect.y=oy
                s.blit(f1,(ox,oy))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o2:
                self.rect.x=o2x
                self.rect.y=o2y
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o3:
                self.rect.x=o3x
                self.rect.y=o3y
                s.blit(f3,(o3x,o3y))
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y)) 
            elif self==o4:
                self.rect.x=o4x
                self.rect.y=o4y
                s.blit(f4,(o4x,o4y))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f1,(ox,oy))
                s.blit(f5,(o5x,o5y))
            elif self==o5:
                self.rect.x=o5x
                self.rect.y=o5y
                s.blit(f5,(o5x,o5y))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f1,(ox,oy))
class player(pygame.sprite.Sprite):
    def __init__(self,imagefile,x,y):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.load=pygame.image.load(imagefile).convert()
        self.movex=0
        self.movey=0
        self.rect=self.load.get_rect()
        self.rect.x=x
        self.rect.y=y
    def boundary(self):
        if status == 'DEFENSE':
            if self.rect.x>=675:
                self.rect.x=675
            if self.rect.x<=30:
                self.rect.x=30
            if self.rect.y<=15:
                self.rect.y=15
            if self.rect.y>=390:
                self.rect.y=390
    def activecoord(self):
        if self==p1:
            z=[px,py]
        elif self==p3:
            z=[p3x,p3y]
        elif self==p2:
            z=[p2x,p2y]
        elif self==p4:
            z=[p4x,p4y]
        elif self==p5:
            z=[p5x,p5y]
        return z
    def movement(self,x,y):
        self.movex += x
        self.movey +=y
    def update(self):
        global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y        
        self.rect.x+=self.movex
        self.rect.y+=self.movey
        
        if TP(player.activecoord(self)[0],player.activecoord(self)[1]):
                self.K=True
        else:
                self.K=False
        if defplayer=="pg":
            px=self.rect.x
            py=self.rect.y
            s.blit(l1,(px,py))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif defplayer=="sg":
            p2x=self.rect.x
            p2y=self.rect.y
            s.blit(l2,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif defplayer=="sf":
            p3x=self.rect.x
            p3y=self.rect.y
            s.blit(l3,(p3x,p3y))
            s.blit(l2,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif defplayer=="pf":
            p4x=self.rect.x
            p4y=self.rect.y
            s.blit(l4,(p4x,p4y))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l1,(px,py))
            s.blit(l5,(p5x,p5y))
        elif defplayer=="c":
            p5x=self.rect.x
            p5y=self.rect.y
            s.blit(l5,(p5x,p5y))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l1,(px,py))
class ball:
    def __init__(self,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.rad=10
        self.ballmovex,self.ballmovey=0,0
        self.screen=s
        self.state="P"
        self.number=0
    def boundary(self):
            if self.x>=675:
                self.x=675
            if self.x<=30:
                self.x=30
            if self.y<=15:
                self.y=15
            if self.y>=390:
                self.y=390
    def collision(self,x2,y2):
        if math.dist((self.x,self.y),(x2,y2))<20:
                self.ballmovex=0
                self.ballmovey=0
                return True
    def collisionb(self,x2,y2):
        if math.dist([self.x],[x2])<=10:
            if math.dist([self.y],[y2])<=5:
                self.ballmovex=0
                self.ballmovey=0
                return True
    def movement(self,x2,y2):
        global disfn
        self.number=max(abs(x2-self.x),abs(y2-self.y))
        self.ballmovex=float(x2-self.x)/self.number
        self.ballmovey=float(y2-self.y)/self.number
        self.state="M"
        if shoot==False:
            
            if math.dist((self.x,self.y),(x2,y2))<=100:
                disfn="T1"
            elif math.dist((self.x,self.y),(x2,y2))<=300 and math.dist((self.x,self.y),(x2,y2))>100:
                disfn="T2"
            else:
                disfn="T3"
        else:
            disfn="T0"
    def draw(self):
        global shoot,movement,status,coll
        if shoot==False:
            if self.state=="M":
                if ball.collision(self,px,py):
                    self.state="D1"
                    coll=True
                elif ball.collision(self,p2x,p2y):
                    self.state="D2"
                    coll=True
                elif ball.collision(self,p3x,p3y):
                    self.state="D3"
                    coll=True
                elif ball.collision(self,p4x,p4y):
                    self.state="D4"
                    coll=True
                elif ball.collision(self,p5x,p5y):
                    self.state="D5"
                    coll=True
                    
            if ball.collision(self,ox,oy) or ball.collision(self,o2x,o2y) or ball.collision(self,o3x,o3y) or ball.collision(self,o4x,o4y)or ball.collision(self,o5x,o5y) :
                self.state="P"
                movement=True
        if ball.collisionb(self,cx,cy):
            shoot=True
            self.x=90
            self.y=220
                
        ball.boundary(self)
        if self.state=="M":
            if disfn=="T1":
                fx=1.5
            elif disfn=="T2":
                fx=2
            elif disfn=="T0":
                fx=3
            else:
                fx=3
            self.x+=self.ballmovex*fx
            self.y+=self.ballmovey*fx            
        elif self.state=="P":
            if offopp=="pg":
                self.x=ox
                self.y=oy+20
            elif offopp=="sg":
                self.x=o2x
                self.y=o2y+20
            elif offopp=="sf":
                self.x=o3x
                self.y=o3y+20
                
            elif offopp=="pf":
                self.x=o4x
                self.y=o4y+20
            elif offopp=="c":
                self.x=o5x
                self.y=o5y+20
        else:
            if self.state=="D1":
                self.x=px
                self.y=py+20
            elif self.state=="D2":
                self.x=p2x
                self.y=p2y+20
            elif self.state=="D3":
                self.x=p3x
                self.y=p3y+20
            elif self.state=="D4":
                self.x=p4x
                self.y=p4y+20
            elif self.state=="D5":
                self.x=p5x
                self.y=p5y+20
            tst=fontst.render(itext,True, [0,0,0], [155,0,0])
            s.blit(tst,icenter)
            
        pygame.draw.circle(s,(255,140,0),[self.x,self.y],self.rad)       
RUN= True
scp=0
s=pygame.display.set_mode([1450,800])
defplayer="pg"
if status == "DEFENSE":
    px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y=405,200,285,90,285,320,85,160,85,255
    ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y=675,200,365,35,370,370,145,120,145,290
l1=pygame.image.load("ply.png").convert()
l2=pygame.image.load("ply2.png").convert()
l3=pygame.image.load("ply3.png").convert()
l4=pygame.image.load("ply4.png").convert()
l5=pygame.image.load("ply5.png").convert()
f1=pygame.image.load("opp.png").convert()
f2=pygame.image.load("opp2.png").convert()
f3=pygame.image.load("opp3.png").convert()
f4=pygame.image.load("opp4.png").convert()
f5=pygame.image.load("opp5.png").convert()
fontdef=pygame.font.get_fonts()[23]
fontdef2=pygame.font.get_fonts()[3]
fontdef3=pygame.font.get_fonts()[0]
font=pygame.font.SysFont(fontdef,30)
mtext="MISS!"
thptext="3 POINTER MADE!"
tptext="2 POINTER MADE!"
bltext="BLOCKED!"
itext="INTERCEPTED"
mcenter=(665,40)
tpcenter=(540,40)
blcenter=(620,40)
state="P"
fontdefst=pygame.font.get_fonts()[12]
fontst=pygame.font.SysFont(fontdefst,50)
thpcenter=(540,40)
icenter=(585,40)
coll=False
textcenter = (660,450)
winfont=pygame.font.SysFont(fontdef2,90)
winfont2=pygame.font.SysFont(fontdef3,30)
wincenter=(570,500)
wincenter2=(568,590)
count2=True
shoot1=False
movement=True
cx,cy=65,200
tcenter=(1180,450)
move=True
tfont=pygame.font.SysFont(fontdef3,30)
pygame.display.set_caption("Swisheroo")    
b=pygame.image.load("Courtn2.png").convert()
icon=pygame.image.load("icon2.jpeg").convert()
fontdef3=pygame.font.get_fonts()[0]
tfont=pygame.font.SysFont(fontdef3,30)
pygame.display.set_icon(icon)
img1=pygame.image.load("PG1.png").convert()
img2=pygame.image.load("SG.png").convert()
img3=pygame.image.load("PG2.png").convert()
img4,img5=pygame.image.load("PF.png").convert(),pygame.image.load("C.png").convert()
tcenter=(1180,450)
valo=[90,80]
opplist=["sg","sf","pf","c"]
opplistog=[]
valp=[30,40]
sc=0
b1=ball(ox+200,oy+40)
shoot=False
fin=False
pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))
start_ticks=pygame.time.get_ticks()
status= 'DEFENSE'
while RUN:
    s.fill([0,0,0])
    F2=False
    s.blit(b,(0,0))
    s.blit(img1,(0,520))
    s.blit(img2,(312,520))
    s.blit(img3,(624,520))
    s.blit(img4,(936,520))
    s.blit(img5,(1250,520))
    p1=player("ply.png",px ,py)
    p2=player("ply2.png",p2x,p2y)    
    p3=player("ply3.png",p3x,p3y)
    p4=player("ply4.png",p4x,p4y)
    p5=player("ply5.png",p5x,p5y)
    o1=opponent("opp.png",ox,oy)
    o2=opponent("opp2.png",o2x,o2y)
    o3=opponent("opp3.png",o3x,o3y)
    o4=opponent("opp4.png",o4x,o4y)
    o5=opponent("opp5.png",o5x,o5y)
    nonpcollide()
    player.boundary(p1)
    player.boundary(p2)
    player.boundary(p3)
    player.boundary(p4)
    player.boundary(p5)
    boundforall()
    scoretxt="Score is " + str(sc)
    zpr=[[ox,oy],[o2x,o2y],[o3x,o3y],[o4x,o4y],[o5x,o5y]]
    text = font.render(scoretxt,True, [155,0,0], [0,0,0])
    seconds=(pygame.time.get_ticks()-start_ticks)//1000
    s.blit(text,textcenter)
    coll2()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                                
            elif event.type == pygame.KEYDOWN:
                    if shoot==False:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_a:                  
                                player.movement(curplayer(),-20,0)
                            elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:        
                                    player.movement(curplayer(),20,0)
                            elif event.key == pygame.K_UP or event.key==pygame.K_w:
                                    player.movement(curplayer(),0,-20)
                            elif event.key== pygame.K_DOWN or event.key==pygame.K_s:
                                    player.movement(curplayer(),0,20)
                            elif event.key == pygame.K_1:
                                        defplayer="pg"
                            elif event.key == pygame.K_2:
                                        defplayer="sg"
                            elif event.key == pygame.K_3:
                                        defplayer="sf"
                            elif event.key == pygame.K_4:
                                        defplayer="pf"
                            elif event.key == pygame.K_5:
                                        defplayer="c"
                            elif event.key == pygame.K_SPACE:
                                print(movement)
    
    if state=="M":
        tst=fontst.render(mtext,True, [0,0,0], [155,0,0])
        s.blit(tst,mcenter)
    elif state=="2p":
        tst=fontst.render(tptext,True, [0,0,0], [155,0,0])
        s.blit(tst,tpcenter)
    elif state=="3p":
        tst=fontst.render(thptext,True, [0,0,0], [155,0,0])
        s.blit(tst,thpcenter)
    elif state=="B":
        tst=fontst.render(bltext,True, [0,0,0], [155,0,0])
        s.blit(tst,blcenter)                    
    sc+=opponent.score(activeopp())
    if pass1:
        if seconds==pass1dur:
            opponent.opppass(activeopp())
            pass1=False
    if pass2:
        if seconds==pass2dur:
            opponent.opppass(activeopp())
            pass2=False
    if pass3:
        if seconds==pass3dur:
            opponent.opppass(activeopp())
            pass3=False
    if pass4:
        if seconds==pass4dur:
            opponent.opppass(activeopp())
            pass4=False
    if state=="M":
        tst=fontst.render(mtext,True, [0,0,0], [155,0,0])
        s.blit(tst,mcenter)
    elif state=="2p":
        tst=fontst.render(tptext,True, [0,0,0], [155,0,0])
        s.blit(tst,tpcenter)
    elif state=="3p":
        tst=fontst.render(thptext,True, [0,0,0], [155,0,0])
        s.blit(tst,thpcenter)
    elif state=="B":
        tst=fontst.render(bltext,True, [0,0,0], [155,0,0])
        s.blit(tst,blcenter)
    tleft="Time Left is : " + str(20-seconds)
    tblit = tfont.render(tleft,True, [155,0,0], [0,0,0])
    s.blit(tblit,tcenter)
    player.update(curplayer())
    opponent.update(activeopp())
    ball.draw(b1)
    if seconds>90000:
        RUN= False
        move=False
    pygame.display.update()
    if RUN== False:
        pygame.quit()
