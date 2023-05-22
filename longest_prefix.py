class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        result = ""
        i = 1
        while len(set([w[:i] for w in strs])) == 1:
            result = set([w[:i] for w in strs])
            i += 1
        
        if result: return list(result)[0]
        else: return result


solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
print(solution.longestCommonPrefix(["dog","racecar","car"]))