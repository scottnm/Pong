import pygame, sys
from pygame.locals import *

pygame.init()

dSurf = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Test Text")
myFont = pygame.font.SysFont("Times New Roman", 30)

while True:
    testText = myFont.render("Test Text", 0, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    dSurf.fill((0,0,0))
    dSurf.blit(testText, (200,200))

          """ b1.checkCollision(pLEFT, pRIGHT)
        b2.checkCollision(pLEFT, pRIGHT)
        
        b1.update()
        b2.update() """
        
        
    """#check for score on right goal
        if(b1.x>WINDOW_WIDTH):
            b1 = Ball()
            sb.scoreLeft+=1
        elif(b1.x<0):
            b1 = Ball()
            sb.scoreRight+=1
            
        #check for score on left goal
        if(b2.x>WINDOW_WIDTH):
            b2 = Ball()
            sb.scoreLeft+=1
        elif(b2.x<0):
            b2 = Ball()
            sb.scoreRight+=1 """

        """#Draws Balls
        b1.draw(DS)
        b2.draw(DS)"""
