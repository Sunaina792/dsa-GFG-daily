from math import gcd

class Solution:
    def lcm(self, a, b):
        return (a * b) // gcd(a, b)
    
    def lcmTriplet(self, a, b, c):
        return self.lcm(a, self.lcm(b, c))
    
    def lcmTriplets(self, n):
        if n <= 2:
            return n
        if n % 2 != 0:
            return self.lcmTriplet(n, n - 1, n - 2)
        else:
            return max(
                self.lcmTriplet(n, n - 1, n - 3),
                self.lcmTriplet(n - 1, n - 2, n - 3)
            )
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    sol = Solution()
    result = sol.lcmTriplets(n)
    print(result)