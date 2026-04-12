"""
CS 211 - Sabrina Zhang 
HW 3 - Kaprekar's Constant 

"""
class Kaprekar:
    kaprekar_constant = 6174 # a class variable or member

    def __init__(self, number):
        # instance members
        self.orginal = number
        self.number = number
        self.digits = 0

    def __repr__(self):
       return f"Number = ({self.number}), Digit = ({self.kaprekar_steps()})"
        
    def __str__(self):
        return f"{self.orginal}"

    def is_kaprekar(self):
        return self.number == Kaprekar.kaprekar_constant

    def largest(self):
        """returns largest integer from digits
        Converts numbers to str and sorted"""
        num = str(self.number)
        sort = sorted(num, reverse = True)
        lg = ""
        for value in sort:
            lg += value
        return int(lg)

    def smallest(self):
        """returns smallest integer from digits
        Converts numbers to str and sorted
        """
        num = str(self.number)
        sort = sorted(num)
        sm = ""
        for value in sort:
            sm += value
        return int(sm)

    def step(self):
        # produces one step in the Kaprekar process
       
        self.number = self.largest() - self.smallest()
        return self.number 

    def kaprekar_steps(self):
        """returns number of steps to reach Kaprekar constant
        stop at 100 to avoid an infinite loop"""

        while not self.is_kaprekar() and self.digits != 100:
            self.step()
            self.digits = self.digits + 1
        if self.digits == 100:
            return self.digits
        return self.digits
        

if __name__ == "__main__":
    print(f"Kaprekar constant: {Kaprekar.kaprekar_constant}")
    n = input("Enter a 4-digit number: ")

    if len(n) != 4 or not n.isdigit():
        print("Please enter a valid 4-digit number.")
        exit(1)
        
    k = Kaprekar(int(n))
    print(k)
    print(repr(k))
    print(f"Number of steps to reach Kaprekar constant: {k.kaprekar_steps()}")
    print(f"Is Kaprekar constant: {k.is_kaprekar()}")
        
   # 5200 -> 7
   # 1234 -> 3
   # 8894 -> 6
   # 5757 -> 6
   # 1111 -> 100
   # 6174 -> 0