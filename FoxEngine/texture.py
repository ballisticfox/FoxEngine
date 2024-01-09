import numpy
from dataTypes import *

class Texture2D:
    texture : numpy.empty((2, 2), Color)
    Width : int
    Height : int
    
    def toPixelValue(v: float) -> int:
        return v*255
    
    def CheckBounds(self, x: int, y: int):
        if x < 0:
            x = 0
            
        elif x > self.Width:
            x = self.Width
        
        if y < 0:
            y = 0
            
        elif y > self.Height:
            y = self.Height
        
        return x, y
    
    def SetPixel(self, x: int, y: int, color: Color):
        ExistingColor: Color
        NewColor : Color
        
        ExistingColor = self.texture[y][x]
        
        
        NewColor = Color(
            ExistingColor.r()*(1-color.a())+color.r()*(color.a()),
            ExistingColor.g()*(1-color.a())+color.g()*(color.a()),
            ExistingColor.b()*(1-color.a())+color.b()*(color.a())
            )
        
        #print(color.GetColor().GetTuple())
        print(NewColor.GetTuple())
        print(color.a())
        self.texture[y][x] = NewColor
    
    def GetPixel(self, x: int, y: int) -> Color:
        x, y = self.CheckBounds(x, y)
        color: Color
        color = self.texture[y][x]
        
        return color.GetTuple255()
    
    def FillTexture(self, color: Color):
        for y in range(0,self.Height):
            for x in range(0,self.Width):
                self.texture[y][x] = color.GetColor()
    
    def __init__(self, Width: int, Height: int, FillColor: Color) -> None:
        Width = max(Width,2)
        Height = max(Width,2)
        
        self.Width = Width
        self.Height = Height
        self.texture = numpy.empty((self.Height, self.Width), dtype=Color)
        self.FillTexture(FillColor)