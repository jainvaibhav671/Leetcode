#!/usr/bin/env python3

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = -1

        bp = 0
        sp = 0

        for i in range(len(prices)):
            if prices[bp] > prices[i]:
                max_profit = max(max_profit, prices[sp] - prices[bp])
                sp = i
                bp = i
            elif prices[sp] < prices[i]:
                sp = i
        max_profit = max(max_profit, prices[sp] - prices[bp])
        return max_profit
