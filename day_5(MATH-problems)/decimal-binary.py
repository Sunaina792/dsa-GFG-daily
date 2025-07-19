#decimal to binary conversion

def dectoBinary(n):
    binArr = []

    while n > 0:
        bit = n % 2
        binArr.append(str(bit))
        n //= 2

    # reverse the array
    binArr.reverse()
    return"".join(binArr)

n = int(input("binary number:"))
print(dectoBinary(n))

# using recursion

def dectobinrec(n, binArr):
    if n == 0:
        return
    
    dectobinrec(n // 2, binArr)

    binArr.append(str(n % 2))

def dectobinary(n):
    if n ==0:
        return "0"
    binArr =[]
    dectobinrec(n, binArr)
    return"".join(binArr)
n = int(input("binary number using recurtion:"))
print(dectobinary(n))

#builtin mathod
import math

def dec_binary(n):
    return bin(n)[2::]
n = int(input("binary number using builtin function:"))
print(dectobinary(n))