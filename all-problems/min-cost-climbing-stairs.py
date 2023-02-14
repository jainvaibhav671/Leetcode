# https://leetcode.com/problems/min-cost-climbing-stairs

class Solution:
    def backtrack(self, cost: List[int], dp: List[int], i: int) -> int:
        n: int = len(cost)
        min_cost = 1e8
        if i > n:
            return min_cost
        elif i == n:
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        min_cost = min([
            min_cost,
            cost[i] + self.backtrack(cost, dp, i+1),
            cost[i] + self.backtrack(cost, dp, i+2)
        ])

        dp[i] = min_cost
        return dp[i]        


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n: int = len(cost)
        dp: List[int] = [-1] * (n + 1)
        return min(self.backtrack(cost, dp, 0), self.backtrack(cost, dp, 1))

