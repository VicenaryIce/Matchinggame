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
correctnames = []
dict_images = {}
dict_names = {}
imagesclicked = []
answers = {}

clickedimage = False
score = 0
def renderimages():
    global dict_images
    global dict_names
    global lnames
    images =['candycrush.jpg','sorry.png','temple_runner.png','subway_surfers.png']
    names = ['Candy crush','Sorry','Temple Runner','Subway Surfers']
    cordinate = 25
    ncord = 25
    newestcord = 25
    #random.shuffle(names)
    for i in range(4):
        
        image = pygame.transform.scale(pygame.image.load(images[i]),(50,50))
        screen.blit(image,(50,cordinate))
        imagerect = pygame.Rect(50,cordinate,50,50)
        name = font.render(names[i],True,'white')
        screen.blit(name,(400,ncord))
        namerect = pygame.Rect(400,ncord,300,50)
        limages.append(imagerect)
        lnames.append(namerect)
        answers[i] = [imagerect, namerect]


        ncord  = ncord+100
        #dict_images[i] = imagerect
        cordinate = cordinate+100
    ncord = 25
    combined = list(zip(names,lnames))
    random.shuffle(combined)
    names,lnames = zip(*combined)
    names= list(names)
    #lnames = list(lnames)
    for i in range(4):
        name = font.render(names[i],True,'white')
        screen.blit(name,(400,ncord))

        

    print("DICTIONARY ",answers)
    for value in answers.values():
        print("VALUE:" +str(value))

#The image rect is the first value

    

"""   ncord = 25
    for i in names:
        
        #name = font.render(i,True,'white')
        screen.blit(name,(400,ncord))
        namerect = pygame.Rect(400,ncord,300,50)
        lnames.append(namerect)
        ncord  = ncord+100
        #dict_names[i] = [namerect,dict_images[]]
        """

   
#  correctnames.append(namerect)
renderimages()
print("EXAMPLE",answers[0][0])
#print(limages)
#print(lnames)
#print(correctnames)
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

                        imageclicked = i
                        imagesclicked.append(imageclicked)
                        print(imageclicked)
                        selectcirc = pygame.draw.circle(screen,'red',(mx,my),radius= 10)
                        pos1 = pygame.mouse.get_pos()
                        clickedimage = True
                  

        

                    

        if event.type == pygame.MOUSEBUTTONUP: 
           
            nx,ny = pygame.mouse.get_pos()    
               
            for i in lnames:
                
                #print(i)
                if i.collidepoint((nx,ny)):
                    if clickedimage == True:
                        nameclicked = i
                        imagesclicked.append(nameclicked)
                        print("LIST: ",imagesclicked)
                        for value in answers.values():
                            if imagesclicked == value:
                                selectcirc = pygame.draw.circle(screen,'red',(nx,ny),radius= 10)
                                pos2 = pygame.mouse.get_pos()
                                pygame.draw.line(screen,'red',start_pos=pos1,end_pos=pos2,width=10)
                                score = score+1
                                imagesclicked.clear()
                                clickedimage = False

                    
#CHECK IF THE NAME CLICKED IS THE KEY OF THE IMAGE IN THE SUB-LIST
#PUT IMAGE RECT AND NAME RECT IN A LIST, AND DO if *list* in answers[0]
#Check pos of where clicked to determine whether it is clicked or not. You need to ask if the
#image name is the same as the name name. use i.collidepoint function and use i.x, i.y
                    
        

    
    
    
    
    
    
    
    pygame.display.update()
   
   