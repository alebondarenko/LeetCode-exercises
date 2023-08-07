class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0: return 0

        for i in range(1, x+1):
            if i*i == x: return i
            elif i*i > x: return i-1

solution = Solution()

print(solution.mySqrt(4))
print(solution.mySqrt(8))