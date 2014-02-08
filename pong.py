import pygame, sys, random
from pygame.locals import *

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
DS = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Test")



class Ball():
    def __init__(self):
        self.x = WINDOW_WIDTH/2
        self.y = WINDOW_HEIGHT/2
        self.r = 10
        self.directionX = [-1,1]
        self.vx = 3 * self.directionX[random.randint(0,1)]
        self.vy = random.randint(1,3)*self.directionX[random.randint(0,1)]

    def draw(self, DS):
        pygame.draw.circle(DS, WHITE, (self.x,self.y), self.r)

    def collideX(self):
        if(self.vx>0):
            self.vx=self.vx+1
        else:
            self.vx=self.vx-1
            
        self.vx = -self.vx
        print 'x velocity '+ str(self.vx)

    def collideY(self):
        if(self.vy>0):
            self.vy = self.vy+1
        else:
            self.vy = self.vy-1
            
        self.vy = -self.vy
        print 'y velocity '+ str(self.vy)

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

        if(b1.x>WINDOW_WIDTH or b1.x<0):
            b1 = Ball()
        
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
        if(pLEFT.up and pLEFT.y > 0):
            pLEFT.y=pLEFT.y-10
        if(pLEFT.down and pLEFT.y+PADDLE_LENGTH < WINDOW_HEIGHT):
            pLEFT.y=pLEFT.y+10

        if(pRIGHT.up and pRIGHT.y > 0):
            pRIGHT.y=pRIGHT.y-10
        if(pRIGHT.down and pRIGHT.y+PADDLE_LENGTH < WINDOW_HEIGHT):
            pRIGHT.y=pRIGHT.y+10
        if(b1.y-b1.r <= 0 or b1.y+b1.r >= WINDOW_HEIGHT):
            b1.collideY()
        if((b1.x-b1.r <= PADDLE_WIDTH and (b1.y+b1.r >= pLEFT.y and b1.y-b1.r <= pLEFT.y+PADDLE_LENGTH)) or (b1.x+b1.r >= WINDOW_WIDTH-PADDLE_WIDTH and (b1.y+b1.r >= pRIGHT.y and b1.y-b1.r <= pRIGHT.y+PADDLE_LENGTH))):
            b1.collideX()
            
        

        b1.x = b1.x+b1.vx
        b1.y = b1.y+b1.vy
        pygame.display.update()
        DS.fill(BLACK)

        b1.draw(DS)
        
        pLEFT.draw(DS)
        pRIGHT.draw(DS)
main()
