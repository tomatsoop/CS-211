"""Closed intervals of intergers
Sabrina Zhang, 2025-04-02, CS 211
"""

import doctest

class Interval:
    """An interval [m..n] represents the set of intergers
    from m to n.
    
    Every class must start with a constructor using __init__
    """
    
    
    def __init__(self, low: int, high: int):
        """Interval(low, high) represents the interval 
        [low..high]

        Returns ValueError if self.low is greater than self.high 
        """
        self.low = low 
        self.high = high
        if low > high:
           return ValueError
    
   
    def contains(self, i:int) -> bool:
        """Interger i is within the closed interval
        
        >>> Interval(-1,1).contains(0)
        True
        >>> Interval(3,6).contains(7)
        False
        """
        if i >= self.low and i <= self.high:
            return True
        else:
            return False
        
    def overlaps(self, other: "Interval") -> bool:
        """i.overlaps(j) iff i and j have some elements in common
        
        >>> Interval(0,2).overlaps(Interval(-1,5))
        True
        >>> Interval(-1,2).overlaps(Interval(3,5))
        False
        """        
        if self.low <= other.high and self.high >= other.low:
            return True
        else:
            return False
        
    def __eq__(self, other : "Interval") -> bool:
        """Intervals are equal if they the same low and high bounds
        
        .__eq__ can be used but it means == and is redundent

        >>> Interval(3,5) == Interval(3,4)
        False
        >>> Interval(3,5) == Interval(3,5)
        True
        >>> Interval(3,5).__eq__(Interval(3,5))
        True
        """
        return self.low == other.low and self.high == other.high
    
    def join(self, other: "Interval") -> "Interval":
        """Create a new Interval thhat contains the union of
        elements in self and other
        Pre condition: self and other must overlap
        
        assert(self.overlaps(other)) checks if overlaps returns
        True and runs. Otherwise False and does not run
        
        >>> print(Interval(3,4).join(Interval(3,7)))
        [3..7]
        """
        assert(self.overlaps(other)) 
        return Interval(min(self.low, other.low), 
                        max(self.high, other.high))
        # Make sure  to return interval calss and not tuple
    
    def __str__(self) -> str: # this  makes it readable
        """Builtin Functions do not need to be called. 
        For String use print()
        
        >>> print(Interval(3,5))
        [3..5]
        """
        return f"[{self.low}..{self.high}]"
    
    def __repr__(self): 
        """This is a reference for the programmer
        
        >>> import intervals # this is file name
        >>> i = intervals.Interval(3,5) # module call like turtle.Turtle()
        >>> i
        Interval(3,5)
        """
        return(f"{__class__.__name__}({self.low},{self.high})")

if __name__ == "__main__":
    print(doctest.testmod())