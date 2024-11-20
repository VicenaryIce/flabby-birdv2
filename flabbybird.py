import pygame, sys
from pygame.locals import QUIT
import random
pygame.init()
screen = pygame.display.set_mode((800, 900))
background = pygame.image.load('background.png')
ground = pygame.image.load('groundpicture.png')
#screen.blit(background,(0,0))
starttime = pygame.time.get_ticks()
x=0


class Bird(pygame.sprite.Sprite):#Bird is child class, sprite class is the parent class which is a template.
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.birdimages = []
        self.pictures = 0

        for i in range(1,4):
    
            self.birdimages.append(pygame.image.load('bird'+str(i)+'.png'))
        self.image = self.birdimages[self.pictures]
        self.rect = self.image.get_rect()
        self.delay = 0
        self.rect.center = x,y
        self.velocity = 0
    def update(self):
        #For the flying:
        #Introducing game physics
        self.velocity = self.velocity+0.1
        if self.velocity >=8:
            self.velocity = 8
        if self.rect.y <= 700:
            self.rect.y = self.rect.y+self.velocity
        print(self.velocity)


        #flapping the wings:
        self.delay = self.delay+1

        if self.delay>5:
            self.delay = 0
            self.pictures = self.pictures+1

            if self.pictures == 3:
                self.pictures = 0
            self.image = self.birdimages[self.pictures]

class Pipe(pygame.sprite.Sprite):
    def __init__ (self,x,y,position):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('pipe.png')
        self.rect = self.image.get_rect()
        if position == 0:#toppipe
            self.image = pygame.transform.flip(self.image,False,True)#to flip the pipe
            self.rect.bottomleft = x,y-100
        else:
            self.rect.topleft = x,y+100



    def update(self):
      self.rect.x = self.rect.x-5

    """def create(self):
        #pos = random.randint(0,400)
        #screen.blit(screen,(self.x,pos))"""
    """def move(self):
        pos = random.randint(0,400)
        screen.blit(screen,(self.x,pos))
        self.x  = self.x-5
        pygame.display.update()
        #if abs(self.x) == 35:
            #pos = random.randint(0,400)
            #self.x = 800"""

        

        
birdgroup = pygame.sprite.Group()
pipes  = pygame.sprite.Group()

bird = Bird(25,450)
birdgroup.add(bird)#now bird should have the properties of birgroups


pygame.display.set_caption('Flappy Bird')



clock = pygame.time.Clock()
while True:
    screen.blit(background,(0,0))
    screen.blit(ground,(x,700))
    clock.tick(60)
    x=x-1
    if abs(x) >35:
        x = 0
    birdgroup.draw(screen)
    birdgroup.update()
    currenttime = pygame.time.get_ticks()
    y = random.randint(-100,100)
    
    if currenttime-starttime >= 1500:
        bottompipe = Pipe(800,350+y,1234567)
        toppipe = Pipe(800,350+y,0)
        pipes.add(toppipe)
        pipes.add(bottompipe)
        starttime = currenttime
    pipes.draw(screen)
#Whole update function behind the if condition. 

    pipes.update()



    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
    pygame.display.update()
