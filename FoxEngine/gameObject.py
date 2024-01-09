from dataTypes import *
from texture import *


class gameObject:
    name: str
    objectSize = Vector2(0,0)
    objectPosition = Vector2(0,0)
    color = Color(1,0,1,1)
    texture = Texture2D(2,2,Color(1,0,1))
    
    topLeft     = Vector2(0,0)
    topRight    = Vector2(0,0)
    bottomLeft  = Vector2(0,0)
    bottomRight = Vector2(0,0)
    
    
    
    
    def UpdateBounds(self) -> None:
        self.topLeft = Vector2(self.objectPosition.x(),self.objectPosition.y()+self.objectSize.y())
        self.topRight = Vector2(self.objectPosition.x()+self.objectSize.x(),self.objectPosition.y()+self.objectSize.y())
        self.bottomLeft = Vector2(self.objectPosition.x(),self.objectPosition.y())
        self.bottomRight = Vector2(self.objectPosition.x()+self.objectSize.x(),self.objectPosition.y())
        
    def __init__(self, name: str, objectSize: Vector2, objectPosition: Vector2, color: Color) -> None:
        self.name = name
        self.objectSize = objectSize
        self.objectPosition = objectPosition
        self.color = color
        
        self.UpdateBounds()
        pass
