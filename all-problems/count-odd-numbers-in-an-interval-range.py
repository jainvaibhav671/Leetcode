
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        n: int = high - low + 1
        half: int = n // 2
        if low % 2 and high % 2:
            return half + 1
        return half

