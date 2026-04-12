class Add:
    def __init__(self, x, y, z):
        self.sum = x + y + z 

x = Add(1, 2, 3)
y = x.sum
x.sum = y + 1
print(x.sum)

class A:
    def m1(self):
        return self.m2()
    def m2(self):
        return "A"
    
class B(A):
    def m2(self):
        return "B"
    
a = A()
b = B()
print(a.m1(), b.m1(),a.m2(), b.m2())


a = 1
b = 0
index = 7
a_list = [1,2,3]
try:  
    c = a/b
    print(a_list[index])
except IndexError as e:
    print("Index out of range")
    
except ZeroDivisionError as z:
    print("b is 0")
    
    
x = [1,2,3]
x.append([4,5,6])
print(len(x))