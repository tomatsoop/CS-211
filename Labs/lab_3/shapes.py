"""Shapes and Classes - Lab 3
Sabrina Zhang, 2025-04-16, CS 211
"""

import math

class Shape3D:
    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")
    
    def volume(self) -> float: 
        raise NotImplementedError("Not implemented for abstract class")
    
    def area(self) -> float:
        raise NotImplementedError("not implemeted for abstract class")
    
    def print_info(self):
        return f"Area: {self.area()}, Volume:{self.volume()}"
        
class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        
    def volume(self):
        volume = self.height* math.pi*(self.radius)**2
        return volume
        
    def area(self):
        area= 2*math.pi*self.radius**2 + 2*math.pi*self.radius*self.height
        return area
    
class Cuboid(Shape3D):
    def __init__(self, width, length, height) -> float:
        self.width = width
        self.length = length
        self.height = height
        
    def volume(self):
        volume = self.width * self.length * self.height
        return volume
    
    def area(self):
        lw = self.width * self.length 
        wh = self.width * self.height
        lh = self.length * self.height
        area = 2* (lw + wh + lh)
        return area

class Cube(Cuboid):
    def __init__(self, dim):
        super().__init__(dim, dim, dim)
            

if __name__ == "__main__":
    cyl = Cylinder(3,5)
    cuboid = Cuboid(6,4,9)
    lst = [Cube(3), cyl, cuboid]
    for shape in lst:
        print(shape.print_info())
        
