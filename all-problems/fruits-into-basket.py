#!/usr/bin/env python3
# https://leetcode.com/problems/fruit-into-baskets


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        j = 0
        res = 0

        count = {}
        while j < len(fruits):
            count.setdefault(fruits[j], 0)
            count[fruits[j]] += 1

            if len(count) <= 2:
                res = max([res, j - i + 1])
            else:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    count.pop(fruits[i])
                i += 1
            j += 1
        return res
