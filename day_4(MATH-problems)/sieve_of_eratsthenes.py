### What is the Sieve of Eratosthenes?
# It’s an efficient algorithm to find all prime numbers up to a given number n.
# Instead of checking each number one by one like isPrime, 
# this method marks the multiples of each prime number as non-prime, starting from 2.

def sieve(n):
    prime = [True] * (n+1)
    p = 2

    #Sieve of Eratosthenes algorithm
    while p * p <= n:
        if prime [p]:
            for i in range( p*p, n+1, p):
                prime [i]=False
        p += 1
    
    result = []
    for p in range(2, n+1):
        if prime[p]:
            result.append(p)
    return result
    
if __name__ == "__main__":
    n = 35
    result = sieve(n)
    for element in result:
        print(element, end=" ")


# def sieve(n):
   
#     #Create a boolean list to track prime status of numbers
#     prime = [True] * (n + 1)
#     p = 2

#     # Sieve of Eratosthenes algorithm
#     while p * p <= n:
#         if prime[p]:
            
#             # Mark all multiples of p as non-prime
#             for i in range(p * p, n + 1, p):
#                 prime[i] = False
#         p += 1

#     # Collect all prime numbers
#     res = []
#     for p in range(2, n + 1):
#         if prime[p]:
#             res.append(p)
    
#     return res

# if __name__ == "__main__":
#     n = 35
#     res = sieve(n)
#     for ele in res:
#         print(ele, end=' ')