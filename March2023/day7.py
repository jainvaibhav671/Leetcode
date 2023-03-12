from typing import List
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left: int = 1
        right: int = totalTrips * max(time)

        while left <= right:
            t: int = left + (right - left) // 2
            actualTrips: int = sum([ t // ti for ti in time ])
            if totalTrips <= actualTrips:
                right = t - 1
            else:
                left = t + 1
        return left