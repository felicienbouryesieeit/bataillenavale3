import pygame
import sys
import random

isennemi=False
numberofslot=100
numberofbarriereslot=0
numberofplayership=0
numberofennemiship=0
basedecalage=130
ispressingspace=False
ispressingrotate=False
isvertical=False
playershipetape=0
topleft3=0
isingame=False
playerlife=0
ennemilife=0

numberofplayershot=0
numberofennemishot=0

numberofplayervalidshot=0
numberofennemivalidshot=0


playership=[]
ennemiship=[]
slots = []
barriereslot = []
playershot=[]
ennemishot=[]
playervalidshot=[]
ennemivalidshot=[]



#initialisez la fenetre du jeu
pygame.init()

#detailler la taille de la fenetre du jeu
slotdistance=30
beginlocationx=0
beginlocationy=0
currentplayerlocationx=0
currentplayerlocationy=0
haveplayermoved=False

taille_fenetre = (800, 600)

blanc = (0, 100,100)
red = (255,0,0)
bleu=(0,255,255)
yellow=(255,255,0)
blue2=(0,0,255)
white=(255,255,255)
rose=(255,0,255)
black=(0,0,0)
green=(0,255,0)

col=blue2
col2=blue2

uplimit=(1*slotdistance)+basedecalage
leftlimit=(2*slotdistance)+basedecalage
downlimit=(10*slotdistance)+basedecalage
rightlimit=(11*slotdistance)+basedecalage

fenetre = pygame.display.set_mode(taille_fenetre)
#slotimage = pygame.image.load('slot.png')
#slotimage.convert()
rectanglewidth=(25+(slotdistance*(5-1)))
rectangleheight=25
currentplayershipscale=0
shipbasescale=5



















font = pygame.font.Font(None, 36)
text = font.render("Hello, Pygame!", True, white)
victoiretexte=""

text_rect = text.get_rect()

# Placer le texte au centre de la fenêtre
text_rect.center = (350, 100)

























def changeplayershipsize(b):
    global currentplayershipscale
    global ennemilife
    global playerlife
    currentplayershipscale=b
    if isennemi:
            ennemilife+=b
    else:
            playerlife+=b
    
def beginplaceshipglobal():
    global shipbasescale
    changeplayershipsize(shipbasescale)

beginplaceshipglobal()


rectanglewidth2=(25+(slotdistance*(currentplayershipscale-1)))
rectangleheight2=25

rect1=pygame.Rect(0,0,rectanglewidth,rectangleheight)




def beginplaceshipennemi():
    global playershipetape
    global topleft3
    global rect1
    global isennemi
    isennemi=True
    print("wejdene")
    playershipetape=0
    beginplaceshipglobal()
    rect1.topleft=topleft3
    
    #rotateship2()
    
    #rotateship2()
    spawnrect1()

def firstplayerturn():
    global currentplayershipscale
    global topleft3
    global rect1
    global isingame
    global isennemi
    isennemi=False
    isingame=True
    currentplayershipscale=1
    rect1.topleft=topleft3





def changeplayership():
    global playershipetape
    global currentplayershipscale
    global isennemi
    changeplayership2(0,3)
    changeplayership2(1,3)
    changeplayership2(2,4)
    changeplayership2(3,2)
    if not playershipetape==4:
        playershipetape+=1
    else:
        if isennemi==False:
            beginplaceshipennemi()
        else:
            firstplayerturn()



def changeplayership2(a,b):
    global playershipetape
    global currentplayershipscale
    global ennemilife
    global playerlife

    print("pitie",playershipetape==a)
    if playershipetape==a:
        changeplayershipsize(b)

    print("gaga",currentplayershipscale)



def setplayersize():
    global rectanglewidth2
    global rectangleheight2
    
    rectanglewidth2=(25+(slotdistance*(currentplayershipscale-1)))
    rectangleheight2=25

