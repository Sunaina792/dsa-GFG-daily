class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash={}
        for i in range(len(nums)):
            if target - nums[i] in num_hash:
                return [num_hash[target - nums[i]], i]
            num_hash[nums[i]]=i
        return []
# Example usage:
solution = Solution()     
print(solution.twoSum([2, 7, 11, 15], 9)) 
print(solution.twoSum([3, 2, 4], 6))         

