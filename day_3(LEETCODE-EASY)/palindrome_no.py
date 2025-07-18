class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        original = x
        reversed_num = 0

        while x != 0:
            digit = x % 10 
            reversed_num = reversed_num * 10 + digit
            x = x//10

        return original == reversed_num
    
# Example usage:
solution = Solution()
print(solution.isPalindrome(121))  
print(solution.isPalindrome(-121)) 
print(solution.isPalindrome(10))   