def spawnrect1():
    global rect1
    global rectanglewidth
    global rectangleheight
    global topleft3

    
    topleft2=rect1.topleft
    rect1=pygame.Rect(0,0,rectanglewidth,rectangleheight)
    rect1.topleft=topleft2




def setrect1scale():
    global rectanglewidth
    global rectangleheight
    global currentplayershipscale
    
    #rectanglewidth=(25+(slotdistance*(currentplayershipscale-1)))
    #rectangleheight=25
    #spawnrect1()

setrect1scale()



def resetmoveplayer():
    global haveplayermoved
    if haveplayermoved==True:
        haveplayermoved=False

def moveplayer(directionx,directiony):
    global currentplayerlocationx
    global currentplayerlocationy
    global haveplayermoved
    global slotdistance
    global uplimit
    global leftlimit
    global topleft3
    global rect1

    if haveplayermoved==False:

        haveplayermoved=True

        

        
        
        
        """
        

        
        
        
        """
        #print("rectangley: ",rect1.y,"uplimit:",uplimit)
            

        if topleft3==0:
            topleft3=rect1.topleft

        currentplayerlocationx=slotdistance*directionx
        currentplayerlocationy=slotdistance*directiony

        moveplayer2(currentplayerlocationx,currentplayerlocationy)


        

def moveplayer2(x,y):
    rect1.topleft=rect1.x+x,rect1.y+y
    if rect1.y<uplimit:
        rect1.y=uplimit

    if rect1.x<leftlimit:
        rect1.x=leftlimit

    if rect1.y>downlimit:
        rect1.y=downlimit

    if rect1.x>rightlimit:
        rect1.x=rightlimit


def rotateship2():
    global isvertical
    if isvertical==False:
        isvertical=True
    else:
        isvertical=False
    rotateship()

def rotateship():
    global rectangleheight
    global rectanglewidth
    global rect1
    global isvertical
    
    #rectangleheight3=rectangleheight
    #rectanglewidth3=rectanglewidth
    print("vol")
    setplayersize()
    if (isvertical==True) :
            rectangleheight=rectanglewidth2
            rectanglewidth=rectangleheight2
    else:
            rectangleheight=rectangleheight2
            rectanglewidth=rectanglewidth2 
    spawnrect1()
            
    
    #moveplayer2(0,0)
rotateship()



def spawnslots():
    count = 0
    global numberofslot
    global slots
    global barriereslot
    global numberofbarriereslot
    global beginlocationx
    global beginlocationy
    global slotdistance
    global basedecalage
    slots=numberofslot
    numberofslot2=numberofslot
    slots = []
    barriereslot=[]
    locationx=0
    locationy=0
    #distance=30
    isbarriere=False
    numberofslot=0
    numberofbarriereslot=0
    numberofslot2=0
    
    while locationy <= 11:

        isbarriere=False

        if locationx==12:
            locationx=0
            locationy+=1
        
        
        if locationx==0 or locationx==11   or locationy==0 or locationy==11:
            isbarriere=True
        
        nouveau_rectangle = pygame.Rect(0, 0, 20, 20)

        

        if isbarriere==False :
            slots.append(nouveau_rectangle)
            numberofslot+=1
        else:

            if not(locationx==0 and locationy==12):
                

                barriereslot.append(nouveau_rectangle)
                numberofbarriereslot+=1
        
        
            
        locationx+=1
        nouveau_rectangle.topleft=(locationx*slotdistance)+basedecalage,(locationy*slotdistance)+basedecalage
        
        if numberofslot==1:
            beginlocationx=nouveau_rectangle.x
            beginlocationy=nouveau_rectangle.y


        #numberofbarriereslot=numberofslot2-numberofslot
        

        count+=1
        
    """
        isbarriere=False
        
        
        if locationx==0 or locationx==10 or locationy==0 or locationy==10:
            isbarriere=True
        
        

        #if isbarriere==False:
        slots.append(nouveau_rectangle)
        #else:
        #barriereslot.append(nouveau_rectangle)
            #numberofslot2+=1

       
        """

    #numberofbarriereslot=numberofslot2-numberofslot

