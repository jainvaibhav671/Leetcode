
# https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n: int = len(nums)
        prefixSum: List[int] = [0]*k

        prefixSum[0] += 1
        cnt: int = 0
        currSum: int = 0

        for i in range(n):
            currSum = (currSum + nums[i]%k + k)%k
            cnt += prefixSum[currSum]
            prefixSum[currSum] += 1

        return cnt   
