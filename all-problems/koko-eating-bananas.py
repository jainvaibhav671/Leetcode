
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mis: int = 1
        mas: int = max(piles)

        print(sum(piles))
        while mis <= mas:
            speed: int = mis + (mas - mis) // 2
            actual_time: int = sum([ 1 if x <= speed else (x // speed) + 1 if x % speed else (x // speed) for x in piles ])
            print(speed, actual_time)
            if actual_time == h:
                mas = speed - 1
            elif actual_time > h:
                mis = speed + 1
            else:
                mas = speed - 1

        return mis
            