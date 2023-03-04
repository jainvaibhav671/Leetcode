class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [len(list(filter(lambda x: x < y, nums))) for y in nums]
