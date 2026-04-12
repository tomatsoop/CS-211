"""Homework 1: Euclidean distances class Point3D
   Sabrina Zhang, 2025-04-03 CS 211
   """

class Point3D:
    """Calculates euclidean distance given 2 sets of points in the 3rd dimension.
    def __init__(self, a:int, b:int, c:int):
        class constructor method __init__ to establish points a, b, c
    
    def euclidean_distance(self, other: "Point3D"):
        calculates the distance**2 of point1(self) and point2(other)
        returns the squareroot of distance
        
    def __str__(self) ->:
        returns string formatting of self.a , self.b , self.c
    
    """
    def __init__(self, a:int, b:int, c:int):
        self.a = a 
        self.b = b
        self.c = c
        
    def __str__(self) -> str:
        return f"{self.a}, {self.b}, {self.c}"
    
    def euclidean_distance(self, other: "Point3D"):
        distance = (self.a - other.a)**2 + (self.b - other.b)**2 + (self.c - other.c)**2
        return distance ** 0.5
    
if __name__ == "__main__":
    p1 = Point3D(1, 2, 3)
    p2 = Point3D(4, 5, 6)
    print(f"Distance between Point3D({p1}) and Point3D({p2}:{p1.euclidean_distance((p2))})")
    
    p3 = Point3D(0, 0, 0)
    print(f"Distance between Point3D({p3}) and itself: {p3.euclidean_distance(p3)}")
    
    p4 = Point3D(-1, -2, -3)
    p5 = Point3D(-4, -5, -6)
    print(f"Distance between Point3D({p4}) and itself: {p4.euclidean_distance(p5)}")
