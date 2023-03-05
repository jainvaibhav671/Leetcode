class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi1: int = 0
        maxi2: int = 0

        for num in nums:
            if num > maxi1:
                maxi2 = maxi1
                maxi1 = num
            elif num > maxi2:
                maxi2 = num

        return (maxi1 - 1) * (maxi2 - 1)
