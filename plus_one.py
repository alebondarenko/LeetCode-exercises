from typing import List

class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        add_one = int("".join(map(str, digits))) + 1

        return list(map(int, str(add_one)))

solution = Solution()

print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))
print(solution.plusOne([9]))