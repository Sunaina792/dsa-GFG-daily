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

