from typing import List, Tuple


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        n: int = len(nums)
        subset: List[int] = []

        def helper(i: int) -> None:
            if tuple(subset) not in subsets:
                subsets.append(subset.copy())

            if i == n:
                return

            helper(i + 1)

            subset.append(nums[i])
            helper(i + 1)
            subset.pop()

        helper(0)
        return subsets
