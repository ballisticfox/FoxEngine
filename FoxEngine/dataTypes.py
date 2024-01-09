import math

class Vector2:
    vector = tuple((0,0))
    
    def __init__(self, x: float, y: float) -> None:
        self.vector = tuple((x,y))
        
    def x(self) -> float:
        return self.vector[0]
    
    def y(self) -> float:
        return self.vector[1]
    
    def GetVector(self) -> tuple:
        return self.vector
    
    def Length(self) -> float:
        print()
        return math.sqrt(math.pow(self.x(), 2)+math.pow(self.y(), 2))
        

class Color:
    color = (0,0,0)
    
    def __init__(self, r: float, g: float, b: float) -> None:
        
        self.color = tuple((r,g,b))
        
    def r(self):
        return self.color[0]
    
    def g(self):
        return self.color[1]
    
    def b(self):
        return self.color[2]
    
    def SetColor(self, r: float, g: float, b: float) -> None:
        self.color = tuple((r,g,b))
    
    def GetColor(self):
        r = self.r()
        g = self.g()
        b = self.b()
        return Color(r,g,b)
    
    def GetTuple(self):
        r = self.r()
        g = self.g()
        b = self.b()
        return tuple((r,g,b))
    
    def GetTuple255(self):
        r = self.r()*255
        g = self.g()*255
        b = self.b()*255
        return tuple((r,g,b))
    