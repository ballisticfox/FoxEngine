from dataTypes import *
class gameObject:
    objectSize = Vector2(0,0)
    objectPosition = Vector2(0,0)
    
    topLeft: Vector2(0)
    topRight: Vector2(0)
    bottomLeft: Vector2(0)
    bottomRight: Vector2(0)
    
    def UpdateBounds(self) -> None:
        self.topLeft = Vector2(self.objectPosition.x,self.objectPosition.y+self.objectSize.y)
        self.topRight = Vector2(self.objectPosition.x+self.objectSize.x,self.objectPosition.y+self.objectSize.y)
        self.bottomLeft = Vector2(self.objectPosition.x,self.objectPosition.y)
        self.bottomRight = Vector2(self.objectPosition.x+self.objectSize.x,self.objectPosition.y)
        
    def __init__(self, objectSize: Vector2, objectPosition: Vector2) -> None:
        pass
