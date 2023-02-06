#!/usr/bin/env python3

# https://leetcode.com/problems/find-pivot-index/


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        sumLeft: List[int] = [0] * len(nums)
        total_sum: int = sum(nums)
        for i in range(0, len(nums)):
            if i > 0:
                sumLeft[i] = sumLeft[i - 1] + nums[i - 1]
            if sumLeft[i] == total_sum - sumLeft[i] - nums[i]:
                return i

        return -1
