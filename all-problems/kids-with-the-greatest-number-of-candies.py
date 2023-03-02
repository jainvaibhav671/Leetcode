from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        most_candies: int = max(candies)
        result: List[bool] = [candy + extraCandies >= most_candies for candy in candies]
        return result
