import pygame
from player import Player
from network import Network

width,height=500,500
win=pygame.display.set_mode((width,height))
pygame.display.set_caption('Trial')

def redraw(win,player,player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    
    pygame.display.update()
def main():
    n=Network()
    p=n.getP()
    r=True
    clock=pygame.time.Clock()
    while r:
        p2=n.send(p)
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                r=False
                pygame.quit()
        p.move()
        redraw(win,p,p2)


main()   
