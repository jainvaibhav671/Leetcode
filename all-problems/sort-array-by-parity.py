#!/usr/bin/env python3

# https://leetcode.com/problems/sort-array-by-parity


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = n - 1

        while i < j:
            if nums[i] % 2 == 0:
                i += 1
            if nums[j] % 2 == 1:
                j -= 1

            if i >= j:
                break

            if nums[j] % 2 == 0 and nums[i] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        return nums
