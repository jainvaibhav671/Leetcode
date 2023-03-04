from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        leftBound = minPos = maxPos = -1
        ans = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                leftBound = i

            if nums[i] == minK:
                minPos = i
            if nums[i] == maxK:
                maxPos = i

            ans += max(0, min(minPos, maxPos) - leftBound)

        return ans
