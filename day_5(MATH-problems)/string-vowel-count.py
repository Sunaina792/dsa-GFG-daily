from math import factorial
from collections import Counter
class Solution:
    def vowelCount(self, s):
        #code here
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freq = Counter(s)
        
        # Step 1: Find unique vowels in s
        unique_vowels = [v for v in vowels if v in freq]
        if not unique_vowels:
            return 0
            
        # Step 2: Count choices for each vowel
        choices = 1
        for v in unique_vowels:
            choices *= freq[v]
            
        # Step 3: Permutations of selected vowels
        permutations = factorial(len(unique_vowels))
        return choices * permutations
        
s = input()
sol = Solution()
result = sol.vowelCount(s)
print(result)