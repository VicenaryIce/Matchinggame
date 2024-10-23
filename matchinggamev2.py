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
clickedimage = False
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
            
            for i in limages:
               if clickedimage== False:
                    if i.collidepoint((mx,my)):
                        
                        
        
                        selectcirc = pygame.draw.circle(screen,'red',(mx,my),radius= 10)
                        pos1 = pygame.mouse.get_pos()
                        clickedimage = True
                  
                    
                    
        

                    

        if event.type == pygame.MOUSEBUTTONUP: 
            nx,ny = pygame.mouse.get_pos()    
               
            for i in lnames:
                i
                print(i)
                if i.collidepoint((nx,ny)) :
                    if clickedimage == True:
                    
                        selectcirc = pygame.draw.circle(screen,'red',(nx,ny),radius= 10)
                        pos2 = pygame.mouse.get_pos()
                        pygame.draw.line(screen,'red',start_pos=pos1,end_pos=pos2,width=10)
                        clickedimage = False
                   
                       
#Check pos of where clicked to determine whether it is clicked or not. You need to ask if the
#image name is the same as the name name. use i.collidepoint function and use i.x, i.y
                    
        
   pygame.display.update()