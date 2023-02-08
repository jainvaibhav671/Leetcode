#!/usr/bin/env python3

# https://leetcode.com/problems/jump-game-ii


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        maxi = 0
        curr = 0
        jumps = 0

        for i in range(n):
            maxi = max(maxi, nums[i] + i)
            if curr == i:
                curr = maxi
                jumps += 1

            if curr >= n - 1:
                return jumps
        return jumps
