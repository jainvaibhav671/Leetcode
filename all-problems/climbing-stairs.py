# https://leetcode.com/problems/climbing-stairs

class Solution:

    def backtrack(self, n: int, dp: List[int]) -> int:
        cnt: int = 0
        if n < 0:
            return cnt
        if n == 0:
            return cnt + 1

        if dp[n] != -1:
            return dp[n]
        
        cnt += self.backtrack(n-1, dp)
        cnt += self.backtrack(n-2, dp)

        dp[n] = cnt
        return cnt

    def climbStairs(self, n: int) -> int:
        dp: List[int] = [-1] * (n+1)
        return self.backtrack(n, dp)
