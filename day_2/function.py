## function
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
a=20876
b=47584
print("Sum of", a, "and", b, "is:", add(a, b))

def factorial(n):
    """ factorial of number"""
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
num = 7
print(f"Factorial of {num} is:", factorial(num))

##*args and **kwargs
def  sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))

def describe(name, **kwargs):
    print(f"name:{name}")
    for key, value in kwargs.items():
        print(f"{key}:{value}")
describe("mia", age=18, city="New York")

# lambda function
square_lambda = lambda x: x * x
print("Square of 5 using lambda function:", square_lambda(5))

num = [1,2,3,4]
sq_num = list(map(lambda x: x * x, num))
print("Squares of numbers using map and lambda:", sq_num)

## modules
import math
print(math.fsum([3,6]))

def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

x = 10
y = 5       
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
