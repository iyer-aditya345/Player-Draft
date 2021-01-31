import pygame
import math
import random
import warnings
warnings.filterwarnings("ignore")
from sys import exit
pygame.init()
i=True
vel = 10
coord=[]
vel = 2
width = 64
height = 64
up = False
player1 = True
player2 = False
down = False
jumpCount = 10
left = False
right = False
walkCount = 0
a=945
b,b2=280,130
stat1="P"
count=0
while i:
    if a>1105:
        break
    coord.append([a,b])
    coord.append([a,b2])
    if a==1095:
        a+=5
    elif count>=5:
        a+=20
    else:
        a+=10
    b+=10
    b2-=10
    count+=1    
def TP(x,y):
    TP= False
    if y==390:
        TP= True
    elif y==15:
        TP= True
    elif x<=940:
        TP= True
    for i in coord:
        if y<=130:
            if y==i[1] or y == i[1]-5 or y==i[1]+5:
                if x<=i[0]:
                    TP=True
        elif y>=280:
            if y==i[1] or y == i[1]+5:
                if x<=i[0]:
                    TP=True
    if TP==True:
        return True    
    
def activedefender():
    z=player.activecoord(useplayer())
    b=min(math.dist(z,[ox,oy]),math.dist(z,[o2x,o2y]),math.dist(z,[o3x,o3y]),math.dist(z,[o4x,o4y]),math.dist(z,[o5x,o5y]))
    if b==math.dist(z,[ox,oy]):
        return o1
    elif b==math.dist(z,[o2x,o2y]):
        return o2
    elif b==math.dist(z,[o3x,o3y]):
        return o3
    elif b==math.dist(z,[o4x,o4y]):
        return o4
    else:
        return o5
