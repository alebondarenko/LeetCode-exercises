class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for x in nums[:]:
            if x == val:
                nums.remove(x)
        return len(nums), nums

    def removeElement1(self, nums, val):
        """
        more efficient solution
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
    
    def removeElement2(self, nums, val):
        nums[:] = [x for x in nums if x != val]
        return len(nums), nums


solution = Solution()

print(solution.removeElement(nums = [3,2,2,3], val = 3))
print(solution.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
print()
print(solution.removeElement1(nums = [3,2,2,3], val = 3))
print(solution.removeElement1(nums = [0,1,2,2,3,0,4,2], val = 2))
print()
print(solution.removeElement2(nums = [3,2,2,3], val = 3))
print(solution.removeElement2(nums = [0,1,2,2,3,0,4,2], val = 2))