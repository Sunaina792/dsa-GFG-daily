def floorDiv(a, b):
    
    # Python's // operator gives correct floor division
    return a // b

# Method to compute ceil of a / b
def ceilDiv(a, b):
    
    # Flip signs to force ceiling behavior
    return -(-a // b)

# Method to compute both floor and ceil of a / b
def divFloorCeil(a, b):
    res = []
    res.append(floorDiv(a, b))
    res.append(ceilDiv(a, b))
    return res

if __name__ == "__main__":
    a = int(input("floor:"))
    b = int(input("ceil:"))
    res = divFloorCeil(a, b)
    print(res[0], res[1])

# Function to compute floor and ceil division with builin functions
import math

def divFloorCeilBuiltIn(a, b):
    floor_val = math.floor(a/b)
    Ceil_val = math.ceil(a/b)

a =int(input("floor-no:"))
b = int(input("ceil-no:"))
res = divFloorCeil(a,b)
print(res[0], res[1])