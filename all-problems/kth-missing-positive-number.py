from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        end = arr[-1]
        for i in range(1, end):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
        print(k)
        return end + k
