import pygame
import keyboard
from gameObject import *
from texture import *
from dataTypes import *

class main:
    ###     MAIN    ###
    @staticmethod
    def main():
        pygame.init()  # Start Pygame


        ###DEFAULT COLORS###
        
        sceneObjects = []
        gameScreen = Screen(480,270,Vector2(-4,4),Vector2(-4,4))
        RawAxis = Vector2(0,0)
        screen = pygame.display.set_mode((gameScreen.screenResX, gameScreen.screenResY))  # Start the screen
        running = True
  
        Buffer = Texture2D(gameScreen.screenResX,gameScreen.screenResY, ColorTypes.BLACK)
        
        #Random Line

        #cubeYellow = gameObject(gameScreen, "cube", objectSize = Vector2(5,5), objectPosition = Vector2(-2,0), color = ColorTypes.YELLOW)
        #sceneObjects.append(cubeYellow)
        
        cubeRed = gameObject(gameScreen, "cube", objectSize = Vector2(1,1), objectPosition = Vector2(0,0), color = ColorTypes.RED)
        sceneObjects.append(cubeRed)
        
        xLine = gameObject(gameScreen, "cube", objectSize = Vector2(gameScreen.screenLengthX,0.01), objectPosition = Vector2(gameScreen.screenRangeX.x,-0.005), color = ColorTypes.MAGENTA)
        sceneObjects.append(xLine)
                
        while running:
            
            print(Input.GetAxisRaw().xy)

                
            ### OBJECTS TO BUFFER ###
            for object in sceneObjects:
                for y in range(object.pixelTop, object.pixelBottom):
                    for x in range(object.pixelLeft, object.pixelRight):
                        Buffer.SetPixel(x,y,object.color)
            
            
            ### BUFFER TO SCREEN ###
            for y in range(0,Buffer.Height):
                for x in range(0,Buffer.Width):
                    screen.set_at((x,y), Buffer.GetPixel(x,y))
    
            ### INPUT LOGGING ###
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # The user closed the window!
                    running = False  # Stop running
            pygame.display.flip()
            
            
        pygame.quit()
    
    

GameLogic = main()
GameLogic.main()