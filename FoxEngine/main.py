import pygame
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
        gameScreen = Screen(160,144,Vector2(-4,4),Vector2(-4,4))
        screen = pygame.display.set_mode((gameScreen.screenResX, gameScreen.screenResY))  # Start the screen
        running = True
  
        Buffer = Texture2D(gameScreen.screenResX,gameScreen.screenResY, ColorTypes.BLACK)
        

        #cubeYellow = gameObject(gameScreen, "cube", objectSize = Vector2(5,5), objectPosition = Vector2(-2,0), color = ColorTypes.YELLOW)
        #sceneObjects.append(cubeYellow)
        
        backdrop = gameObject(gameScreen, "backdrop", objectSize = Vector2(gameScreen.screenLengthX,gameScreen.screenLengthY), objectPosition = Vector2(gameScreen.screenRangeX.x,gameScreen.screenRangeY.x), color = ColorTypes.BLACK)
        sceneObjects.append(backdrop)
        
        Ball = gameObject(gameScreen, "Ball", objectSize=Vector2(0.45,0.45), objectPosition=Vector2(0,0), color = ColorTypes.GREEN)
        sceneObjects.append(Ball)
        
        LPaddle = gameObject(gameScreen, "leftPaddle", objectSize = Vector2(0.25,1.25), objectPosition = Vector2(-3,-1.25), color = ColorTypes.WHITE)
        LPaddle.AddPlayerController(Vector2(0,0.35),1)
        sceneObjects.append(LPaddle)
                
        RPaddle = gameObject(gameScreen, "rightPaddle", objectSize = Vector2(0.25,1.25), objectPosition = Vector2(2.75,-1.25), color = ColorTypes.WHITE)
        RPaddle.AddPlayerController(Vector2(0,0.35),2)
        sceneObjects.append(RPaddle)

        
        #xLine = gameObject(gameScreen, "xAxisLine", objectSize = Vector2(gameScreen.screenLengthX,0.1), objectPosition = Vector2(gameScreen.screenRangeX.x,-0.005), color = ColorTypes.MAGENTA)
        #sceneObjects.append(xLine)
                
        while running:
            
            PreFrameTime = Timing.current_milli_time()
            ### OBJECTS TO BUFFER ###
            PreAllObjectsToBufferTime = Timing.current_milli_time()
            
            
            
            for object in sceneObjects:
                object.UpdateScreen(gameScreen)
                if (object.playerController == True and object.playerChannel == 1):
                    object.PlayerMovement(Input.GetAxisRaw("w","a","s","d"))
                
                if (object.playerController == True and object.playerChannel == 2):
                    object.PlayerMovement(Input.GetAxisRaw("up","left","down","right"))
                
                for y in range(object.pixelTop, object.pixelBottom):
                    for x in range(object.pixelLeft, object.pixelRight):
                        Buffer.SetPixel(x,y,object.color)
                        

            PostAllObjectsToBufferTime = Timing.current_milli_time()
            print("Objects to buffer time: " + str((PostAllObjectsToBufferTime-PreAllObjectsToBufferTime))+"ms")
            
            ### BUFFER TO SCREEN ###
            PreScreenDrawTime = Timing.current_milli_time()
            for y in range(0,Buffer.Height):
                for x in range(0,Buffer.Width):
                    screen.set_at((x,y), Buffer.GetPixel(x,y))
            PostScreenDrawTime = Timing.current_milli_time()
            
            print("Screen Draw time: " + str((PostScreenDrawTime-PreScreenDrawTime))+"ms")
            
            
            ### INPUT LOGGING ###
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # The user closed the window!
                    running = False  # Stop running
            pygame.display.flip()
            
            PostFrameTime = Timing.current_milli_time()
            print("Frame time: " + str((PostFrameTime-PreFrameTime))+"ms")
            
        pygame.quit()
    
    

GameLogic = main()
GameLogic.main()