import pygame
from gameObject import *
from texture import Texture2D
from dataTypes import *

class main:
    
    ###GLOBAL VARIABLES###
    screenResX = 480
    screenResY = 270
    aspectRatio = screenResX/screenResY
        
    screenMinX = -4
    screenMaxX = 4
        
    screenMinY = -4
    screenMaxY = 4
    
    screenRangeX = screenMaxX-screenMinX
    screenUnitX = screenResX/screenRangeX

    screenRangeY = screenMaxY-screenMinY
    screenUnitY = screenResY/screenRangeY
    
    
    def WorldToPixel(self, x, y):
        uvX = (x+abs(self.screenMinX))/self.screenRangeX
        pixelX = int(self.screenResX*uvX)
        
        uvY = (y*self.aspectRatio+abs(self.screenMinY/self.aspectRatio))/self.screenRangeY
        pixelY = int(self.screenResY*uvY)

        return tuple((pixelX,pixelY))

        
    ###     MAIN    ###
    def main(self):
        pygame.init()  # Start Pygame

        

        screen = pygame.display.set_mode((self.screenResX, self.screenResY))  # Start the screen
        running = True

        White = Color(1,1,1)
        Black = Color(0,0,0)
        Red   = Color(1,0,0)
        Green = Color(0,1,0,0.3)
        Error = Color(1,0,1)
        
        
        Buffer = Texture2D(self.screenResX,self.screenResY, Black)
        
        for x in range(0,self.screenResX):
            Buffer.SetPixel(x,int(self.screenResY/2),Green)
        
        cube = gameObject("cube", objectSize = Vector2(1,1), objectPosition = Vector2(0,0), color = Color(1,0,0))
        
        #for y in range(objectBottomRightCorner[1],objectTopLeftCorner[1]):
        #    for x in range(objectTopLeftCorner[0],objectBottomRightCorner[0]):
        #        Buffer.SetPixel(x,y,Red)


        #print(objectTopLeftCorner)
        #print(objectBottomRightCorner)
                
        while running:
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