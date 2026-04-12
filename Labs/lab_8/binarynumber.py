""" 
CS 211 - Sabrina Zhang
Lab 8 - Binary Numbers

"""
from typing import List

class BinaryNumber:

    def __init__(self, bits: List[int]):
        self.bits = bits
    
    def __str__(self):
        return f"{self.bits}"
    
    def __or__(self, other):
        b1 = self.bits
        b2 = other.bits
        new = []
        for i in range(len(b1)):
            if b1[i] or b2[i] == 1:
                new.append(1)
            else:
                new.append(0)  
        return BinaryNumber(new)
    
    def __and__(self, other):
        other = other.bits
        b1 = self.bits
        b2 = other
        new = []
        for i in range(len(b1)):
            if b1[i] == b2[i]:
                new.append(1)
            else:
                new.append(0)
                
        return BinaryNumber(new)
        
    def left_shift(self):
        self.bits.pop(0)
        self.bits.append(0)
        
    def right_shift(self):
        self.bits.pop()
        self.bits.insert(0,0)

    def extract(self, start: int, end: int):
        lst = []
        
        length = len(self.bits)
        for i in range(length):
            if i in range(start, end + 1):
                lst.append(1)
            else:
                lst.append(0)
                
        bt = BinaryNumber(lst)
        bits = self.__and__(bt)
        
        for i in range(len(bits.bits)):
            if bits.bits[-1] == 1:
                break
            bt.right_shift()
            bits.right_shift()
        
        return BinaryNumber(bits)
                
            
if __name__ == "__main__":
    # execute and verify

    bn = BinaryNumber([1, 0, 1, 0, 1])
    bn2 = BinaryNumber([1, 1, 1, 0, 0])

    print("1st binary number =", bn)

    print("2nd binary number =", bn2)
    print("AND", bn & bn2)
    
    print("OR", bn | bn2)

    bn.right_shift()
    print("1st number right-shifted =", bn)

    bn.left_shift()
    print("1st number left-shifted =", bn)
    
    bn = BinaryNumber([1, 0, 0, 1, 0, 1, 1, 1])
    extracted = bn.extract(2, 4)
    print(extracted)