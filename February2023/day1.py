
# https://leetcode.com/problems/greatest-common-divisor-of-strings

class Solution:

    def gcd(a: int, b: int):
        high = max([a, b])
        low = min([a, b])

        while (high%low != 0):
            remainder = high%low
            high = low
            low = remainder
        return low

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str1[: gcd(len(str1), len(str2))]
        return ""
            