def useplayer():
    if activeplayer=="pg":
        return p1
    elif activeplayer=="sg":
        return p2
    elif activeplayer=="sf":
        return p3
    elif activeplayer=="pf":
        return p4
    elif activeplayer=="c":
        return p5
    
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
        def boundary(self):

            if self.rect.x>=1365:
                self.rect.x=1365
            if self.rect.x<=725:
                self.rect.x=725
            if self.rect.y<=15:
                self.rect.y=15
            if self.rect.y>=390:
                self.rect.y=390
        def activecoord(self):
            if self==o1:
                z=[ox,oy]
            elif self==o3:
                z=[o3x,o3y]
            elif self==o2:
                z=[o2x,o2y]
            elif self==o4:
                z=[o4x,o4y]
            elif self==o5:
                z=[o5x,o5y]
            return z 
        def move_towards_player(self, player):
            dx=0
            dy=0
            if math.dist([player.rect.x,player.rect.y],[self.rect.x,self.rect.y]) <400:
                step=max(abs(player.rect.x-self.rect.x),abs(player.rect.y-self.rect.y))
                dx+=float(player.rect.x-self.rect.x)/step
                dy+=float(player.rect.y-self.rect.y)/step
            if math.dist([player.rect.x,player.rect.y],[self.rect.x,self.rect.y])<=25:
                dx=0
                dy=0
            self.rect.x += (dx*2/3) 
            self.rect.y += (dy*2/3)
            
        def update(self):
            self=activedefender()
            if shoot!=True:
                opponent.move_towards_player(self,useplayer())

            opponent.boundary(self)
            global ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y
            if self==o1:
                oy=self.rect.y
                ox=self.rect.x
                s.blit(f1,(ox,oy))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o2:
                o2y=self.rect.y
                o2x=self.rect.x
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f3,(o3x,o3y))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o3:
                o3y=self.rect.y
                o3x=self.rect.x
                s.blit(f3,(o3x,o3y))
                s.blit(f2,(o2x,o2y))
                s.blit(f1,(ox,oy))
                s.blit(f4,(o4x,o4y))
                s.blit(f5,(o5x,o5y))
            elif self==o4:
                o4y=self.rect.y
                o4x=self.rect.x
                s.blit(f4,(o4x,o4y))
                s.blit(f2,(o2x,o2y))
                s.blit(f3,(o3x,o3y))
                s.blit(f1,(ox,oy))
                s.blit(f5,(o5x,o5y))
            elif self==o5:
                o5y=self.rect.y
                o5x=self.rect.x
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
        self.state=True
        self.score=0
    def boundary(self):
        if self.rect.x>=1365:
            self.rect.x=1365
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
    
    def collide(self,y,x2,y2):
        if pygame.sprite.collide_rect(self,y):
            if self.rect.x <x2:
                self.movex=-20
            elif self.rect.x>x2:
                self.movex=20
            if self.rect.y<y2:
                self.movey=-20
            elif self.rect.y>y2:
                self.movey=20
    
    def movement(self,x,y):
        self.movex += x
        self.movey +=y
        player.collide(self,o1,ox,oy)
        player.collide(self,o2,o2x,o2y)
        player.collide(self,o3,o3x,o3y)
        player.collide(self,o4,o4x,o4y)
        player.collide(self,o5,o5x,o5y)
        if activeplayer=="pg":
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p4,p4x,p4y)
            player.collide(self,p5,p5x,p5y)
        elif activeplayer=="sg":
            player.collide(self,p1,px,py)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p4,p4x,p4y)
            player.collide(self,p5,p5x,p5y)
        elif activeplayer=="sf":
            player.collide(self,p1,px,py)
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p4,p4x,p4y)
            player.collide(self,p5,p5x,p5y)
        elif activeplayer=="pf":
            player.collide(self,p1,px,py)
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p5,p5x,p5y)
        else:
            player.collide(self,p1,px,py)
            player.collide(self,p2,p2x,p2y)
            player.collide(self,p3,p3x,p3y)
            player.collide(self,p4,p4x,p4y)
            
    def shot(self,x,y,opponent):
        shotprob=0
        if TP(player.activecoord(useplayer())[0],player.activecoord(useplayer())[1]):
            self.K=True
        else:
            self.K=False
        if math.dist(player.activecoord(useplayer()),[1331,202.5])<=100:
            dis=10
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=200 and math.dist(player.activecoord(useplayer()),[1331,202.5])>100:
            dis=8
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=300 and math.dist(player.activecoord(useplayer()),[1331,202.5])>200:
            dis=6
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=400 and math.dist(player.activecoord(useplayer()),[1331,202.5])>300:
            dis=4
        elif math.dist(player.activecoord(useplayer()),[1331,202.5])<=550 and math.dist(player.activecoord(useplayer()),[1331,202.5])>400:
            dis=2
        else:
            dis=0
        if self.K:
            if x[1]-y[1]>=20:
                shotprob=8 + random.randint(0,2)
            elif x[1]-y[1]>=15 and x[1]-y[1]<20:
                shotprob=7 + random.randint(0,3)
            elif x[1]-y[1]>=10 and x[1]-y[1]<15:
                shotprob=6 + random.randint(0,4)
            elif x[1]-y[1]>=7 and x[1]-y[1]<10:
                shotprob=5 + random.randint(0,5)
            else:
                shotprob=2+ random.randint(0,8)
        else:
            if x[0]-y[0]>=20:
                shotprob=8 + random.randint(0,2)
            elif x[0]-y[0]>=15 and x[0]-y[0]<20:
                shotprob=7 + random.randint(0,3)
            elif x[0]-y[0]>=10 and x[0]-y[0]<15:
                shotprob=6 + random.randint(0,4)
            elif x[0]-y[0]>=7 and x[0]-y[0]<10:
                shotprob=5 + random.randint(0,5)
            else:
                shotprob=2+ random.randint(0,8)
        if  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<80:
            blockprob=random.randint(0,1)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
            
            defprob=random.randint(0,10)
        elif math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<100 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=80:
            defprob=2+random.randint(0,8)
            blockprob=random.randint(0,3)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
        elif  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=100 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<120:
            defprob=4+random.randint(0,6)
            blockprob=random.randint(0,9)
            if blockprob==1:
                self.block= True
            else:
                self.block=False
        elif  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])>=120 and  math.dist(player.activecoord(useplayer()),[opponent.rect.x,opponent.rect.y])<=140:
            self.block = False
            defprob=6+random.randint(0,4)
        else:
            self.block = False
            defprob=8+random.randint(0,2)
        self.shotchance= shotprob+defprob+dis
        print(self.shotchance,shotprob,defprob,dis)
    def score(self):
        global stat1
        if self.block==True:
            self.score =0
            stat1="B"
        if self.shotchance>=23:
            if self.K:
                stat1="3p"
                self.score=3
            else:
                self.score =2
                stat1="2p"
        elif self.shotchance<23:
            stat1="M"
            self.score=0
        shoot= True
        return self.score
    def win(self):
        if score >=21:
            wintext= "YOU WIN"
            winblit = winfont.render(wintext,True, [0,0,0], [155,0,0])
            s.blit(winblit,wincenter)
            wintext2="Exit window to close game"
            winblit2=winfont2.render(wintext2,True,[0,0,0],[155,0,0])
            s.blit(winblit2,wincenter2)
            self.movey=0
            self.movex=0
            return True
    def update(self):
        global px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y
        player.win(self)
        print(self.rect.x,self.rect.y)
        if TP(player.activecoord(useplayer())[0],player.activecoord(useplayer())[1]):
            self.K=True
        else:
            self.K=False
        if shoot== False:
            self.rect.x+=self.movex
            self.rect.y+=self.movey
        player.boundary(self)
        global L
        L = [self.rect.x,self.rect.y]
        if activeplayer=="pg":
            px=self.rect.x
            py=self.rect.y
            s.blit(l1,(px,py))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="sg":
            p2x=self.rect.x
            p2y=self.rect.y
            s.blit(l2,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l3,(p3x,p3y))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="sf":
            p3x=self.rect.x
            p3y=self.rect.y
            s.blit(l3,(p3x,p3y))
            s.blit(l2,(p2x,p2y))
            s.blit(l1,(px,py))
            s.blit(l4,(p4x,p4y))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="pf":
            p4x=self.rect.x
            p4y=self.rect.y
            s.blit(l4,(p4x,p4y))
            s.blit(l2,(p2x,p2y))
            s.blit(l3,(p3x,p3y))
            s.blit(l1,(px,py))
            s.blit(l5,(p5x,p5y))
        elif activeplayer=="c":
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
        if self.x>=1365:
            self.x=1365
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
    def movement(self,x2,y2):
        global disfn
        self.number=max(abs(x2-self.x),abs(y2-self.y))
        self.ballmovex=float(x2-self.x)/self.number
        self.ballmovey=float(y2-self.y)/self.number
        self.state="M"
        if math.dist((self.x,self.y),(x2,y2))<=100:
            disfn="T1"
        elif math.dist((self.x,self.y),(x2,y2))<=300 and math.dist((self.x,self.y),(x2,y2))>100:
            disfn="T2"
        else:
            disfn="T3"
            
    def draw(self):
        global shoot
        if shoot == False:
            if self.state=="M":
                if ball.collision(self,ox,oy):
                    self.state="D1"
                elif ball.collision(self,o2x,o2y):
                    self.state="D2"
                elif ball.collision(self,o3x,o3y):
                    self.state="D3"
                elif ball.collision(self,o4x,o4y):
                    self.state="D4"
                elif ball.collision(self,o5x,o5y):
                    self.state="D5"
            if ball.collision(self,px,py) or ball.collision(self,p2x,p2y) or ball.collision(self,p3x,p3y) or ball.collision(self,p4x,p4y)or ball.collision(self,p5x,p5y) :
                self.state="P"
        else:
            ball.collision(self,cx,cy)
        ball.boundary(self)
        if self.state=="M":
            if disfn=="T1":
                fx=1.5
            elif disfn=="T2":
                fx=2
            else:
                fx=3
            self.x+=self.ballmovex*fx
            self.y+=self.ballmovey*fx
        elif self.state=="P":
            if activeplayer=="pg":
                self.x=px+50
                self.y=py+20
            elif activeplayer=="sg":
                self.x=p2x+50
                self.y=p2y+20
            elif activeplayer=="sf":
                self.x=p3x+50
                self.y=p3y+20
            elif activeplayer=="pf":
                self.x=p4x+50
                self.y=p4y+20
            elif activeplayer=="c":
                self.x=p5x+50
                self.y=p5y+20
        else:
            if self.state=="D1":
                self.x=ox
                self.y=oy
            elif self.state=="D2":
                self.x=o2x
                self.y=o2y
            elif self.state=="D3":
                self.x=o3x
                self.y=o3y
            elif self.state=="D4":
                self.x=o4x
                self.y=o4y
            elif self.state=="D5":
                self.x=o5x
                self.y=o5y
            tst=fontst.render(itext,True, [0,0,0], [155,0,0])
            s.blit(tst,icenter)
            
        pygame.draw.circle(s,(255,140,0),[self.x,self.y],self.rad)
