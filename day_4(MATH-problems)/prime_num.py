# import math 

# def is_prime(n):

#     #check if n is 1 or 0
#     if n <= 1:
#         return False
    
#     #check if n is 2 and 3 
#     if n == 2 and n == 3:
#         return True
    
#     #check wether n is divisble by 2 and 3
#     if n % 2 == 0 or n % 3 == 0:
#         return False 
    
#     #check from 5 to square root of n
#     i=5
#     while i <= math.sqrt(n):
#         if n%i==0 or n%(i+2)==0:
#             return False
#         i += 6

# if __name__ == "__main__":
#     n = 5
#     if(is_prime(n)):
#         print("True")
#     else:
#         print("False")

import math

def isPrime(n):

    # Check if n is 1 or 0
    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return True

    # Check whether n is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check from 5 to square root of n
    # Iterate i by (i+6)
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

if __name__ == "__main__":
  n = 7
  if(isPrime(n)): 
    print("true")
  else:
    print("false")

