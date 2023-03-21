from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        subArray: int = 0
        ans: int = 0

        for num in nums:
            if num == 0:
                subArray += 1
            else:
                subArray = 0
            ans += subArray
        return ans
