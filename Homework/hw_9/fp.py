"""
CS 211 - Sabrina Zhang
HW 9 - Data transformation functional programming
"""

from functools import reduce

data = [1, 5, 8, 12, 15, 20, 23, 28, 30, 35, 40]

def is_divisible_by_four(number):
    return (number % 4) == 0

def half_value(number):
    return number / 2

filtered_data = list(filter(is_divisible_by_four, data))

transformed_data = list(map(half_value, filtered_data))

final_sum = reduce(lambda x , y: x + y, transformed_data)

print("Filtered Data:", filtered_data)
print("Transformed Data", transformed_data)
print("Final Sum:", final_sum)

# Reflection
"""
A pure function return will always return the value
as is after a specific change. The result will never 
change any value outside of the function and will 
always return one thing and the same thing every time.

Filter uses the is_divisible_by_four pure function
and returns the value only if the item in the
function returns true.
    
Map applies the function half_value() to every item
in the list in this case its stored in filtered_data. 
By type casting the map object a list, map will
iterate through the item lists and return the
value with the function applied. 

Final sum returns a value. 
Lambda in this case serves as the temporary function
where it will take the sum of each element x and y 
and calculate the sum. The reduced function helps it 
iterate along the list.
"""

