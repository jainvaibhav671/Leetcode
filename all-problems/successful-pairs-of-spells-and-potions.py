from typing import List
import math


class Solution:
    def find_smaller(self, target, potions):
        i = 0
        j = len(potions) - 1

        while i <= j:
            mid = i + (j - i) // 2
            if potions[mid] >= target:
                j = mid - 1
            elif potions[mid] < target:
                i = mid + 1

        # print(i, j, mid, target, potions)
        return j

    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        num_potions = len(potions)
        potions.sort()
        pairs = []

        for spell in spells:
            p = 0
            ind = self.find_smaller(math.ceil(success / spell), potions)
            if ind == -1:
                p = num_potions
            else:
                p = num_potions - ind - 1
                if p < 0:
                    p = 0

            pairs.append(p)

        return pairs
