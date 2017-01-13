import pygame
import random
import time
import nameGenerator

pygame.init()

FPS = 60

display_width = 1280
display_height = 720

desX = 721
desY = 232




status = ['Plukker','Læsser','Container','Emballage']

color = ['black','white']
color[0] = [0,0,0]
color[1] = [255,255,255]

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Arla Game')
clock = pygame.time.Clock()
workerPic = ''
workerImg = pygame.image.load (workerPic)


##class Worker:
##    def __init__(self,name,haircolor):
##        self.name = name
##        self.haircolor = haircolor
##class Plukker(Worker):
##    def Plukker(x,y):
##        gameDisplay.blit(WorkerImg,(x,y))

def worker(start_x,start_y):
    gameDisplay.blit(workerImg,(x,y)) 


def game_loop():

    

    start_x = 500
    start_y = 500
    
    count = 0

    X = 1
    Y = 1
    
    
    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        if (gameExit == False):
            count += 1
            if count > 50:
                y = y - Y
            if y == desY:
                Y = 0
                x = x + X
            if x == desX:
                X = 0
        if 
                
            
            
            
            
            
            
        gameDisplay.fill(color[1])

        

        worker(x,y)

        pygame.display.update()

        clock.tick(FPS)

game_loop()
pygame.quit()
quit()
        





    
        
