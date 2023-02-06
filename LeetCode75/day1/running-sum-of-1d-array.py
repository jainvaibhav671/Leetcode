#!/usr/bin/env python3
# https://leetcode.com/problems/running-sum-of-1d-array/


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        n: int = len(nums)

        ans: List[int] = []

        s: int = 0

        for i in range(n):

            s += nums[i]

            ans.append(s)

        return ans
