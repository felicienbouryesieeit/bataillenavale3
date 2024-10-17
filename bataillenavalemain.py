import pygame
import sys
import random

#Définition de toute les variables globales
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


slotdistance=30
beginlocationx=0
beginlocationy=0
currentplayerlocationx=0
currentplayerlocationy=0
haveplayermoved=False

rectanglewidth=(25+(slotdistance*(5-1)))
rectangleheight=25
currentplayershipscale=0
shipbasescale=5 

#Définition des arrays
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


taille_fenetre = (800, 600)

#definition des couleurs couleurs

couleurfond = (0, 100,100)
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

#définition des limites du terrain (lorsque le joueur se déplace)

uplimit=(1*slotdistance)+basedecalage
leftlimit=(2*slotdistance)+basedecalage
downlimit=(10*slotdistance)+basedecalage
rightlimit=(11*slotdistance)+basedecalage

fenetre = pygame.display.set_mode(taille_fenetre)

















#variables globale  pour afficher le texte de fin

font = pygame.font.Font(None, 36)
text = font.render("", True, white)
victoiretexte=""

text_rect = text.get_rect()

text_rect.center = (350, 100)
























#change la taille du bateau avant de le poser (afin de faire un bateau de chaque type: porte avion, torpilleur, ect)
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

#definition de "rect 1" (le personnage que l'on controle)
rectanglewidth2=(25+(slotdistance*(currentplayershipscale-1)))
rectangleheight2=25

rect1=pygame.Rect(0,0,rectanglewidth,rectangleheight)



#placer un bateau lorsque c'est au joueur 2 de jouer
def beginplaceshipennemi():
    global playershipetape
    global topleft3
    global rect1
    global isennemi
    isennemi=True
    playershipetape=0
    beginplaceshipglobal()
    rect1.topleft=topleft3
    spawnrect1()

#code qui lance le 1er tour du joueur 1, après que tout les bateaux aient été placés
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




#au début du jeu, changer le type de bateau à chaque fois qu'un bateau est placé
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

    if playershipetape==a:
        changeplayershipsize(b)



#permet de changer la taille du bateau lorsqu'on le fait "tourner"
def setplayersize():
    global rectanglewidth2
    global rectangleheight2
    
    rectanglewidth2=(25+(slotdistance*(currentplayershipscale-1)))
    rectangleheight2=25

#permet de changer la taille du joueur
def spawnrect1():
    global rect1
    global rectanglewidth
    global rectangleheight
    global topleft3

    
    topleft2=rect1.topleft
    rect1=pygame.Rect(0,0,rectanglewidth,rectangleheight)
    rect1.topleft=topleft2







#permet de bouger le joueur
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

#permet de faire tourner le bateau
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
    
    
    
    setplayersize()
    if (isvertical==True) :
            rectangleheight=rectanglewidth2
            rectanglewidth=rectangleheight2
    else:
            rectangleheight=rectangleheight2
            rectanglewidth=rectanglewidth2 
    spawnrect1()
            
    
rotateship()


#permet de faire apparaitre le terrain (les cases et les murs)
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



        

        count+=1
        
def onwin(playerwin):
    global victoiretexte
    if playerwin:
        victoiretexte="player 1 win"
    else:
        
        victoiretexte="player 2 win"


def endspawnrectangle(nouveau_rectangle):
    nouveau_rectangle.topleft=rect1.topleft
            
            
    rotateship2()
            
    print("FMA",currentplayershipscale)
    if isingame==False:
            changeplayership()
    rotateship()

#permet de faire apparaitre des choses (des vaisseaux ou des tirs) lorsque l'on appuie sur espace
        
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
















#permet de faire une action en appuyant sur "espace "
def beginspace():
    global ispressingspace
    global currentplayershipscale
    if ispressingspace==False:
        ispressingspace=True
        print("miaou")
        spawnplayership()

def resetspace():
    global ispressingspace
    if ispressingspace==True:
        ispressingspace=False

#permet de faire une action en appuyant sur "R"
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




#permet d'afficher le terrain
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
#permet d'afficher les objets créés par les joueurs
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
    
    while count < numberofplayership:
        
            if isingame==False and isennemi==False:
                pygame.draw.rect(fenetre,white,playership[count])
            if rect1.colliderect(playership[count]) :
                if isingame==True or isennemi==False:
                    col=red
            count+=1
    
    count=0
    while (count<numberofennemiship) :
        if isingame==False and isennemi==True:
            pygame.draw.rect(fenetre,black,ennemiship[count])
        if rect1.colliderect(ennemiship[count]) :
            if isingame==True or isennemi==True:
                col=red
        
        count+=1

    count=0
    while(count<numberofplayershot):
            if isennemi==False :
                pygame.draw.rect(fenetre,rose,playershot[count])
                
            if rect1.colliderect(playershot[count]) and isingame and isennemi==False:
                
                col2=red
            
            count+=1
    
    count=0
    while(count<numberofennemishot):
            if isennemi==True :
                pygame.draw.rect(fenetre,green,ennemishot[count])
            if rect1.colliderect(ennemishot[count]) and isingame and isennemi==True:
                
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





#fonction générale d'affichage
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


#Permet d'alterner entre le joueur 1 et le joueur 2
def switchplayer():
    global isennemi
    if isennemi==True:
        isennemi=False
    else:
        isennemi=True


























































#crée le terrain
spawnslots()



#place le joueur sur la première case
moveplayer2(beginlocationx,beginlocationy)
currentplayerlocationx=beginlocationx
currentplayerlocationx=beginlocationy

#boucle qui se joue plusieurs fois par seconde
while True:
    for event in pygame.event.get():
        
        #permet au jeu de ne pas se quitter tout seul
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #remplis l'arrière plan du jeu d'une couleur choisie
    fenetre.fill(couleurfond)

    #permet d'utiliser les différentes touches du jeu
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



    #permet d'afficher les différents éléments du jeu à chaque frame
    show()

    #permet d'afficher le texte de fin
    text = font.render(victoiretexte, True, white)
    
    fenetre.blit(text, text_rect)


    #permet d'afficher la fenêtre
    pygame.display.flip()
