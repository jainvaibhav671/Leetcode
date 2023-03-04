class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            digits = int(math.log10(num)) + 1
            if digits % 2 == 0:
                cnt += 1
        return cnt
