#Ritar en blomma där vinkeln till varje nytt blad ökar med en fix vinkel v.
#F_(n)/F_(n+1)->0.618...=v ger bäst spridning
#
#Kräver att man har pygame i sin python-installation
#Om man använder anaconda+spyder kan man skriva "pip install pygame" i konsolen
#se https://www.pygame.org/news
#
#Knappar: 
#piltangenter: öka/minska vinkel
#musklick/drag: sätt vinkel beroende på musens x-xoordinat#space: skriv in exakt vinkel i konsolen
#c: växkla mellan enfärgad/slumpfärgad


import pygame
import pygame.gfxdraw
import math
import random
             
pygame.init()


xscreen=800
yscreen=600
screen = pygame.display.set_mode((xscreen,yscreen))

running = True
slumpfärg=True

def rand_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
class Blomma:
    def __init__(self,pos=(400,300),vinkel=0.61803398875,färg=(0,0,0)): #vinkel anges på [0,1] där 1 är ett varv
        self.pos=pos
        self.vinkel=vinkel
        self.färg=färg
    

    def draw(self):
        random.seed(0)
        color = self.färg
        for k in range(300):
            inc=1
            if slumpfärg:
                color = rand_color()
            
            p = (self.pos[0]+(k*inc)*math.cos(k*2*math.pi*self.vinkel),self.pos[1]+(k*inc)*math.sin(k*2*math.pi*self.vinkel))
            pygame.draw.circle(screen, color, p, 3+k/18) 
        
            
b = Blomma(färg=(0,120,0))
    
while running:
    
    knappar = pygame.mouse.get_pressed()
    if knappar[0]:
        pos=pygame.mouse.get_pos()
        v = float(pos[0]/screen.get_width())
        b.vinkel=v
               
    pygame.display.set_caption(str(b.vinkel)+" varv")
    screen.fill((255,255,255))
    b.draw()
    pygame.display.flip()


    #Knapp-events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if event.key==pygame.K_ESCAPE:
                running = False
            elif event.key==pygame.K_SPACE:
                b.vinkel = float(input("Ange vinkel (andel av varv): "))
            elif event.key==pygame.K_LEFT:
                b.vinkel -=0.0005
            elif event.key==pygame.K_RIGHT:
                b.vinkel +=0.0005
            elif event.key==pygame.K_UP:
                b.vinkel +=0.00005
            elif event.key==pygame.K_DOWN:
                b.vinkel -=0.00005
            elif event.key==pygame.K_c:
                slumpfärg = not slumpfärg
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            if event.button==1:
                pass
        
pygame.quit()
            