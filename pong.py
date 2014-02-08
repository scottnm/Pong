import pygame, sys, random
from pygame.locals import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
PADDLE_WIDTH = 10
PADDLE_LENGTH = 60
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

    def checkCollision(self, pLEFT, pRIGHT):
        if(self.y-self.r <= 0 or self.y+self.r >= WINDOW_HEIGHT):
            self.collideY()
        if((self.x-self.r <= PADDLE_WIDTH and (self.y+self.r >= pLEFT.y and self.y-self.r <= pLEFT.y+PADDLE_LENGTH)) or (self.x+self.r >= WINDOW_WIDTH-PADDLE_WIDTH and (self.y+self.r >= pRIGHT.y and self.y-self.r <= pRIGHT.y+PADDLE_LENGTH))):
            self.collideX()

    def update(self):
        self.x = self.x+self.vx
        self.y = self.y+self.vy

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
    b1 = Ball()
    b2 = Ball()
    pLEFT = Paddle(0, 200-PADDLE_LENGTH/2, PADDLE_WIDTH, PADDLE_LENGTH)
    pRIGHT = Paddle(WINDOW_WIDTH-PADDLE_WIDTH, 200-PADDLE_LENGTH/2, PADDLE_WIDTH, PADDLE_LENGTH)

    
    #Game Loop
    while True:

        if(b1.x>WINDOW_WIDTH or b1.x<0):
            b1 = Ball()

        if(b2.x>WINDOW_WIDTH or b2.x<0):
            b2 = Ball()
        
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
        

        b1.checkCollision(pLEFT, pRIGHT)
        b2.checkCollision(pLEFT, pRIGHT)
        

        b1.update()
        b2.update()
        
        pygame.display.update()
        DS.fill(BLACK)
    
        b1.draw(DS)
        b2.draw(DS)
        
        pLEFT.draw(DS)
        pRIGHT.draw(DS)
main()
