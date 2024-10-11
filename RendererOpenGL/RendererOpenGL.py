
import pygame
from pygame.locals import *
from gl import Renderer
from buffer import Buffer

width = 960
height = 540

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF) #pygame.OPENGL Para dibujar pixles con open gl, # | pygame.DOUBLEBUF Para que no se vea el parpadeo  #| es un bitwise or

clock = pygame.time.Clock()

rend  = Renderer(screen)

triangle= [-0.5, -0.5, 0.0,
           0.0, 0.5, 0.0,
           0.5, -0.5, 0.0]

triangle= [-0.5, -0.5, 0.0,
           0.0, 0.5, 0.0,
           0.5, -0.5, 0.0]

rend.scene.append( Buffer(triangle) )

isRunning = True

while isRunning: 
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
            
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    deltaTime = clock.tick(60) / 1000.0
    rend.Render()
    
    pygame.display.flip()
    

pygame.quit()

