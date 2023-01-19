
# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n: int = len(nums)
        maxSum: int = nums[0]
        minSum: int = nums[0]
        currMax: int = 0
        currMin: int = 0

        total: int = 0
        for x in nums:
            total += x
            currMax = max(currMax+x, x)
            currMin = min(currMin+x, x)

            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
