# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        check_dict = {"(":")","{":"}","[":"]"}

        if len(s) % 2 != 0:
            return False
        for i in range(0, len(s), 2):
            if check_dict[s[i]] != s[i+1]:
                return False
        return True
        
solution = Solution()

print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("[()]")) # would be interesting to solve this case