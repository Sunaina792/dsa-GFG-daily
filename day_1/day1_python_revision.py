print("Python for dsa")

# Numeric operations 
pi = 3.14159
radius = 7.02
area_of_circle = pi * radius **2
print("Area of circle is :", area_of_circle)

# String operations
message = "this is string"
rev_str = message[::-1]
print("Reversed string is :", rev_str)

# List operations
list = [1,2,3,4,5,6]
sum_of_list = sum(list)
print("Sum of list is :", sum_of_list)
average_of_list = sum_of_list / len(list)
print("average of list :", average_of_list)

#tuple operations
x1 = 4
y1 = 2
x2 = 0
y2 = 0
tuple1= (x1,y1)
tuple2 = (x2, y2)
def distance_from_origin(t1,t2):
    return ((t1[0]-t2[0])**2 + (t1[1]-t2[1])**2)**0.5
print("Distance from origin is :", distance_from_origin(tuple1, tuple2))

#set operations
set1 = {3,2,4,5,7,9}
set2 = {2,4,6,8}

def set_operations(s1, s2):
    set_union = s1.union(s2)
    set_intersection = s1.intersection(s2)
    set_difference = s1.difference(s2)
    return set_union, set_intersection, set_difference

set_union, set_intersection, set_difference = set_operations(set1, set2)
print("Set union:", set_union)
print("Set intersection:", set_intersection)
print("Set difference:", set_difference)

# Dictionary operations
#create a dictionary to count frequency of characters in a string
def char_frequency(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency
string = "sunaina"
frequency_dict = char_frequency(string)
print("Character frequency:", frequency_dict)

## if elif else statments
x = 5
if x > 5:
    print("x is greater than 5")
elif x < 5:
    print("x is less than 5")
else:
    print("x is equal to 5")

# Nested loop
x = 10
y = 1
if x > 5:
    if y > 2:
        print("x is greater than 5 and y is greater than 2")  # This line will be executed
    else:
        print("x is greater than 5 but y is not greater than 2")
else:
    print("x is not greater than 5")

# determining sign numbers
def sign_num(x):
    if x >0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"
print("Sign of number is:", sign_num(10)) 
print("Sign of number is:", sign_num(-5))  
print("Sign of number is:", sign_num(0))   

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(1, 5):
     print(i)

# while loops
i = 1
while i < 5:
    print(i)
    i += 1

# break and continue statements
for i in range(10):
    if i == 3:
        break  
    print(i)  

for i in range(5):
    if i == 2:
        continue  
    print(i) 

# eg-- calculate sun of numbers
def sum_num(n):
    total = 0
    for i in range(1,n+1):
        total += i
    return total
print("Sum of numbers from 1 to 5 is:", sum_num(6))  

#List comprehensions
squares = []
for i in range(10):
    squares.append(i * i)
print("Squares of numbers from 0 to 9:", squares)

squares_comp = [i * i for i in range(10)]
print("Squares of numbers from 0 to 9 using list comprehension:", squares_comp)

even_squares = [i * i for i in range(10) if i % 2 == 0]
print("Squares of even numbers from 0 to 9 using list comprehension:",even_squares) 
