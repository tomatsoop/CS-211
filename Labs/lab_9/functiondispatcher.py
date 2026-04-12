""" Lab 07 Functions as arguments
    Harsha Siddagangaiah
"""
import math
from typing import List, Callable


def total_sum(list1: List[int]):
    return sum(list1)

def apply(fun: Callable, list1: List[int]):
    return [fun(i) for i in list1]

def square(list1: List[int]):
    sq = lambda x : x ** 2
    a = apply(sq, list1)
    return a

def magnitude(vector: List[int]):
    squared = square(vector)
    total = total_sum(squared)
    return math.sqrt(total)

class FunctionDispatcher:

    def __init__(self, dispatch_table: dict):
        self.dispatch_table = dispatch_table

    def process_command(self, key: int, list1: List[int]):
        func = self.dispatch_table[key]
        return func(list1)
    
if __name__ == '__main__':
    dispatch_table = {
        1: total_sum, 2: square, 3: magnitude 
    }
    fd = FunctionDispatcher(dispatch_table)
    print(fd.process_command(1, [3, 4]))
    print(fd.process_command(2, [3, 4]))
    print(fd.process_command(3, [3, 4]))