def curval():
    if activedefender()==o1:
        return valo1
    elif activedefender()==o2:
        return valo2
    elif activedefender()==o3:
        return valo3
    elif activedefender()==o4:
        return valo4
    elif activedefender()==o5:
        return valo5

    
RUN=True
score=0
pause=False
fontdef=pygame.font.get_fonts()[23]
fontdef2=pygame.font.get_fonts()[3]
fontdef3=pygame.font.get_fonts()[0]
fontdefst=pygame.font.get_fonts()[12]
font=pygame.font.SysFont(fontdef,30) 
textcenter = (660,450)
winfont=pygame.font.SysFont(fontdef2,90)
winfont2=pygame.font.SysFont(fontdef3,30)
tfont=pygame.font.SysFont(fontdef3,30)
s=pygame.display.set_mode([1450,800])
fontst=pygame.font.SysFont(fontdefst,50)
mtext="MISS!"
thptext="3 POINTER MADE!"
tptext="2 POINTER MADE!"
bltext="BLOCKED!"
itext="INTERCEPTED"
wincenter=(570,500)
wincenter2=(568,590)
tcenter=(1180,450)
activeplayer="pg"
pygame.init()
mcenter=(665,40)
tpcenter=(540,40)
blcenter=(620,40)
thpcenter=(540,40)
img1=pygame.image.load("PG1.png").convert()
img2=pygame.image.load("SG.png").convert()
img3=pygame.image.load("PG2.png").convert()
img4,img5=pygame.image.load("PF.png").convert(),pygame.image.load("C.png").convert()
icenter=(585,40)
valp1=[97,90]
valp2=[94,90]
valp3=[45,100]
valp4=[95,89]
valp5=[77,33]
coord=[]
valo=[40,60]
px,py,p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y=725,200,1050,40,1050,360,1250,120,1250,290
ox,oy,o2x,o2y,o3x,o3y,o4x,o4y,o5x,o5y=925,200,1100,90,1100,320,1300,120,1300,255
cx,cy=1375,225
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
pygame.display.set_caption("Swisheroo")    
b=pygame.image.load("Courtn2.png").convert()
icon=pygame.image.load("icon2.jpeg").convert()
pygame.display.set_icon(icon)
b1=ball(px,py)
kpr="pg"
shoot= False
start_ticks=pygame.time.get_ticks()
while RUN:
    s.fill([0,0,0])
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
    scoretxt="Score is " + str(score)
    text = font.render(scoretxt,True, [155,0,0], [0,0,0])
    s.blit(text,textcenter)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                                
            elif event.type == pygame.KEYDOWN:
                    if shoot==False:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_a:                  
                                player.movement(useplayer(),-20,0)
                        elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:        
                                player.movement(useplayer(),20,0)
                        elif event.key == pygame.K_UP or event.key==pygame.K_w:
                                player.movement(useplayer(),0,-20)
                        elif event.key== pygame.K_DOWN or event.key==pygame.K_s:
                                player.movement(useplayer(),0,20)
                        elif event.key == pygame.K_1:
                                if activeplayer!="pg":
                                    ball.movement(b1,px,py)
                                    activeplayer="pg"
                                    kpr="pg"
                        elif event.key == pygame.K_2:
                                if activeplayer!="sg":
                                    ball.movement(b1,p2x,p2y)
                                    activeplayer="sg"
                                    kpr="sg"
                        elif event.key == pygame.K_3:
                                if activeplayer!="sf":
                                    ball.movement(b1,p3x,p3y)
                                    activeplayer="sf"
                                    kpr="sf"
                        elif event.key == pygame.K_4:
                                if activeplayer!="pf":
                                    ball.movement(b1,p4x,p4y)
                                    activeplayer="pf"
                                    kpr="pf"
                        elif event.key == pygame.K_5:
                                if activeplayer!="c":
                                    ball.movement(b1,p5x,p5y)
                                    activeplayer="c"
                                    kpr="c"
                        if event.key == pygame.K_SPACE:
                                print(player.activecoord(useplayer()))
                                
                                shoot=True
                                ball.movement(b1,cx,cy)
                                activeplayer=kpr
                                if score<21:
                                    if activeplayer=="pg":
                                            player.shot(useplayer(),valp1,curval(),activedefender())
                                    elif activeplayer=="sg":
                                            player.shot(useplayer(),valp2,curval(),activedefender())
                                    elif activeplayer=="sf":
                                            player.shot(useplayer(),valp3,curval(),activedefender())
                                    elif activeplayer=="pf":
                                            player.shot(useplayer(),valp4,curval(),activedefender())
                                    elif activeplayer=="c":
                                            player.shot(useplayer(),valp5,curval(),activedefender())
                                    score+=player.score(useplayer())
    if stat1=="M":
        tst=fontst.render(mtext,True, [0,0,0], [155,0,0])
        s.blit(tst,mcenter)
    elif stat1=="2p":
        tst=fontst.render(tptext,True, [0,0,0], [155,0,0])
        s.blit(tst,tpcenter)
    elif stat1=="3p":
        tst=fontst.render(thptext,True, [0,0,0], [155,0,0])
        s.blit(tst,thpcenter)
    elif stat1=="B":
        tst=fontst.render(bltext,True, [0,0,0], [155,0,0])
        s.blit(tst,blcenter)
    seconds=(pygame.time.get_ticks()-start_ticks)//1000
    if score>=21:
        seconds=15
    tleft="Time Left is : " + str(15-seconds)
    tblit = tfont.render(tleft,True, [155,0,0], [0,0,0])
    s.blit(tblit,tcenter)
    if seconds>=9000000:
        RUN= False                     
    player.update(useplayer())
    #opponent.update(o1)
    ball.draw(b1)
    pygame.display.update()
    if RUN== False:
        pygame.quit()
    
