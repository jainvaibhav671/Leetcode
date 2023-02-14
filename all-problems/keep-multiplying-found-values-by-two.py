
# https://leetcode.com/problems/keep-multiplying-found-values-by-two

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n: int = len(nums)
        nums.sort()
        while True:
            i = 0
            j = n - 1
            found = False
            while i <= j:
                mid = i + (j - i) // 2
                if nums[mid] == original:
                    found = True
                    break
                elif nums[mid] < original:
                    i = mid + 1
                else:
                    j = mid - 1
            if not found:
                break
            else:
                original *= 2 

        return original
