class Solution:

    def countSort(self, nums: List[int]) -> None:
        count: dict = {}
        minimum: int = 1e8
        maximum: int = -1e8

        for x in nums:
            minimum = min(minimum, x)
            maximum = max(maximum, x)

            count.setdefault(x, 0)
            count[x] += 1
        
        nums.clear()
        for x in range(minimum, maximum + 1):
            if x in count.keys():
                nums.extend([x] * count[x])

    def sortArray(self, nums: List[int]) -> List[int]:
        self.countSort(nums)
        return nums
        

