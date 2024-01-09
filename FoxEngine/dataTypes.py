import math

class Vector2:
    xy = tuple((0,0))
    x = 0.0
    y = 0.0
    
    def __init__(self, x: float, y: float) -> None:
        self.xy = tuple((x,y))
        self.x = x
        self.y = y
    
    def SetVector(self, x: float, y: float) -> None:
        self.xy = tuple((x,y))
        self.x = x
        self.y = y
    
    def Length(self) -> float:
        return math.sqrt(math.pow(self.x(), 2)+math.pow(self.y(), 2))
        

class Color:
    color = tuple((0,0,0,0))
    
    def __init__(self, r: float, g: float, b: float, a = 1.0) -> None:
        
        self.color = tuple((r,g,b,a))
    
    #Returns the red value of the color
    def r(self) -> float:
        return self.color[0]
    
    #Returns the green value of the color
    def g(self) -> float:
        return self.color[1]
    
    #Returns the blue value of the color
    def b(self) -> float:
        return self.color[2]
    
    def a(self) -> float:
        return self.color[3]
    
    def SetColor(self, r: float, g: float, b: float, a: 1.0) -> None:
        self.color = tuple((r,g,b,a))
    
    def GetColor(self): #-> Color
        r = self.r()
        g = self.g()
        b = self.b()
        return Color(r,g,b)
    
    def GetTuple(self) -> tuple:
        r = self.r()
        g = self.g()
        b = self.b()
        return tuple((r,g,b))
    
    def GetTuple255(self) -> tuple:
        r = self.r()*255
        g = self.g()*255
        b = self.b()*255
        return tuple((r,g,b))
    