import pygame, sys, random
from pygame.locals import *

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
PADDLE_WIDTH = 10
PADDLE_LENGTH = 60
FONTSIZE = 30
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
DS = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")



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
        #print 'x velocity '+ str(self.vx)

    def collideY(self):
        if(self.vy>0):
            self.vy = self.vy+1
        else:
            self.vy = self.vy-1
            
        self.vy = -self.vy

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

class ScoreBoard():

    def __init__(self):
        self.scoreLeft = 0
        self.scoreRight = 0
        self.myFont = pygame.font.SysFont("Verdana", FONTSIZE)

    def update(self, DS):
        self.scoreLeftIMG = self.myFont.render(str(self.scoreLeft), 0, WHITE)
        self.scoreRightIMG = self.myFont.render(str(self.scoreRight), 0, WHITE)
        DS.blit(self.scoreLeftIMG, (WINDOW_WIDTH/4 - FONTSIZE/2, 10))
        DS.blit(self.scoreRightIMG, (3 * WINDOW_WIDTH/4 - FONTSIZE/2, 10))

def main():
    Balls = [Ball(), Ball(), Ball()]
    
    pLEFT = Paddle(0, 200-PADDLE_LENGTH/2, PADDLE_WIDTH, PADDLE_LENGTH)
    pRIGHT = Paddle(WINDOW_WIDTH-PADDLE_WIDTH, 200-PADDLE_LENGTH/2, PADDLE_WIDTH, PADDLE_LENGTH)
    sb = ScoreBoard()
    
    #Game Loop
    while True:

        for i in range(0, len(Balls)):
            if(Balls[i].x>WINDOW_WIDTH):
                Balls[i] = Ball()
                sb.scoreLeft+=1
            elif(Balls[i].x<0):
                Balls[i] = Ball()
                sb.scoreRight+=1
        
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
        
        for b in Balls:
            b.checkCollision(pLEFT, pRIGHT)
            b.update()
            
 
        
        pygame.display.update()

        #DrawsBackground
        DS.fill(BLACK)
        pygame.draw.line(DS, WHITE, (WINDOW_WIDTH/2,0), (WINDOW_WIDTH/2, WINDOW_HEIGHT))
        sb.update(DS)
        
        #Draws Paddles
        pLEFT.draw(DS)
        pRIGHT.draw(DS)

        for b in Balls:
            b.draw(DS)

        
main()
