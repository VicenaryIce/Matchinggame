import pygame, sys
from pygame.locals import QUIT
import random

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Hello World!')
font = pygame.font.SysFont('Sans',50)
limages = []
lnames = []
circs = []
clickedimage = 0
def renderimages():
    images =['candycrush.jpg','sorry.png','temple_runner.png','subway_surfers.png']
    names = ['Candy crush','Sorry','Temple Runner','Subway Surfers']
    
    random.shuffle(names)
    cordinate = 25
    ncord = 25
    for i in images:
        image = pygame.transform.scale(pygame.image.load(i),(50,50))
        screen.blit(image,(50,cordinate))
        imagerect = pygame.Rect(50,cordinate,50,50)
        limages.append(imagerect)
        
        
        cordinate = cordinate+100
    for i in names:
         name = font.render(i,True,'white')
         screen.blit(name,(400,ncord))
         namerect = pygame.Rect(400,ncord,300,50)
         lnames.append(namerect)
         print('pass')
         ncord  = ncord+100
         #textrect = pygame.Rect(400,ncord,)




renderimages()
print(limages)
while True:
   
   for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mx,my = pygame.mouse.get_pos()
            selectrect = pygame.Rect(mx,my,40,40)
            for i in limages:
                if selectrect.colliderect(i):
                    clickedimage == 1
                    
    
                    selectcirc = pygame.draw.circle(screen,'red',(mx,my),radius= 10)
                    circs.append(selectcirc)
                    
                    
        

                    

        if event.type == pygame.MOUSEBUTTONUP:            
            for i in lnames:
                if selectrect.colliderect(i) :
                    if len(circs)==1:
                        selectcirc = pygame.draw.circle(screen,'red',(mx,my),radius= 10)
                        circs.append(selectcirc)
                        pygame.draw.line(screen,'red',start_pos=(circs[0].x,circs[0].y),end_pos=(circs[1].x,circs[1].y),width=10)
                   
                    circs.clear()

                    
        
   pygame.display.update()