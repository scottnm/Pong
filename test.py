import pygame, sys
from pygame.locals import *

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
DS = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Test")



class Ball():
    def __init__(self):
        self.x = 200
        self.y = 200
        self.r = 10

    def draw(self, DS):
        pygame.draw.circle(DS, WHITE, (self.x,self.y), self.r)

class Paddle():
    
    def __init__(self, x, y, width, length):
        self.x=x
        self.y=y
        self.WIDTH=width
        self.LENGTH=length
        self.up=False
        self.down=False

    def draw(self, DS):
        pygame.draw.rect(DS, WHITE, pygame.Rect(self.x, self.y, self.WIDTH, self.LENGTH))

def main():
    PADDLE_WIDTH = 10
    PADDLE_LENGTH = 60
    
    b1 = Ball()
    pLEFT = Paddle(0, 200-PADDLE_LENGTH/2, PADDLE_WIDTH, PADDLE_LENGTH)
    pRIGHT = Paddle(WINDOW_WIDTH-PADDLE_WIDTH, 200-PADDLE_LENGTH/2, PADDLE_WIDTH, PADDLE_LENGTH)

    
    #Game Loop
    while True:
        for event in pygame.event.get():
            
            if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
                pLEFT.up=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_s:
                pLEFT.down=True
            if event.type==pygame.KEYUP and event.key==pygame.K_w:
                pLEFT.up=False
            if event.type==pygame.KEYUP and event.key==pygame.K_s:
                pLEFT.down=False

            if event.type==pygame.KEYDOWN and event.key==pygame.K_o:
                pRIGHT.up=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_l:
                pRIGHT.down=True
            if event.type==pygame.KEYUP and event.key==pygame.K_o:
                pRIGHT.up=False
            if event.type==pygame.KEYUP and event.key==pygame.K_l:
                pRIGHT.down=False
            
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
                
        #Game State
        if(pLEFT.up):
            pLEFT.y=pLEFT.y-3
        if(pLEFT.down):
            pLEFT.y=pLEFT.y+3

        if(pRIGHT.up):
            pRIGHT.y=pRIGHT.y-3
        if(pRIGHT.down):
            pRIGHT.y=pRIGHT.y+3
                
        pygame.display.update()
        DS.fill(BLACK)

        b1.draw(DS)
        
        pLEFT.draw(DS)
        pRIGHT.draw(DS)
main()
