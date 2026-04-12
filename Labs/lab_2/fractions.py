"""Fractions - Lab 2
Sabrina Zhang, 2025-04-16, CS 211
"""
def gcd(a, b): 
    "Finds Greatest Common denominator"
    if a> b:
        a, b = b,a
            
    elif a == 0:
        return abs(b)
    return gcd(a, b - a)

class Fraction:
    """
    Simplifies and applies operations
    addition and multiplication
    """
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den
        assert self.num or self.den != 0   
        self.simplify() 
      
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self, other:"Fraction"):
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        return  Fraction(num, den)
    
    def __mul__(self, other: "Fraction"):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def simplify(self):
        gc = gcd(self.num,self.den)
        self.num = self.num // gc
        self.den = self.den // gc
        
if __name__ == "__main__":
    f1 = Fraction(6,10)
    f2 = Fraction(1,2)
    print(f"{f1} + {f2} = {f1 + f2}")
    print(f"{f1} * {f2} = {f1 * f2}")
    new_f = Fraction(6,10)
    print(f"new_f = {new_f}")
    
    
    