def endspawnrectangle(nouveau_rectangle):
    nouveau_rectangle.topleft=rect1.topleft
            
            
    rotateship2()
            
    print("FMA",currentplayershipscale)
    if isingame==False:
            changeplayership()
    rotateship()

def onwin(playerwin):
    global victoiretexte
    if playerwin:
        victoiretexte="player 1 win"
    else:
        
        victoiretexte="player 2 win"
        
def spawnplayership():
    global playershot
    global ennemishot
    global playership
    global numberofplayership
    global numberofplayershot
    global numberofennemishot
    global rectangleheight
    global rectanglewidth
    global col
    global isvertical
    global currentplayershipscale
    global isennemi
    global numberofennemiship
    global numberofplayervalidshot
    global playervalidshot
    global numberofennemivalidshot
    global col2
    global blue2
    global red
    global ennemilife
    global playerlife
    if not col==red: 
            rotateship2()
            nouveau_rectangle = pygame.Rect(0, 0, rectangleheight,rectanglewidth)
            if not isingame==True:
                if isennemi==True:
                        ennemiship.append(nouveau_rectangle)
                        numberofennemiship+=1
                else:
                        playership.append(nouveau_rectangle)
                        numberofplayership+=1
            else:
                if isennemi==False:
                    playershot.append(nouveau_rectangle)
                    numberofplayershot+=1 
                else:
                    ennemishot.append(nouveau_rectangle)
                    numberofennemishot+=1 
                switchplayer()
                    


            
            
            endspawnrectangle(nouveau_rectangle)
    else:
         if isingame==True and col2==blue2:
            rotateship2()
            nouveau_rectangle = pygame.Rect(0, 0, rectangleheight,rectanglewidth)
            if isennemi==True:
                playervalidshot.append(nouveau_rectangle)
                numberofplayervalidshot+=1
                playerlife-=1
                if playerlife==0:
                    onwin(False)
            else:
                ennemivalidshot.append(nouveau_rectangle)
                numberofennemivalidshot+=1
                ennemilife-=1
                if ennemilife==0:
                    onwin(True)
            switchplayer()

            endspawnrectangle(nouveau_rectangle)

















def beginspace():
    global ispressingspace
    global currentplayershipscale
    if ispressingspace==False:
        ispressingspace=True
        print("miaou")
        spawnplayership()
        #currentplayershipscale=2
        setrect1scale()


def resetspace():
    global ispressingspace
    if ispressingspace==True:
        ispressingspace=False


def beginrotate():
    global ispressingrotate
    if ispressingrotate==False:
        ispressingrotate=True
        print("UUUUU")
        rotateship2()


def resetrotate():
    global ispressingrotate
    if ispressingrotate==True:
        ispressingrotate=False





def showslots():
    count = 0
    global slots
    global barriereslot
    global numberofslot
    global numberofbarriereslot
    global col
    global rect1
    while count < numberofslot:
        pygame.draw.rect(fenetre,bleu,slots[count])
        
        count+=1

    
    
    count=0
    while count < numberofbarriereslot:
        pygame.draw.rect(fenetre,yellow,barriereslot[count])
        if rect1.colliderect(barriereslot[count]):
            col=red
        
        count+=1

