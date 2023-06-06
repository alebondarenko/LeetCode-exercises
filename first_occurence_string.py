# Given two strings needle and haystack, return the index of the first occurrence of 
# needle in haystack, or -1 if needle is not part of haystack

class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        end = len(needle)
        for start in range(len(haystack)):
            # print(haystack[start:end])
            if haystack[start:end] == needle:
                return start
            end+=1

        return -1


solution = Solution()
print(solution.strStr(haystack = "sadbutsad", needle = "sad"))
print(solution.strStr(haystack = "leetcode", needle = "leeto"))