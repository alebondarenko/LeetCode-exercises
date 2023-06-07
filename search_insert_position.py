# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

from typing import List

class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff == 1:
                return i+1
            elif diff == -1:
                return i-1
        
        return len(nums)+1


solution = Solution()
print(solution.searchInsert(nums = [1,3,5,6], target = 5))
print(solution.searchInsert(nums = [1,3,5,6], target = 2))
print(solution.searchInsert(nums = [1,3,5,6], target = 7))