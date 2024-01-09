from dataTypes import *
from texture import *

class Screen:
    screenResX: int
    screenResY: int
    aspectRatio: float
    
    screenRangeX: Vector2
    screenRangeY: Vector2
    
    screenLengthX: float
    screenLengthY: float
    
    def WorldToPixel(self, x: float, y: float) -> tuple:
        uvX = (x+abs(self.screenRangeX.x))/self.screenLengthX
        pixelX = int(self.screenResX*uvX)
        
        uvY = (y*self.aspectRatio+abs(self.screenRangeX.y/self.aspectRatio))/self.screenLengthY
        pixelY = int(self.screenResY*uvY)

        return tuple((pixelX,pixelY))
    
    def UpdateRanges(self):
        self.screenLengthX = self.screenRangeX.y-self.screenRangeX.x
        self.screenLengthY = self.screenRangeY.y-self.screenRangeY.x
        
    def UpdateAspectRatio(self):
        self.aspectRatio = self.screenResX/self.screenResY
        
    def __init__(self, screenResX: int, screenResY: int, screenX: Vector2, screenY: Vector2) -> None:
        self.screenResX = screenResX
        self.screenResY = screenResY
        self.screenRangeX = screenX
        self.screenRangeY = screenY
        
        self.UpdateRanges()
        self.UpdateAspectRatio()
        
    

class gameObject:
    screenData: Screen
    name: str
    objectSize     = Vector2(0,0)
    objectPosition = Vector2(0,0)
    color          = Color(1,0,1,1)
    texture        = Texture2D(2,2,Color(1,0,1))
    
    top    = 0.0
    left   = 0.0
    right  = 0.0
    bottom = 0.0
    
    pixelTop    = 0
    pixelLeft   = 0
    pixelRight  = 0
    pixelBottom = 0
    
    
    def UpdateBounds(self) -> None:
        self.top     = (self.objectPosition.y+self.objectSize.y)
        self.bottom  = (self.objectPosition.y)
        self.left    = (self.objectPosition.x)
        self.right   = (self.objectPosition.x+self.objectSize.x)
        
        TopLeft = self.screenData.WorldToPixel(self.left,self.top)
        BottomRight = self.screenData.WorldToPixel(self.right, self.bottom)
        
        self.pixelLeft = TopLeft[0]
        self.pixelRight = BottomRight[0]
        self.pixelTop = TopLeft[1]
        self.pixelBottom = BottomRight[1]
        
    def __init__(self, screen: Screen, name: str, objectSize: Vector2, objectPosition: Vector2, color: Color) -> None:
        self.screenData = screen
        self.name = name
        self.objectSize = objectSize
        self.objectPosition = objectPosition
        self.color = color
        
        self.UpdateBounds()
        pass
