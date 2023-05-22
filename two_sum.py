from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []

print(Solution().twoSum(nums = [3,2,4], target = 6))

for i, num in enumerate([3,2,4]):
    print(i, num)

