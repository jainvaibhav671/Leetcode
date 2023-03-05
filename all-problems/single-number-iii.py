from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans: List[int] = []
        for x in nums:
            if len(ans) == 2:
                break

            if nums.count(x) == 1:
                ans.append(x)
        return ans
