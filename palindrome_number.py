class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """

        x = str(x)

        return x == x[::-1]
    
    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        half = 0
        while x > half:
            half = (half * 10) + (x % 10)
            x = x // 10
        return x == half or x == half // 10
    
solution = Solution()

x = 12321
print(solution.isPalindrome(x))
print(solution.isPalindrome2(x))