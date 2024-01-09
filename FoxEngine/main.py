import pygame
from gameObject import *
from texture import *
from dataTypes import *

class main:



        
    ###     MAIN    ###
    def main(self):
        pygame.init()  # Start Pygame


        ###DEFAULT COLORS###
        White = Color(1,1,1)
        Gray = Color(0.5,0.5,0.5)
        Black = Color(0,0,0)
        Red   = Color(1,0,0)
        Green = Color(0,1,0,0.3)
        Error = Color(1,0,1)
        
        
        sceneObjects = []
        gameScreen = Screen(480,270,Vector2(-4,4),Vector2(-4,4))
    
        screen = pygame.display.set_mode((gameScreen.screenResX, gameScreen.screenResY))  # Start the screen
        running = True
  
        Buffer = Texture2D(gameScreen.screenResX,gameScreen.screenResY, Gray)
        
        #Random Line
        for x in range(0,gameScreen.screenResX):
            Buffer.SetPixel(x,int(gameScreen.screenResY/2),Green)
        
        cubeRed = gameObject(gameScreen, "cube", objectSize = Vector2(0.65,1), objectPosition = Vector2(0,0), color = Color(0,0,1,0.5))
        sceneObjects.append(cubeRed)
        
        cubeGreen = gameObject(gameScreen, "cube", objectSize = Vector2(0.5,1), objectPosition = Vector2(0.5,0), color = Color(1,1,1,0.5))
        sceneObjects.append(cubeGreen)

        cubeBlue = gameObject(gameScreen, "cube", objectSize = Vector2(0.65,1), objectPosition = Vector2(0.85,0), color = Color(1,0,0,0.5))
        sceneObjects.append(cubeBlue)
                
        while running:
            
            for object in sceneObjects:
                for y in range(object.pixelBottom, object.pixelTop):
                    for x in range(object.pixelLeft, object.pixelRight):
                        Buffer.SetPixel(x,y,object.color)
            
            
            ###BUFFER TO SCREEN###
            for y in range(0,Buffer.Height):
                for x in range(0,Buffer.Width):
                    screen.set_at((x,y), Buffer.GetPixel(x,y))
                    #pygame.draw.rect(screen, , pygame.Rect(x,y,1,1))
    
            ##Update after every line
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # The user closed the window!
                    running = False  # Stop running
            pygame.display.flip()
            
            
            # No game logic for simple window needed
        pygame.quit()  # Close the window
    
    

GameLogic = main()
GameLogic.main()