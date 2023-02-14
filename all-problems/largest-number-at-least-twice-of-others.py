# https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        highest = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[highest]:
                highest = i
        
        for x in nums:
            if x == nums[highest]:
                continue
            if nums[highest] < 2*x:
                return -1
        return highest

