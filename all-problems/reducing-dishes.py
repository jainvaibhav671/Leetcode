from typing import List


class Solution:
    def __init__(self):
        self.memo: List[List[int]] = []
        self.n = 0
        self.int_min = -1e5
        self.ans = self.int_min

    def helper(self, satisfaction: List[int], i: int = 0, time: int = 1, currSum: int = 0) -> int:
        if i >= self.n or time > self.n:
            return 0

        if self.memo[i][time] != self.int_min:
            return self.memo[i][time]

        ltc = satisfaction[i] * time
        ltc = max([
            ltc + self.helper(satisfaction, i+1, time+1),
            self.helper(satisfaction, i+1, time)
        ])

        self.memo[i][time] = ltc
        return ltc

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        maximum = max(satisfaction)
        if maximum <= 0:
            return 0

        satisfaction.sort()
        self.n = len(satisfaction)
        self.memo = [[self.int_min] * (self.n + 1) for _ in range(self.n)]

        return self.helper(satisfaction)
