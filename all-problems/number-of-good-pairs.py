class Solution:
    def findAll(self, nums: List[int], target: int):
        i = 0
        j = len(nums) - 1

        found = []
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] == target:
                found.append(mid)
                i = mid + 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return found

    def numIdenticalPairs(self, nums: List[int]) -> int:
        n: int = len(nums)
        if n == 1:
            return 0

        cnt = 0
        for i in range(n):
            _next = nums[i + 1 :].count(nums[i])
            cnt += _next
        return cnt