def showplayerships():
    global playership
    global ennemiship
    global numberofplayership
    global numberofennemiship
    global rect1
    global col
    global isennemi
    global numberofplayershot
    global numberofennemishot
    global playershot
    global ennemishot
    global ennemivalidshot
    global numberofennemivalidshot
    global playervalidshot
    global numberofplayervalidshot
    global col2

    count=0
    #if (isennemi==False):
    while count < numberofplayership:
        #print("bateau")
            if isingame==False and isennemi==False:
                pygame.draw.rect(fenetre,white,playership[count])
            if rect1.colliderect(playership[count]) :#and not isingame:
                if isingame==True or isennemi==False:
                    col=red
            count+=1
    #else:
    count=0
    while (count<numberofennemiship) :
        if isingame==False and isennemi==True:
            pygame.draw.rect(fenetre,black,ennemiship[count])
        if rect1.colliderect(ennemiship[count]) :
            if isingame==True or isennemi==True:#and not isingame:
                col=red
        
        count+=1

    count=0
    while(count<numberofplayershot):
            if isennemi==False :
                pygame.draw.rect(fenetre,rose,playershot[count])
                
            if rect1.colliderect(playershot[count]) and isingame and isennemi==False:
                #col=red
                col2=red
            
            count+=1
    
    count=0
    while(count<numberofennemishot):
            if isennemi==True :
                pygame.draw.rect(fenetre,green,ennemishot[count])
            if rect1.colliderect(ennemishot[count]) and isingame and isennemi==True:
                #col=red
                col2=red
            
            count+=1

    
    count=0
    while(count<numberofplayervalidshot):
            if isennemi==True :
                pygame.draw.rect(fenetre,black,playervalidshot[count])
            if rect1.colliderect(playervalidshot[count]) and isingame and isennemi==True:
                col2=red
            
            count+=1 

    count=0
    while(count<numberofennemivalidshot):
            if isennemi==False :
                pygame.draw.rect(fenetre,white,ennemivalidshot[count])
            if rect1.colliderect(ennemivalidshot[count]) and isingame and isennemi==False:
                col2=red
            
            count+=1


def switchplayer():
    global isennemi
    if isennemi==True:
        isennemi=False
    else:
        isennemi=True

def show():
    
    global rect1
    global col
    global col2
    global isingame
    global screen
    col=blue2
    col2=blue2
    col3=blue2
    showslots()
    showplayerships()
    if isingame:
        col3=col2
    else:
        col3=col
        
    pygame.draw.rect(fenetre,col3,rect1)
























































gogo=0


#detailler la taille de la fenetre du jeu

spawnslots()
#rect2=pygame.Rect(0,0,25,25)

#variable qui definit la couleur de fond du jeu


#rect[]
#rect2.center=600,110


#boucle qui se joue plusieurs fois par seconde
moveplayer2(beginlocationx,beginlocationy)
currentplayerlocationx=beginlocationx
currentplayerlocationx=beginlocationy
random_number = 0
while True:
    for event in pygame.event.get():
        #random_number = random.randint(0, 255)
        
        #blanc = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


#appliquer la couleur de fond du jeu
    

    fenetre.fill(blanc)
    #rect1.center=gogo,200
    #gogo+=0.1
    #print("player life: ",playerlife," ennemilife ",ennemilife)
    if pygame.key.get_pressed()[pygame.K_SPACE] :
        
        beginspace()

    else: 
        resetspace()


    if pygame.key.get_pressed()[pygame.K_r] :
        
        beginrotate()

    else: 
        resetrotate()

















    if pygame.key.get_pressed()[pygame.K_RIGHT] :
        
        moveplayer(1,0)
    
    if pygame.key.get_pressed()[pygame.K_LEFT] :
        
        moveplayer(-1,0)

    if pygame.key.get_pressed()[pygame.K_UP] :
        
        moveplayer(0,-1)
    
    if pygame.key.get_pressed()[pygame.K_DOWN] :
        
        moveplayer(0,1)

    if not pygame.key.get_pressed()[pygame.K_DOWN] and  not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
        resetmoveplayer()
        #gogo+=0.1

    #
    
    
    
    show()
    #
    #fenetre.blit(slotimage,[10,10])

    
    text = font.render(victoiretexte, True, white)
    
    fenetre.blit(text, text_rect)

    pygame.display.flip()
