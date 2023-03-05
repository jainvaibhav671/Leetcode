from typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        cnt: int = 0
        for start, end in zip(startTime, endTime):
            if queryTime >= start and queryTime <= end:
                cnt += 1

        return cnt
