class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r = []

        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1

            r.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(r))


solution = Solution()

print(solution.addBinary(a="11", b="1"))
print(solution.addBinary(a = "1010", b = "1011"))